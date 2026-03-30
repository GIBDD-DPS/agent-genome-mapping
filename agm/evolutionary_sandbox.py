"""
Evolutionary Sandbox™ v1.0
Среда для направленной эволюции ИИ-агентов

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Методология: Agent Genome Mapping™ (AGM)
"""

import random
import copy
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class BreedingStrategy(Enum):
    BEST_OF_BOTH = "best_of_both"
    AVERAGE = "average"
    RANDOM_SELECT = "random_select"
    PARENT_A_DOMINANT = "parent_a_dominant"
    PARENT_B_DOMINANT = "parent_b_dominant"


class MutationType(Enum):
    UNIFORM = "uniform"
    GAUSSIAN = "gaussian"
    BOUNDED = "bounded"


class SelectionMethod(Enum):
    TOURNAMENT = "tournament"
    ROULETTE = "roulette"
    RANK_BASED = "rank_based"
    ELITISM = "elitism"


@dataclass
class EvolutionEvent:
    """
    Событие эволюции (для журналирования в Genome Ledger™)
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """
    event_type: str  # "breed", "mutate", "select"
    timestamp: str
    parent_ids: List[str]
    child_id: str
    changes: Dict[str, Any]
    author: str = "Dm.Andreyanov"
    methodology: str = "Agent Genome Mapping™"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_type": self.event_type,
            "timestamp": self.timestamp,
            "parent_ids": self.parent_ids,
            "child_id": self.child_id,
            "changes": self.changes,
            "author": self.author,
            "methodology": self.methodology
        }


@dataclass
class EvolutionResult:
    """
    Результат эволюционной операции
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """
    success: bool
    child_genome: Optional[Dict[str, Any]]
    events: List[EvolutionEvent]
    metrics: Dict[str, Any]
    author: str = "Dm.Andreyanov"
    methodology: str = "Agent Genome Mapping™"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "child_genome": self.child_genome,
            "events": [e.to_dict() for e in self.events],
            "metrics": self.metrics,
            "author": self.author,
            "methodology": self.methodology
        }


