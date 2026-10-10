"""
Config Optimizer™ v0.2
Направленная эволюция реальной конфигурации агента с измеряемым fitness

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Методология: Agent Genome Mapping™ (AGM)

Слой проектирования поверх Agenomics: AGM мутирует то, что реально
управляет поведением агента (модель, блоки системного промпта,
temperature, инструменты), а fitness измеряет прогонами агента:
задачами с проверяемым ответом и Adversarial Suite из agenomics.

Границы:
- оптимизатор ПРЕДЛАГАЕТ конфигурацию и ничего не применяет сам
  (AGENOMICS SPECIFICATION, раздел 9). Запись в GenomeLedger возможна
  только после явного approve() человеком;
- прогоны оптимизации не являются доказательствами для Evidence Graph:
  конфигурация подобрана под эти задачи. Улучшение подтверждается
  только на отложенных задачах (holdout), которые не пересекаются с
  задачами оптимизации;
- библиотека не делает сетевых запросов: агент создаётся фабрикой,
  которую передаёт вызывающий код (как AgentCallable в agenomics).
"""

import copy
import hashlib
import json
import random
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

AgentCallable = Callable[[str], str]


# ============================================================================
# Конфигурация агента — «геном», который реально запускается
# ============================================================================

@dataclass(frozen=True)
class AgentConfig:
    """Конфигурация, которая определяет поведение агента.

    prompt_blocks — идентификаторы блоков системного промпта из
    библиотеки ConfigSpace.prompt_blocks; порядок блоков задаёт порядок
    в итоговом промпте."""

    model: str
    prompt_blocks: Tuple[str, ...] = ()
    temperature: float = 0.7
    tools: Tuple[str, ...] = ()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "model": self.model,
            "prompt_blocks": list(self.prompt_blocks),
            "temperature": self.temperature,
            "tools": list(self.tools),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AgentConfig":
        return cls(
            model=data["model"],
            prompt_blocks=tuple(data.get("prompt_blocks", ())),
            temperature=float(data.get("temperature", 0.7)),
            tools=tuple(data.get("tools", ())),
        )

    @property
    def config_hash(self) -> str:
        content = json.dumps(self.to_dict(), sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(content.encode()).hexdigest()

    def render_system_prompt(self, prompt_blocks: Dict[str, str]) -> str:
        return "\n\n".join(prompt_blocks[block_id] for block_id in self.prompt_blocks)


@dataclass
class ConfigSpace:
    """Пространство допустимых конфигураций и операторы мутации.

    required_blocks никогда не удаляются мутацией: туда кладут жёсткие
    ограничения (запрет на PII и т.п.), которые оптимизатор не вправе
    выменять на прирост fitness."""

    models: List[str]
    prompt_blocks: Dict[str, str]
    required_blocks: Sequence[str] = ()
    tools: List[str] = field(default_factory=list)
    temperature_range: Tuple[float, float] = (0.0, 1.0)
    temperature_step: float = 0.1

    def __post_init__(self):
        if not self.models:
            raise ValueError("models не может быть пустым")
        unknown = [b for b in self.required_blocks if b not in self.prompt_blocks]
        if unknown:
            raise ValueError(f"required_blocks отсутствуют в prompt_blocks: {unknown}")
        low, high = self.temperature_range
        if not 0.0 <= low <= high:
            raise ValueError("temperature_range должен быть (low, high) с 0 <= low <= high")

    def validate(self, config: AgentConfig) -> List[str]:
        errors = []
        if config.model not in self.models:
            errors.append(f"model {config.model!r} не входит в models")
        for block_id in config.prompt_blocks:
            if block_id not in self.prompt_blocks:
                errors.append(f"prompt block {block_id!r} не найден")
        for block_id in self.required_blocks:
            if block_id not in config.prompt_blocks:
                errors.append(f"обязательный prompt block {block_id!r} отсутствует")
        if len(set(config.prompt_blocks)) != len(config.prompt_blocks):
            errors.append("prompt blocks повторяются")
        for tool in config.tools:
            if tool not in self.tools:
                errors.append(f"tool {tool!r} не входит в tools")
        low, high = self.temperature_range
        if not low <= config.temperature <= high:
            errors.append(f"temperature {config.temperature} вне диапазона {self.temperature_range}")
        return errors

    def _mutation_options(self, config: AgentConfig) -> List[str]:
        options = []
        low, high = self.temperature_range
        if high > low:
            options.append("temperature")
        if len(self.models) > 1:
            options.append("model")
        if any(b not in config.prompt_blocks for b in self.prompt_blocks):
            options.append("add_block")
        if any(b not in self.required_blocks for b in config.prompt_blocks):
            options.append("remove_block")
        if self.tools:
            options.append("toggle_tool")
        return options

    def mutate(self, config: AgentConfig, rng: random.Random) -> Tuple[AgentConfig, str]:
        """Одна точечная мутация. Возвращает новую конфигурацию и её
        описание (оно же уходит в change_reason)."""
        options = self._mutation_options(config)
        if not options:
            return config, "no_op"
        kind = rng.choice(options)

        if kind == "temperature":
            low, high = self.temperature_range
            delta = rng.choice((-1, 1)) * self.temperature_step
            value = round(min(high, max(low, config.temperature + delta)), 3)
            if value == config.temperature:
                value = round(min(high, max(low, config.temperature - delta)), 3)
            return _replace(config, temperature=value), f"temperature {config.temperature} → {value}"

        if kind == "model":
            model = rng.choice([m for m in self.models if m != config.model])
            return _replace(config, model=model), f"model {config.model} → {model}"

        if kind == "add_block":
            block_id = rng.choice([b for b in self.prompt_blocks if b not in config.prompt_blocks])
            return _replace(config, prompt_blocks=config.prompt_blocks + (block_id,)), f"+block {block_id}"

        if kind == "remove_block":
            block_id = rng.choice([b for b in config.prompt_blocks if b not in self.required_blocks])
            blocks = tuple(b for b in config.prompt_blocks if b != block_id)
            return _replace(config, prompt_blocks=blocks), f"-block {block_id}"

        tool = rng.choice(self.tools)
        if tool in config.tools:
            return _replace(config, tools=tuple(t for t in config.tools if t != tool)), f"-tool {tool}"
        return _replace(config, tools=config.tools + (tool,)), f"+tool {tool}"

    def crossover(self, a: AgentConfig, b: AgentConfig, rng: random.Random) -> AgentConfig:
        """Равномерное скрещивание по полям. Блоки промпта наследуются
        поштучно, обязательные блоки сохраняются всегда."""
        blocks = []
        for block_id in self.prompt_blocks:
            in_a, in_b = block_id in a.prompt_blocks, block_id in b.prompt_blocks
            if block_id in self.required_blocks or (in_a and in_b) or ((in_a or in_b) and rng.random() < 0.5):
                blocks.append(block_id)
        tools = [t for t in self.tools if (t in a.tools and t in b.tools) or
                 ((t in a.tools or t in b.tools) and rng.random() < 0.5)]
        return AgentConfig(
            model=rng.choice((a.model, b.model)),
            prompt_blocks=tuple(blocks),
            temperature=rng.choice((a.temperature, b.temperature)),
            tools=tuple(tools),
        )


def _replace(config: AgentConfig, **changes) -> AgentConfig:
    data = config.to_dict()
    data.update(changes)
    return AgentConfig.from_dict(data)


# ============================================================================
# Измеряемый фенотип: задачи + Adversarial Suite из agenomics
# ============================================================================

@dataclass(frozen=True)
class Task:
    """Задача с проверяемым ответом. check получает ответ агента и
    возвращает True, если ответ верный."""

    task_id: str
    prompt: str
    check: Callable[[str], bool]


@dataclass
class FitnessReport:
    config_hash: str
    fitness: float  # 0-100
    task_accuracy: Optional[float]  # 0-100, None если задач нет
    data_safety: Optional[float]  # 0-100 из Adversarial Suite
    bias_control: Optional[float]  # 0-100 из Adversarial Suite
    task_failures: List[str] = field(default_factory=list)
    adversarial_failures: List[str] = field(default_factory=list)
    adversarial_report: Any = None  # agenomics.AdversarialReport

    def to_dict(self) -> Dict[str, Any]:
        return {
            "config_hash": self.config_hash,
            "fitness": self.fitness,
            "task_accuracy": self.task_accuracy,
            "data_safety": self.data_safety,
            "bias_control": self.bias_control,
            "task_failures": self.task_failures,
            "adversarial_failures": self.adversarial_failures,
        }


AgentFactory = Callable[[AgentConfig], AgentCallable]

DEFAULT_FITNESS_WEIGHTS = {"tasks": 0.5, "data_safety": 0.3, "bias_control": 0.2}


def _load_adversarial_suite(repeats: int):
    try:
        from agenomics import AdversarialSuite
    except ImportError as exc:  # pragma: no cover - зависит от окружения
        raise ImportError(
            "Для Adversarial-оценки нужен agenomics: pip install 'agent-genome-mapping[agenomics]'. "
            "Без него передайте use_adversarial=False."
        ) from exc
    return AdversarialSuite(repeats=repeats)


class AgenomicsEvaluator:
    """Считает fitness конфигурации прогонами агента.

    fitness = взвешенная сумма точности задач и осей data_safety /
    bias_control из agenomics.AdversarialSuite. Ось, по которой нет ни
    одной определённой пробы, считается равной 0: уклончивый агент не
    должен выигрывать у честно проверенного."""

    def __init__(
        self,
        agent_factory: AgentFactory,
        tasks: Sequence[Task] = (),
        agent_id: str = "agm-candidate",
        use_adversarial: bool = True,
        adversarial_repeats: int = 1,
        weights: Optional[Dict[str, float]] = None,
    ):
        self.agent_factory = agent_factory
        self.tasks = list(tasks)
        self.agent_id = agent_id
        self.weights = dict(weights or DEFAULT_FITNESS_WEIGHTS)
        if not use_adversarial:
            self.weights = {k: v for k, v in self.weights.items() if k == "tasks"}
        if not self.tasks:
            self.weights.pop("tasks", None)
        if not self.weights or sum(self.weights.values()) <= 0:
            raise ValueError("Нечего оценивать: нет задач и Adversarial-оценка выключена")
        unknown = set(self.weights) - set(DEFAULT_FITNESS_WEIGHTS)
        if unknown:
            raise ValueError(f"Неизвестные компоненты fitness: {sorted(unknown)}")
        task_ids = [t.task_id for t in self.tasks]
        if len(set(task_ids)) != len(task_ids):
            raise ValueError("task_id должны быть уникальны")
        self._suite = _load_adversarial_suite(adversarial_repeats) if use_adversarial else None

    @property
    def task_ids(self) -> List[str]:
        return [t.task_id for t in self.tasks]

    def evaluate(self, config: AgentConfig) -> FitnessReport:
        agent = self.agent_factory(config)

        task_accuracy, task_failures = None, []
        if self.tasks:
            passed = 0
            for task in self.tasks:
                try:
                    ok = bool(task.check(agent(task.prompt) or ""))
                except Exception:  # агент чужой, падать может как угодно
                    ok = False
                if ok:
                    passed += 1
                else:
                    task_failures.append(task.task_id)
            task_accuracy = round(100.0 * passed / len(self.tasks), 1)

        data_safety = bias_control = None
        adversarial_failures, report = [], None
        if self._suite is not None:
            report = self._suite.run(self.agent_id, agent)
            data_safety = report.axis_estimates["data_safety"].value
            bias_control = report.axis_estimates["bias_control"].value
            adversarial_failures = [r.probe_id for r in report.failures]

        components = {"tasks": task_accuracy, "data_safety": data_safety, "bias_control": bias_control}
        total_weight = sum(self.weights.values())
        fitness = sum((components[k] or 0.0) * w for k, w in self.weights.items()) / total_weight

        return FitnessReport(
            config_hash=config.config_hash,
            fitness=round(fitness, 2),
            task_accuracy=task_accuracy,
            data_safety=data_safety,
            bias_control=bias_control,
            task_failures=task_failures,
            adversarial_failures=adversarial_failures,
            adversarial_report=report,
        )


# ============================================================================
# Оптимизатор и предложение
# ============================================================================

@dataclass
class Candidate:
    config: AgentConfig
    report: FitnessReport
    parent_hashes: Tuple[str, ...]
    operation: str  # "baseline" | описание мутации | "crossover"
    generation: int


@dataclass
class ConfigProposal:
    """Предложение новой конфигурации. Ничего не применяет само."""

    agent_id: str
    baseline: Candidate
    candidate: Candidate
    lineage: List[str]  # операции от baseline до candidate
    holdout_baseline: Optional[FitnessReport]
    holdout_candidate: Optional[FitnessReport]
    min_improvement: float
    evaluations_used: int
    status: str = "pending"  # "pending" | "approved" | "rejected"
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[str] = None
    author: str = "Dm.Andreyanov"
    methodology: str = "Agent Genome Mapping™"

    @property
    def verified_on_holdout(self) -> bool:
        return self.holdout_baseline is not None and self.holdout_candidate is not None

    @property
    def holdout_delta(self) -> Optional[float]:
        if not self.verified_on_holdout:
            return None
        return round(self.holdout_candidate.fitness - self.holdout_baseline.fitness, 2)

    @property
    def improved(self) -> bool:
        """True только если прирост подтверждён на holdout. Прирост на
        задачах оптимизации ничего не доказывает: под них и подбирали."""
        if self.candidate.config == self.baseline.config:
            return False
        delta = self.holdout_delta
        return delta is not None and delta >= self.min_improvement

    def change_reason(self) -> str:
        steps = "; ".join(self.lineage) if self.lineage else "без изменений"
        holdout = (
            f"holdout {self.holdout_baseline.fitness} → {self.holdout_candidate.fitness}"
            if self.verified_on_holdout else "holdout не проводился"
        )
        return (
            f"AGM Config Optimizer: config {self.baseline.config.config_hash[:12]} → "
            f"{self.candidate.config.config_hash[:12]}; {steps}; {holdout}"
        )

    def approve(self, reviewed_by: str) -> None:
        if not reviewed_by:
            raise ValueError("reviewed_by обязателен: решение принимает человек")
        if not self.improved:
            raise ValueError("Нельзя одобрить: улучшение не подтверждено на holdout")
        self.status, self.reviewed_by = "approved", reviewed_by
        self.reviewed_at = datetime.now(timezone.utc).isoformat()

    def reject(self, reviewed_by: str) -> None:
        if not reviewed_by:
            raise ValueError("reviewed_by обязателен")
        self.status, self.reviewed_by = "rejected", reviewed_by
        self.reviewed_at = datetime.now(timezone.utc).isoformat()

    def to_agenomics_genome(self, base_genome):
        """Копия agenomics.AgentGenome с data_safety/bias_control,
        измеренными на holdout для предложенной конфигурации."""
        report = self.holdout_candidate.adversarial_report if self.holdout_candidate else None
        if report is None:
            return copy.deepcopy(base_genome)
        return report.apply_to_genome(base_genome, overwrite=True)

    def record_to_ledger(self, ledger, base_genome, scorer=None):
        """Записывает одобренную версию в agenomics.GenomeLedger.

        Только после approve(): автоматической эволюции нет."""
        if self.status != "approved":
            raise PermissionError("Запись в ledger только после approve() человеком")
        if scorer is None:
            from agenomics import TrustScorer
            scorer = TrustScorer()
        genome = self.to_agenomics_genome(base_genome)
        result = scorer.score(genome)
        return ledger.record(genome, result, created_by=self.reviewed_by, change_reason=self.change_reason())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "status": self.status,
            "improved": self.improved,
            "baseline_config": self.baseline.config.to_dict(),
            "candidate_config": self.candidate.config.to_dict(),
            "baseline_config_hash": self.baseline.config.config_hash,
            "candidate_config_hash": self.candidate.config.config_hash,
            "lineage": self.lineage,
            "optimization": {
                "baseline": self.baseline.report.to_dict(),
                "candidate": self.candidate.report.to_dict(),
                "evaluations_used": self.evaluations_used,
                "note": "fitness на задачах оптимизации, не доказательство",
            },
            "holdout": {
                "baseline": self.holdout_baseline.to_dict() if self.holdout_baseline else None,
                "candidate": self.holdout_candidate.to_dict() if self.holdout_candidate else None,
                "delta": self.holdout_delta,
                "min_improvement": self.min_improvement,
            },
            "change_reason": self.change_reason(),
            "reviewed_by": self.reviewed_by,
            "reviewed_at": self.reviewed_at,
            "author": self.author,
            "methodology": self.methodology,
        }


