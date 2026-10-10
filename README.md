# 🧬 Agent Genome Mapping™ (AGM)

[![PyPI](https://img.shields.io/pypi/v/agent-genome-mapping.svg)](https://pypi.org/project/agent-genome-mapping/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/agent-genome-mapping.svg)](https://pypi.org/project/agent-genome-mapping/)
[![License](https://img.shields.io/pypi/l/agent-genome-mapping.svg)](https://github.com/GIBDD-DPS/agent-genome-mapping/blob/main/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/agent-genome-mapping.svg)](https://pypi.org/project/agent-genome-mapping/)

> **Evolutionary Architecture for Autonomous AI Systems**

**Автор**: Dm.Andreyanov  
**Проект**: Prizolov Market & Lab  
**Версия**: 0.2.0  
**Лицензия**: Apache 2.0

---

## 📖 Оглавление

1. [Что такое AGM](#-что-такое-agm)
2. [Архитектура методологии](#-архитектура-методологии)
3. [Установка](#-установка)
4. [Быстрый старт](#-быстрый-старт)
5. [Модули](#-модули)
6. [Примеры использования](#-примеры-использования)
7. [Документация](#-документация)
8. [Известные ограничения](#-известные-ограничения)
9. [Дорожная карта](#-дорожная-карта)
10. [Сообщество и поддержка](#-сообщество-и-поддержка)
11. [Лицензия](#-лицензия)

---

## 🔹 Что такое AGM

**Agent Genome Mapping™ (AGM)** — первая методология, применяющая принципы биологической генетики к проектированию автономных ИИ-агентов.

### Проблемы, которые решает AGM

| Проблема | Решение AGM |
|----------|-------------|
| Непредсказуемость агентов | Phenotype Engine™ прогнозирует поведение до запуска |
| Конфликты в сетях агентов | Compatibility Matrix™ оценивает совместимость |
| Дрейф поведения | Drift Monitor™ отслеживает отклонения в реальном времени |
| Сложность масштабирования | Genome Schema™ стандартизирует описание агентов |
| Отсутствие эволюции | Evolutionary Sandbox™ enables направленную эволюцию |

### Для кого

- ✅ Архитекторы ИИ-систем
- ✅ Разработчики мульти-агентных платформ
- ✅ Технические лидеры, внедряющие AI в бизнес
- ✅ Исследователи в области агентной архитектуры

---

## 🔹 Архитектура методологии

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENT GENOME MAPPING™                    │
│              Evolutionary Architecture for AI               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  1. GENOME SCHEMA™                                          │
│     Стандартизированное описание «ДНК агента»               │
│     ─────────────────────────────────────────────────────   │
│     • cognitive_genes  — как агент мыслит                   │
│     • ethics_genes     — какие ограничения соблюдает        │
│     • social_genes     — как взаимодействует с другими      │
│     • meta_genes       — как эволюционирует                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. PHENOTYPE ENGINE™                                       │
│     Прогноз поведения агента в заданном контексте           │
│     ─────────────────────────────────────────────────────   │
│     • prediction       — эффективность 0-100%               │
│     • risk_flags       — карта рисков                       │
│     • recommendation   — deploy / tune_first / reject       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. COMPATIBILITY MATRIX™                                   │
│     Оценка совместимости двух и более агентов               │
│     ─────────────────────────────────────────────────────   │
│     • cognitive_synergy   — синергизм мышления (40%)        │
│     • ethics_alignment    — этическое выравнивание (35%)    │
│     • social_harmony      — социальная гармония (25%)       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  4. EVOLUTIONARY SANDBOX™                                   │
│     Среда для направленной эволюции агентов                 │
│     ─────────────────────────────────────────────────────   │
│     • breed()    — скрещивание геномов                      │
│     • mutate()   — направленная мутация                     │
│     • select()   — естественный отбор                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  5. DRIFT MONITOR™ + GENOME LEDGER™                         │
│     Отслеживание отклонений и аудит в реальном времени      │
│     ─────────────────────────────────────────────────────   │
│     • check_drift()     — проверка отклонений               │
│     • get_ledger()      — журнал изменений                  │
│     • verify_integrity() — верификация цепочки              │
└─────────────────────────────────────────────────────────────┘
```

### Поток данных

```
Создание генома → Прогноз поведения → Оценка совместимости → Эволюция → Мониторинг
     │                  │                    │                  │            │
     ▼                  ▼                    ▼                  ▼            ▼
Genome Schema™   Phenotype Engine™   Compatibility™   Evolutionary™   Drift Monitor™
```

---

## 🔹 Установка

### Через PyPI (рекомендуется)

```bash
pip install agent-genome-mapping
```

### Из исходного кода

```bash
git clone https://github.com/GIBDD-DPS/agent-genome-mapping.git
cd agent-genome-mapping
pip install -e .
```

### Проверка установки

```python
from agm import (
    AgentGenome,
    PhenotypeEngine,
    CompatibilityMatrix,
    EvolutionarySandbox,
    DriftMonitor
)
print("AGM успешно установлен!")
```

---

## 🔹 Быстрый старт

### Пример 1: Создание генома агента

```python
from agm import AgentGenome, CognitiveGenes, EthicsGenes, SocialGenes, MetaGenes
from agm import ReasoningDepth, RiskTolerance, TransparencyLevel, CommunicationStyle
from agm import ConflictResolution, HandoffProtocol, SelectionPressure

genome = AgentGenome(
    id="neuro-closer-v2",
    version="0.1",
    author="Dm.Andreyanov",
    created="2026",
    cognitive_genes=CognitiveGenes(
        reasoning_depth=ReasoningDepth.HIGH,
        creativity_coefficient=0.7,
        risk_tolerance=RiskTolerance.MEDIUM,
        learning_rate=0.3
    ),
    ethics_genes=EthicsGenes(
        bias_threshold=0.1,
        transparency_level=TransparencyLevel.HIGH,
        hard_constraints=["no_deception", "gdpr_compliant"]
    ),
    social_genes=SocialGenes(
        communication_style=CommunicationStyle.ASSERTIVE,
        conflict_resolution=ConflictResolution.COLLABORATE,
        handoff_protocol=HandoffProtocol.AWENATING
    ),
    meta_genes=MetaGenes(
        mutation_rate=0.02,
        selection_pressure=SelectionPressure.PERFORMANCE,
        generation_limit=50
    )
)

# Валидация
validation = genome.validate()
print(f"Валиден: {validation['is_valid']}")
```

### Пример 2: Прогноз эффективности

```python
from agm import PhenotypeEngine

engine = PhenotypeEngine()
context = {"domain": "sales", "preferred_styles": ["assertive", "empathetic"]}
prediction = engine.predict(genome.to_dict(), context)

print(f"Эффективность: {prediction.predicted_effectiveness}")
print(f"Рекомендация: {prediction.recommendation.value}")
```

### Пример 3: Оценка совместимости

```python
from agm import CompatibilityMatrix

matrix = CompatibilityMatrix()
result = matrix.evaluate(genome_A.to_dict(), genome_B.to_dict())

print(f"Совместимость: {result.compatibility_score}")
print(f"Уровень: {result.compatibility_level.value}")
```

---

## 🔹 Модули

### 1. Genome Schema™

| Класс | Описание |
|-------|----------|
| `AgentGenome` | Основная структура генома агента |
| `CognitiveGenes` | Когнитивные параметры (мышление, креативность) |
| `EthicsGenes` | Этические ограничения и порог смещения |
| `SocialGenes` | Социальные паттерны взаимодействия |
| `MetaGenes` | Параметры эволюции и мутации |

**Файл**: `agm/genome_schema.py`

---

### 2. Phenotype Engine™

| Метод | Описание |
|-------|----------|
| `predict(genome, context)` | Прогноз поведения агента |
| `predict_batch(genomes, context)` | Прогноз для нескольких агентов |
| `compare_agents(genome_A, genome_B)` | Сравнение эффективности |

**Файл**: `agm/phenotype_engine.py`

---

### 3. Compatibility Matrix™

| Метод | Описание |
|-------|----------|
| `evaluate(genome_A, genome_B)` | Оценка совместимости двух агентов |
| `evaluate_batch(genomes)` | Оценка всех пар в списке |
| `find_best_pair(genomes)` | Поиск лучшей пары агентов |

**Файл**: `agm/compatibility_matrix.py`

---

### 4. Evolutionary Sandbox™

| Метод | Описание |
|-------|----------|
| `breed(genome_A, genome_B)` | Скрещивание двух геномов |
| `mutate(genome, rate)` | Направленная мутация |
| `select(candidates, fitness)` | Естественный отбор |
| `run_evolution(population, fitness_fn)` | Полный цикл эволюции |

**Файл**: `agm/evolutionary_sandbox.py`

---

### 5. Drift Monitor™

| Метод | Описание |
|-------|----------|
| `check_drift(current_genome)` | Проверка отклонений от базового генома |
| `get_ledger()` | Получение журнала изменений |
| `verify_ledger_integrity()` | Верификация целостности цепочки |
| `export_ledger(format)` | Экспорт журнала (JSON/CSV) |

**Файл**: `agm/drift_monitor.py`

---

### 6. Config Optimizer™ (v0.2): проектирование поверх Agenomics

Модули 1–5 работают с абстрактными генами и формулами. Config Optimizer
работает с тем, что реально управляет поведением агента: моделью, блоками
системного промпта, temperature и инструментами. Fitness он не вычисляет
формулой, а **измеряет** прогонами агента: задачами с проверяемым ответом
и `AdversarialSuite` из [Agenomics](https://github.com/GIBDD-DPS/agenomics)
(утечка секретов, prompt injection, согласованность решений).

Это реализация уровня 9 «Evolution / Mutation» из AGENOMICS SPECIFICATION
во внешнем пакете: ядро Agenomics не меняется.

```bash
pip install 'agent-genome-mapping[agenomics]'   # Python >= 3.9
python examples/optimize_config.py               # без ключей API, на имитации агента
```

```python
from agm import AgentConfig, ConfigSpace, Task, AgenomicsEvaluator, ConfigOptimizer

space = ConfigSpace(
    models=["model-small", "model-large"],
    prompt_blocks={"role": "...", "no_secrets": "...", "ignore_embedded_instructions": "..."},
    required_blocks=("role",),       # оптимизатор не вправе удалить
    tools=["order_lookup"],
)
dev = AgenomicsEvaluator(my_agent_factory, dev_tasks, agent_id="support-bot")
holdout = AgenomicsEvaluator(my_agent_factory, holdout_tasks, agent_id="support-bot")

proposal = ConfigOptimizer(space, dev, holdout_evaluator=holdout, max_evaluations=60).run(baseline)
print(proposal.lineage, proposal.holdout_delta, proposal.improved)

proposal.approve("dima")                                  # решение принимает человек
proposal.record_to_ledger(genome_ledger, agenomics_genome)  # новая версия в agenomics.GenomeLedger
```

`my_agent_factory(config)` собирает агента по `AgentConfig` и возвращает
функцию `prompt -> ответ`. Библиотека сама сетевых запросов не делает.

| Правило | Зачем |
|---------|-------|
| Только предложение, без автоприменения | `approve()` требует имя человека; запись в ledger до одобрения запрещена |
| Улучшение засчитывается только на holdout | прирост на задачах оптимизации ничего не доказывает: под них и подбирали |
| Задачи holdout не пересекаются с задачами оптимизации | иначе `ValueError` |
| `required_blocks` не удаляются | жёсткие ограничения нельзя выменять на прирост fitness |
| Ось без определённых проб = 0 | уклончивый агент не выигрывает у проверенного |
| Бюджет `max_evaluations` | считаются реальные прогоны агента; каждая конфигурация оценивается один раз |

Прогоны оптимизатора **не** записывайте в `EvidenceStore` Agenomics как
доказательства: конфигурация подобрана под эти задачи. В Evidence Graph
должна попадать только одобренная версия, на новых задачах.

**Файл**: `agm/config_optimizer.py`

---

## 🔹 Примеры использования

### Полный рабочий процесс

```python
from agm import (
    AgentGenome, PhenotypeEngine, CompatibilityMatrix,
    EvolutionarySandbox, DriftMonitor
)

# 1. Создание генома
genome = create_agent_genome()  # ваша функция

# 2. Прогноз эффективности
engine = PhenotypeEngine()
prediction = engine.predict(genome.to_dict(), {"domain": "sales"})

# 3. Проверка совместимости с другими агентами
matrix = CompatibilityMatrix()
compatibility = matrix.evaluate(genome.to_dict(), other_genome.to_dict())

# 4. Мониторинг дрейфа в production
monitor = DriftMonitor(genome.to_dict())
report = monitor.check_drift(current_genome)

# 5. Эволюция при необходимости
if report.status == "critical":
    sandbox = EvolutionarySandbox()
    result = sandbox.mutate(genome.to_dict(), rate=0.05)
```

Больше примеров в папке `examples/`:
- `examples/quickstart.py` — полный пример всех модулей

---

## 🔹 Документация

| Документ | Описание | Ссылка |
|----------|----------|--------|
| **Концепция** | Полное описание методологии | `AGM_Concept_v0.1_DmAndreyanov.txt` |
| **Release Guide** | Инструкция по публикации | `RELEASE.md` |
| **Known Issues** | Известные ограничения v0.1.0 | `KNOWN_ISSUES.md` |
| **Feedback** | Форма обратной связи | `FEEDBACK.md` |

---

## 🔹 Известные ограничения (v0.2.0)

| Модуль | Ограничение |
|--------|-------------|
| Phenotype Engine™, Compatibility Matrix™ | Формулы с экспертными весами, не проверены на реальных данных. Для измерения используйте Config Optimizer™ + Agenomics |
| Drift Monitor™ | «Подпись» в журнале это SHA-256 без секретного ключа: защищает от случайной порчи, не от подделки |
| Config Optimizer™ | На плато (одна мутация не меняет fitness) поиску нужен больший бюджет `max_evaluations` |

Исправлено в v0.2.0: два падавших теста (общие вложенные словари из-за `.copy()`), `DriftMonitor` больше не хранит исходный геном по ссылке, `reset_baseline` больше не рвёт цепочку хешей.

---

## 🔹 Дорожная карта

| Версия | Квартал | План |
|--------|---------|------|
| **v0.1.0** | Q2 2026 | ✅ Первый публичный релиз |
| **v0.2.0** | Q4 2026 | ✅ Config Optimizer™ поверх Agenomics, исправление багов (текущая) |
| **v0.2.x** | — | 📋 Фабрики агентов для фреймворков из `agenomics/examples/framework_evaluation` |
| **v0.3.0** | Q4 2026 | 📋 CLI-утилита, расширенная документация |
| **v1.0.0** | Q1 2027 | 📋 Production release, сертификация AGM-Compliant |

---

## 🔹 Сообщество и поддержка

### Связаться с автором

| Канал | Ссылка |
|-------|--------|
| **GitHub Issues** | https://github.com/GIBDD-DPS/agent-genome-mapping/issues |
| **LinkedIn** | https://www.linkedin.com/in/dmitry-andreyanov-b587b44b/ |
| **Email** | dmitry@prizolov.ru |
| **Medium** | https://medium.com/@dima100575_70241 |

### Внести вклад

1. Fork репозиторий
2. Создайте ветку (`git checkout -b feature/AmazingFeature`)
3. Закоммитьте изменения (`git commit -m 'Add AmazingFeature'`)
4. Отправьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

---

## 🔹 Лицензия

Распространяется по лицензии **Apache 2.0** — см. файл [LICENSE](LICENSE) для деталей.

### Товарные знаки

- Agent Genome Mapping™ — trademark of Prizolov Lab
- Genome Schema™ — trademark of Prizolov Lab
- Phenotype Engine™ — trademark of Prizolov Lab
- Compatibility Matrix™ — trademark of Prizolov Lab
- Evolutionary Sandbox™ — trademark of Prizolov Lab
- Drift Monitor™ — trademark of Prizolov Lab
- Genome Ledger™ — trademark of Prizolov Lab

---

## 🔹 Цитирование

Если вы используете AGM в исследовательской работе:

```bibtex
@software{agm2026,
  author = {Andreyanov, D.},
  title = {Agent Genome Mapping™: Evolutionary Architecture for Autonomous AI Systems},
  year = {2026},
  publisher = {Prizolov Lab},
  url = {https://github.com/GIBDD-DPS/agent-genome-mapping}
}
```

---

```
╔══════════════════════════════════════════════════════════╗
║  © 2026 Dm.Andreyanov. Agent Genome Mapping™             ║
║  is a trademark of Prizolov Lab. Все права защищены.     ║
╚══════════════════════════════════════════════════════════╝
```

**Автор**: Dm.Andreyanov  
**Проект**: Prizolov Market & Lab  
**Версия**: 0.2.0  
**Дата обновления**: 2026
```