class EvolutionarySandbox:
    """
    Evolutionary Sandbox™ — безопасная среда для направленной эволюции ИИ-агентов
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """

    def __init__(
        self,
        mutation_rate: float = 0.02,
        max_generations: int = 100,
        population_size: int = 10,
        elitism_count: int = 2,
        random_seed: Optional[int] = None
    ):
        """
        Инициализация эволюционной песочницы

        Args:
            mutation_rate: Базовая скорость мутации (0.0 - 0.1)
            max_generations: Максимальное число поколений
            population_size: Размер популяции
            elitism_count: Количество лучших особей для сохранения
            random_seed: Сид для воспроизводимости
        """
        self.author = "Dm.Andreyanov"
        self.methodology = "Agent Genome Mapping™"
        
        self.mutation_rate = min(max(mutation_rate, 0.0), 0.1)
        self.max_generations = max_generations
        self.population_size = max(population_size, 4)
        self.elitism_count = min(elitism_count, population_size // 2)
        
        if random_seed is not None:
            random.seed(random_seed)
        
        self.generation = 0
        self.population: List[Dict[str, Any]] = []
        self.fitness_scores: List[float] = []
        self.ledger: List[EvolutionEvent] = []
        self.best_genome: Optional[Dict[str, Any]] = None
        self.best_fitness: float = 0.0

    def _log_event(self, event: EvolutionEvent) -> None:
        """Журналирование события в Genome Ledger™"""
        self.ledger.append(event)

    def _validate_genome(self, genome: Dict[str, Any]) -> bool:
        """Базовая валидация структуры генома"""
        required_keys = ["meta", "cognitive_genes", "ethics_genes", "social_genes", "meta_genes"]
        return all(key in genome for key in required_keys)

    def _generate_child_id(self, parent_ids: List[str]) -> str:
        """Генерация уникального ID для потомка"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"hybrid-{self.generation + 1}-{timestamp}"

    # ========================================================================
    # BREEDING (Скрещивание)
    # ========================================================================

    def breed(
        self,
        genome_A: Dict[str, Any],
        genome_B: Dict[str, Any],
        strategy: BreedingStrategy = BreedingStrategy.BEST_OF_BOTH
    ) -> EvolutionResult:
        """
        Скрещивание двух агентов для получения гибрида

        Args:
            genome_A: Геном первого родителя
            genome_B: Геном второго родителя
            strategy: Стратегия скрещивания

        Returns:
            EvolutionResult: Результат скрещивания
        """
        events = []
        
        if not self._validate_genome(genome_A) or not self._validate_genome(genome_B):
            return EvolutionResult(
                success=False,
                child_genome=None,
                events=events,
                metrics={"error": "Invalid genome structure"},
                author=self.author,
                methodology=self.methodology
            )

        child_genome = self._breed_genomes(genome_A, genome_B, strategy)
        
        event = EvolutionEvent(
            event_type="breed",
            timestamp=datetime.now().isoformat(),
            parent_ids=[genome_A["meta"]["id"], genome_B["meta"]["id"]],
            child_id=child_genome["meta"]["id"],
            changes={"strategy": strategy.value}
        )
        events.append(event)
        self._log_event(event)

        return EvolutionResult(
            success=True,
            child_genome=child_genome,
            events=events,
            metrics={
                "strategy": strategy.value,
                "generation": self.generation,
                "ledger_entries": len(self.ledger)
            },
            author=self.author,
            methodology=self.methodology
        )

    def _breed_genomes(
        self,
        genome_A: Dict[str, Any],
        genome_B: Dict[str, Any],
        strategy: BreedingStrategy
    ) -> Dict[str, Any]:
        """Внутренний метод скрещивания геномов"""
        
        child = copy.deepcopy(genome_A)
        child["meta"]["id"] = self._generate_child_id([genome_A["meta"]["id"], genome_B["meta"]["id"]])
        child["meta"]["version"] = f"{self.generation + 1}.0"
        child["meta"]["parents"] = [genome_A["meta"]["id"], genome_B["meta"]["id"]]
        child["meta"]["created"] = datetime.now().isoformat()

        if strategy == BreedingStrategy.BEST_OF_BOTH:
            # Выбираем лучшие значения по каждому параметру
            child["cognitive_genes"]["reasoning_depth"] = self._select_best_reasoning(
                genome_A["cognitive_genes"]["reasoning_depth"],
                genome_B["cognitive_genes"]["reasoning_depth"]
            )
            child["cognitive_genes"]["creativity_coefficient"] = max(
                genome_A["cognitive_genes"]["creativity_coefficient"],
                genome_B["cognitive_genes"]["creativity_coefficient"]
            )
            child["cognitive_genes"]["learning_rate"] = max(
                genome_A["cognitive_genes"]["learning_rate"],
                genome_B["cognitive_genes"]["learning_rate"]
            )
            child["ethics_genes"]["bias_threshold"] = min(
                genome_A["ethics_genes"]["bias_threshold"],
                genome_B["ethics_genes"]["bias_threshold"]
            )
            child["ethics_genes"]["hard_constraints"] = list(set(
                genome_A["ethics_genes"]["hard_constraints"] +
                genome_B["ethics_genes"]["hard_constraints"]
            ))

        elif strategy == BreedingStrategy.AVERAGE:
            # Усредняем числовые значения
            child["cognitive_genes"]["creativity_coefficient"] = (
                genome_A["cognitive_genes"]["creativity_coefficient"] +
                genome_B["cognitive_genes"]["creativity_coefficient"]
            ) / 2
            child["cognitive_genes"]["learning_rate"] = (
                genome_A["cognitive_genes"]["learning_rate"] +
                genome_B["cognitive_genes"]["learning_rate"]
            ) / 2
            child["ethics_genes"]["bias_threshold"] = (
                genome_A["ethics_genes"]["bias_threshold"] +
                genome_B["ethics_genes"]["bias_threshold"]
            ) / 2

        elif strategy == BreedingStrategy.RANDOM_SELECT:
            # Случайный выбор от одного из родителей
            for key in child["cognitive_genes"]:
                if random.random() > 0.5:
                    child["cognitive_genes"][key] = genome_B["cognitive_genes"][key]
            for key in child["ethics_genes"]:
                if random.random() > 0.5:
                    child["ethics_genes"][key] = genome_B["ethics_genes"][key]

        elif strategy == BreedingStrategy.PARENT_A_DOMINANT:
            # Родитель A доминирует с небольшими вкраплениями от B
            for key in child["cognitive_genes"]:
                if random.random() > 0.8:
                    child["cognitive_genes"][key] = genome_B["cognitive_genes"][key]

        elif strategy == BreedingStrategy.PARENT_B_DOMINANT:
            # Родитель B доминирует с небольшими вкраплениями от A
            child = copy.deepcopy(genome_B)
            child["meta"]["id"] = self._generate_child_id([genome_A["meta"]["id"], genome_B["meta"]["id"]])
            for key in child["cognitive_genes"]:
                if random.random() > 0.8:
                    child["cognitive_genes"][key] = genome_A["cognitive_genes"][key]

        return child

    def _select_best_reasoning(self, depth_A: str, depth_B: str) -> str:
        """Выбирает лучшую глубину рассуждений"""
        order = {"low": 1, "medium": 2, "high": 3}
        return depth_A if order.get(depth_A, 2) >= order.get(depth_B, 2) else depth_B

    # ========================================================================
    # MUTATION (Мутация)
    # ========================================================================

    def mutate(
        self,
        genome: Dict[str, Any],
        rate: Optional[float] = None,
        mutation_type: MutationType = MutationType.UNIFORM
    ) -> EvolutionResult:
        """
        Направленная мутация генома с контролем рисков

        Args:
            genome: Геном для мутации
            rate: Скорость мутации (переопределяет базовую)
            mutation_type: Тип мутации

        Returns:
            EvolutionResult: Результат мутации
        """
        events = []
        rate = rate if rate is not None else self.mutation_rate
        rate = min(max(rate, 0.0), 0.1)

        if not self._validate_genome(genome):
            return EvolutionResult(
                success=False,
                child_genome=None,
                events=events,
                metrics={"error": "Invalid genome structure"},
                author=self.author,
                methodology=self.methodology
            )

        mutated_genome = copy.deepcopy(genome)
        mutated_genome["meta"]["id"] = f"{genome['meta']['id']}-mutated-{self.generation + 1}"
        
        changes = self._apply_mutations(mutated_genome, rate, mutation_type)

        event = EvolutionEvent(
            event_type="mutate",
            timestamp=datetime.now().isoformat(),
            parent_ids=[genome["meta"]["id"]],
            child_id=mutated_genome["meta"]["id"],
            changes=changes
        )
        events.append(event)
        self._log_event(event)

        return EvolutionResult(
            success=True,
            child_genome=mutated_genome,
            events=events,
            metrics={
                "mutation_rate": rate,
                "mutation_type": mutation_type.value,
                "changes_count": len(changes),
                "generation": self.generation
            },
            author=self.author,
            methodology=self.methodology
        )

    def _apply_mutations(
        self,
        genome: Dict[str, Any],
        rate: float,
        mutation_type: MutationType
    ) -> Dict[str, Any]:
        """Применяет мутации к геному"""
        changes = {}

        # Мутация креативности
        if random.random() < rate:
            old_value = genome["cognitive_genes"]["creativity_coefficient"]
            if mutation_type == MutationType.GAUSSIAN:
                delta = random.gauss(0, 0.1)
            else:
                delta = random.uniform(-0.1, 0.1)
            new_value = max(0.0, min(1.0, old_value + delta))
            genome["cognitive_genes"]["creativity_coefficient"] = new_value
            changes["creativity_coefficient"] = {"old": old_value, "new": new_value}

        # Мутация скорости обучения
        if random.random() < rate:
            old_value = genome["cognitive_genes"]["learning_rate"]
            delta = random.uniform(-0.05, 0.05)
            new_value = max(0.0, min(1.0, old_value + delta))
            genome["cognitive_genes"]["learning_rate"] = new_value
            changes["learning_rate"] = {"old": old_value, "new": new_value}

        # Мутация порога смещения (bias)
        if random.random() < rate:
            old_value = genome["ethics_genes"]["bias_threshold"]
            delta = random.uniform(-0.02, 0.02)
            new_value = max(0.0, min(1.0, old_value + delta))
            genome["ethics_genes"]["bias_threshold"] = new_value
            changes["bias_threshold"] = {"old": old_value, "new": new_value}

        # Мутация скорости мутации (мета-мутация)
        if random.random() < rate * 0.5:
            old_value = genome["meta_genes"]["mutation_rate"]
            delta = random.uniform(-0.005, 0.005)
            new_value = max(0.0, min(0.1, old_value + delta))
            genome["meta_genes"]["mutation_rate"] = new_value
            changes["mutation_rate"] = {"old": old_value, "new": new_value}

        return changes

    # ========================================================================
    # SELECTION (Отбор)
    # ========================================================================

    def select(
        self,
        candidates: List[Dict[str, Any]],
        fitness_scores: List[float],
        method: SelectionMethod = SelectionMethod.TOURNAMENT,
        num_selected: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Естественный отбор: оставляем только лучших

        Args:
            candidates: Список геномов-кандидатов
            fitness_scores: Список оценок фитнеса для каждого кандидата
            method: Метод отбора
            num_selected: Количество отбираемых особей

        Returns:
            List[Dict[str, Any]]: Отобранные геномы
        """
        if len(candidates) != len(fitness_scores):
            raise ValueError("Length of candidates and fitness_scores must match")

        num_selected = num_selected or self.population_size
        num_selected = min(num_selected, len(candidates))

        if method == SelectionMethod.ELITISM:
            return self._elitism_selection(candidates, fitness_scores, num_selected)
        elif method == SelectionMethod.TOURNAMENT:
            return self._tournament_selection(candidates, fitness_scores, num_selected)
        elif method == SelectionMethod.ROULETTE:
            return self._roulette_selection(candidates, fitness_scores, num_selected)
        elif method == SelectionMethod.RANK_BASED:
            return self._rank_based_selection(candidates, fitness_scores, num_selected)
        else:
            return candidates[:num_selected]

    def _elitism_selection(
        self,
        candidates: List[Dict[str, Any]],
        fitness_scores: List[float],
        num_selected: int
    ) -> List[Dict[str, Any]]:
        """Отбор через элитизм — сохраняем лучших"""
        indexed = list(enumerate(fitness_scores))
        indexed.sort(key=lambda x: x[1], reverse=True)
        selected_indices = [idx for idx, _ in indexed[:num_selected]]
        return [candidates[i] for i in selected_indices]

    def _tournament_selection(
        self,
        candidates: List[Dict[str, Any]],
        fitness_scores: List[float],
        num_selected: int,
        tournament_size: int = 3
    ) -> List[Dict[str, Any]]:
        """Турнирный отбор"""
        selected = []
        for _ in range(num_selected):
            tournament_indices = random.sample(range(len(candidates)), min(tournament_size, len(candidates)))
            winner_idx = max(tournament_indices, key=lambda i: fitness_scores[i])
            selected.append(copy.deepcopy(candidates[winner_idx]))
        return selected

    def _roulette_selection(
        self,
        candidates: List[Dict[str, Any]],
        fitness_scores: List[float],
        num_selected: int
    ) -> List[Dict[str, Any]]:
        """Рулеточный отбор"""
        total_fitness = sum(fitness_scores)
        if total_fitness == 0:
            return random.sample(candidates, min(num_selected, len(candidates)))
        
        probabilities = [f / total_fitness for f in fitness_scores]
        selected_indices = random.choices(range(len(candidates)), weights=probabilities, k=num_selected)
        return [copy.deepcopy(candidates[i]) for i in selected_indices]

    def _rank_based_selection(
        self,
        candidates: List[Dict[str, Any]],
        fitness_scores: List[float],
        num_selected: int
    ) -> List[Dict[str, Any]]:
        """Отбор на основе рангов"""
        indexed = list(enumerate(fitness_scores))
        indexed.sort(key=lambda x: x[1], reverse=True)
        ranks = [0] * len(indexed)
        for rank, (idx, _) in enumerate(indexed):
            ranks[idx] = len(indexed) - rank
        
        selected_indices = random.choices(range(len(candidates)), weights=ranks, k=num_selected)
        return [copy.deepcopy(candidates[i]) for i in selected_indices]

    # ========================================================================
    # FULL EVOLUTION CYCLE (Полный цикл эволюции)
    # ========================================================================

    def run_evolution(
        self,
        initial_population: List[Dict[str, Any]],
        fitness_function: Callable[[Dict[str, Any]], float],
        generations: Optional[int] = None,
        verbose: bool = False
    ) -> Dict[str, Any]:
        """
        Запускает полный цикл эволюции популяции

        Args:
            initial_population: Начальная популяция геномов
            fitness_function: Функция оценки фитнеса
            generations: Число поколений (переопределяет max_generations)
            verbose: Выводить ли прогресс

        Returns:
            Dict[str, Any]: Результаты эволюции
        """
        generations = generations or self.max_generations
        self.population = [copy.deepcopy(g) for g in initial_population]
        self.fitness_scores = [fitness_function(g) for g in self.population]
        
        self.best_fitness = max(self.fitness_scores)
        self.best_genome = copy.deepcopy(self.population[self.fitness_scores.index(self.best_fitness)])
        
        history = {
            "best_fitness_per_generation": [self.best_fitness],
            "avg_fitness_per_generation": [sum(self.fitness_scores) / len(self.fitness_scores)]
        }

        for gen in range(generations):
            self.generation = gen + 1
            
            # Отбор
            selected = self.select(
                self.population,
                self.fitness_scores,
                method=SelectionMethod.ELITISM,
                num_selected=self.elitism_count
            )
            
            # Скрещивание и мутация для заполнения популяции
            while len(selected) < self.population_size:
                parent_A = random.choice(self.population)
                parent_B = random.choice(self.population)
                
                result = self.breed(parent_A, parent_B, BreedingStrategy.BEST_OF_BOTH)
                if result.success:
                    mutant_result = self.mutate(result.child_genome)
                    if mutant_result.success:
                        selected.append(mutant_result.child_genome)
            
            self.population = selected[:self.population_size]
            self.fitness_scores = [fitness_function(g) for g in self.population]
            
            # Обновление лучшего
            current_best = max(self.fitness_scores)
            if current_best > self.best_fitness:
                self.best_fitness = current_best
                self.best_genome = copy.deepcopy(self.population[self.fitness_scores.index(current_best)])
            
            history["best_fitness_per_generation"].append(self.best_fitness)
            history["avg_fitness_per_generation"].append(sum(self.fitness_scores) / len(self.fitness_scores))
            
            if verbose:
                print(f"Generation {gen + 1}/{generations}: Best={self.best_fitness:.3f}, Avg={sum(self.fitness_scores)/len(self.fitness_scores):.3f}")

        return {
            "success": True,
            "best_genome": self.best_genome,
            "best_fitness": self.best_fitness,
            "generations_completed": self.generation,
            "total_events": len(self.ledger),
            "history": history,
            "author": self.author,
            "methodology": self.methodology
        }

    def get_ledger(self) -> List[Dict[str, Any]]:
        """Возвращает журнал всех событий эволюции (Genome Ledger™)"""
        return [event.to_dict() for event in self.ledger]

    def reset(self) -> None:
        """Сбрасывает состояние песочницы"""
        self.generation = 0
        self.population = []
        self.fitness_scores = []
        self.ledger = []
        self.best_genome = None
        self.best_fitness = 0.0


# ============================================================================
# Пример использования
# ============================================================================

if __name__ == "__main__":
    # Пример генома агента
    base_genome = {
        "meta": {"id": "base-agent-v1", "version": "0.1", "author": "Dm.Andreyanov", "created": "2026"},
        "cognitive_genes": {
            "reasoning_depth": "high",
            "creativity_coefficient": 0.6,
            "risk_tolerance": "medium",
            "learning_rate": 0.3
        },
        "ethics_genes": {
            "bias_threshold": 0.15,
            "transparency_level": "high",
            "hard_constraints": ["no_deception", "gdpr_compliant"]
        },
        "social_genes": {
            "communication_style": "assertive",
            "conflict_resolution": "collaborate",
            "handoff_protocol": "AWENATING"
        },
        "meta_genes": {
            "mutation_rate": 0.02,
            "selection_pressure": "performance",
            "generation_limit": 50
        }
    }

    # Инициализация песочницы
    sandbox = EvolutionarySandbox(mutation_rate=0.02, random_seed=42)

    # Пример 1: Скрещивание
    parent_A = copy.deepcopy(base_genome)
    parent_A["meta"]["id"] = "parent-A"
    parent_A["cognitive_genes"]["creativity_coefficient"] = 0.8

    parent_B = copy.deepcopy(base_genome)
    parent_B["meta"]["id"] = "parent-B"
    parent_B["cognitive_genes"]["creativity_coefficient"] = 0.4

    breed_result = sandbox.breed(parent_A, parent_B, BreedingStrategy.BEST_OF_BOTH)
    print("=== Breeding Result ===")
    print(f"Success: {breed_result.success}")
    if breed_result.success:
        print(f"Child ID: {breed_result.child_genome['meta']['id']}")
        print(f"Creativity: {breed_result.child_genome['cognitive_genes']['creativity_coefficient']}")

    # Пример 2: Мутация
    mutate_result = sandbox.mutate(breed_result.child_genome, rate=0.05)
    print("\n=== Mutation Result ===")
    print(f"Success: {mutate_result.success}")
    print(f"Changes: {mutate_result.metrics['changes_count']}")

    # Пример 3: Журнал событий
    print("\n=== Genome Ledger™ ===")
    for event in sandbox.get_ledger():
        print(f"  {event['event_type']}: {event['child_id']}")

    print(f"\nАвтор: {sandbox.author}")
    print(f"Методология: {sandbox.methodology}")