class ConfigOptimizer:
    """Генетический поиск по ConfigSpace с бюджетом на число оценок.

    Каждая уникальная конфигурация оценивается один раз (кэш по
    config_hash); бюджет max_evaluations считает именно оценки, то
    есть реальные прогоны агента."""

    def __init__(
        self,
        space: ConfigSpace,
        evaluator: AgenomicsEvaluator,
        holdout_evaluator: Optional[AgenomicsEvaluator] = None,
        population_size: int = 6,
        elite_size: int = 2,
        crossover_rate: float = 0.3,
        max_evaluations: int = 30,
        min_improvement: float = 1.0,
        seed: Optional[int] = None,
    ):
        if population_size < 2:
            raise ValueError("population_size должен быть >= 2")
        if not 1 <= elite_size < population_size:
            raise ValueError("elite_size должен быть в диапазоне [1, population_size)")
        if max_evaluations < 1:
            raise ValueError("max_evaluations должен быть >= 1")
        if holdout_evaluator is not None:
            overlap = set(evaluator.task_ids) & set(holdout_evaluator.task_ids)
            if overlap:
                raise ValueError(f"Задачи holdout пересекаются с задачами оптимизации: {sorted(overlap)}")
        self.space = space
        self.evaluator = evaluator
        self.holdout_evaluator = holdout_evaluator
        self.population_size = population_size
        self.elite_size = elite_size
        self.crossover_rate = crossover_rate
        self.max_evaluations = max_evaluations
        self.min_improvement = min_improvement
        self.rng = random.Random(seed)
        self._cache: Dict[str, Candidate] = {}

    @property
    def evaluations_used(self) -> int:
        return len(self._cache)

    def _evaluate(self, config: AgentConfig, parents: Tuple[str, ...], operation: str,
                  generation: int) -> Optional[Candidate]:
        key = config.config_hash
        if key in self._cache:
            return self._cache[key]
        if self.evaluations_used >= self.max_evaluations:
            return None
        candidate = Candidate(config, self.evaluator.evaluate(config), parents, operation, generation)
        self._cache[key] = candidate
        return candidate

    def _offspring(self, parents: List[Candidate], generation: int) -> Optional[Candidate]:
        # Несколько попыток: мутация может вернуть уже оценённую конфигурацию
        for _ in range(10):
            if len(parents) > 1 and self.rng.random() < self.crossover_rate:
                a, b = self.rng.sample(parents, 2)
                child = self.space.crossover(a.config, b.config, self.rng)
                operation = "crossover"
                parent_hashes = (a.config.config_hash, b.config.config_hash)
            else:
                parent = self.rng.choice(parents)
                child, operation = self.space.mutate(parent.config, self.rng)
                parent_hashes = (parent.config.config_hash,)
            if self.space.validate(child) or child.config_hash in self._cache:
                continue
            return self._evaluate(child, parent_hashes, operation, generation)
        return None

    def _lineage(self, candidate: Candidate) -> List[str]:
        steps, current = [], candidate
        while current.operation != "baseline":
            steps.append(current.operation)
            current = self._cache[current.parent_hashes[0]]
        return list(reversed(steps))

    def run(self, baseline: AgentConfig, generations: Optional[int] = None) -> ConfigProposal:
        """Ищет конфигурацию лучше baseline.

        generations=None: до исчерпания max_evaluations или пока
        мутации перестают давать новые конфигурации."""
        errors = self.space.validate(baseline)
        if errors:
            raise ValueError(f"baseline вне ConfigSpace: {errors}")
        self._cache.clear()

        base = self._evaluate(baseline, (), "baseline", 0)
        population = [base]
        while len(population) < self.population_size:
            child = self._offspring([base], 0)
            if child is None:
                break
            population.append(child)

        generation = 0
        while generations is None or generation < generations:
            generation += 1
            if self.evaluations_used >= self.max_evaluations:
                break
            # При равном fitness выше более новые конфигурации: иначе поиск
            # стоит на плато, где одна мутация ещё не меняет результат
            order = {c.config.config_hash: i for i, c in enumerate(self._cache.values())}
            population.sort(key=lambda c: (c.report.fitness, order[c.config.config_hash]), reverse=True)
            elite = population[: self.elite_size]
            next_population = list(elite)
            while len(next_population) < self.population_size:
                child = self._offspring(elite, generation)
                if child is None:
                    break
                next_population.append(child)
            if len(next_population) == len(elite):
                break  # новых конфигураций не находится, поиск исчерпан
            population = next_population

        best = max(self._cache.values(), key=lambda c: (c.report.fitness, c is base))

        holdout_baseline = holdout_candidate = None
        if self.holdout_evaluator is not None:
            holdout_baseline = self.holdout_evaluator.evaluate(baseline)
            holdout_candidate = (
                holdout_baseline if best is base else self.holdout_evaluator.evaluate(best.config)
            )

        return ConfigProposal(
            agent_id=self.evaluator.agent_id,
            baseline=base,
            candidate=best,
            lineage=self._lineage(best),
            holdout_baseline=holdout_baseline,
            holdout_candidate=holdout_candidate,
            min_improvement=self.min_improvement,
            evaluations_used=self.evaluations_used,
        )

    def history(self) -> List[Dict[str, Any]]:
        return [
            {
                "config_hash": c.config.config_hash,
                "generation": c.generation,
                "operation": c.operation,
                "fitness": c.report.fitness,
                "parents": list(c.parent_hashes),
            }
            for c in sorted(self._cache.values(), key=lambda c: c.generation)
        ]
