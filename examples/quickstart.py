"""
Agent Genome Mapping™ — Quick Start Guide
Практический пример использования всех 5 модулей AGM

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Методология: Agent Genome Mapping™ (AGM)
"""

import sys
import os

# Добавляем путь к пакету
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from agm.genome_schema import (
    AgentGenome, CognitiveGenes, EthicsGenes, SocialGenes, MetaGenes,
    ReasoningDepth, RiskTolerance, TransparencyLevel, CommunicationStyle,
    ConflictResolution, HandoffProtocol, SelectionPressure
)
from agm.phenotype_engine import PhenotypeEngine
from agm.compatibility_matrix import CompatibilityMatrix
from agm.evolutionary_sandbox import EvolutionarySandbox, BreedingStrategy
from agm.drift_monitor import DriftMonitor


def print_header(title: str) -> None:
    """Вывод заголовка раздела"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_subheader(title: str) -> None:
    """Вывод подзаголовка"""
    print(f"\n▶ {title}")
    print("-" * 50)


# ============================================================================
# ПРИМЕР 1: Создание генома агента (Genome Schema™)
# ============================================================================

def example_1_genome_schema():
    """Пример 1: Создание и валидация генома агента"""
    print_header("ПРИМЕР 1: Genome Schema™ — Создание генома агента")

    # Создание генома для агента Neuro-Closer (продажа)
    neuro_closer = AgentGenome(
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

    # Валидация генома
    validation = neuro_closer.validate()
    print_subheader("Валидация генома")
    print(f"  ✓ Валиден: {validation['is_valid']}")
    print(f"  ✓ Автор: {validation['author']}")
    print(f"  ✓ Методология: {validation['methodology']}")

    # Экспорт в YAML
    print_subheader("YAML-экспорт (фрагмент)")
    yaml_output = neuro_closer.to_yaml()
    lines = yaml_output.split('\n')[:10]
    for line in lines:
        print(f"  {line}")
    print("  ...")

    # Экспорт в словарь (для использования в других модулях)
    genome_dict = neuro_closer.to_dict()
    print_subheader("Готов к использованию в других модулях")
    print(f"  ✓ ID: {genome_dict['meta']['id']}")
    print(f"  ✓ Когнитивные гены: {len(genome_dict['cognitive_genes'])} параметров")
    print(f"  ✓ Этические гены: {len(genome_dict['ethics_genes']['hard_constraints'])} ограничений")

    return genome_dict


# ============================================================================
# ПРИМЕР 2: Прогноз эффективности (Phenotype Engine™)
# ============================================================================

def example_2_phenotype_engine(genome: dict):
    """Пример 2: Прогноз поведения агента в контексте"""
    print_header("ПРИМЕР 2: Phenotype Engine™ — Прогноз эффективности")

    engine = PhenotypeEngine()

    # Прогноз для домена продаж
    print_subheader("Контекст: Продажи (sales)")
    context_sales = {
        "domain": "sales",
        "preferred_styles": ["assertive", "empathetic"],
        "safety_critical": False,
        "regulated_domain": False
    }
    prediction_sales = engine.predict(genome, context_sales)
    print(f"  ✓ Эффективность: {prediction_sales.predicted_effectiveness}")
    print(f"  ✓ Рекомендация: {prediction_sales.recommendation.value}")
    print(f"  ✓ Уверенность: {prediction_sales.confidence_score}")
    print(f"  ✓ Риски: {prediction_sales.risk_flags if prediction_sales.risk_flags else 'Нет'}")

    # Детализация по компонентам
    print_subheader("Детализация эффективности")
    for component, score in prediction_sales.breakdown.items():
        bar = "█" * int(score / 10)
        print(f"  {component:20s}: {score:5.1f}% {bar}")

    # Прогноз для домена поддержки
    print_subheader("Контекст: Поддержка клиентов (support)")
    context_support = {
        "domain": "support",
        "preferred_styles": ["empathetic", "casual"],
        "safety_critical": False,
        "regulated_domain": False
    }
    prediction_support = engine.predict(genome, context_support)
    print(f"  ✓ Эффективность: {prediction_support.predicted_effectiveness}")
    print(f"  ✓ Рекомендация: {prediction_support.recommendation.value}")

    return prediction_sales, prediction_support


# ============================================================================
# ПРИМЕР 3: Оценка совместимости (Compatibility Matrix™)
# ============================================================================

def example_3_compatibility_matrix(genome_A: dict):
    """Пример 3: Оценка совместимости двух агентов"""
    print_header("ПРИМЕР 3: Compatibility Matrix™ — Совместимость агентов")

    # Создание второго агента (Profiler Service)
    genome_B = {
        "meta": {"id": "profiler-v1", "version": "0.1", "author": "Dm.Andreyanov", "created": "2026"},
        "cognitive_genes": {
            "reasoning_depth": "medium",
            "creativity_coefficient": 0.5,
            "risk_tolerance": "low",
            "learning_rate": 0.4
        },
        "ethics_genes": {
            "bias_threshold": 0.05,
            "transparency_level": "high",
            "hard_constraints": ["no_deception", "gdpr_compliant", "data_minimization"]
        },
        "social_genes": {
            "communication_style": "formal",
            "conflict_resolution": "collaborate",
            "handoff_protocol": "AWENATING"
        },
        "meta_genes": {
            "mutation_rate": 0.01,
            "selection_pressure": "ethics",
            "generation_limit": 30
        }
    }

    matrix = CompatibilityMatrix()
    result = matrix.evaluate(genome_A, genome_B)

    print_subheader("Результаты оценки совместимости")
    print(f"  ✓ Совместимость: {result.compatibility_score} ({result.compatibility_level.value})")
    print(f"  ✓ Рекомендация: {result.recommendation.value}")

    print_subheader("Компоненты совместимости")
    print(f"  ✓ Когнитивный синергизм: {result.cognitive_synergy}")
    print(f"  ✓ Этическое выравнивание: {result.ethics_alignment}")
    print(f"  ✓ Социальная гармония: {result.social_harmony}")

    print_subheader("Риски конфликтов")
    if result.conflict_risks:
        for risk in result.conflict_risks:
            print(f"  ⚠️ {risk}")
    else:
        print("  ✓ Риски не обнаружены")

    print_subheader("Возможности синергии")
    if result.synergy_opportunities:
        for opp in result.synergy_opportunities:
            print(f"  ✨ {opp}")
    else:
        print("  — Возможности не выявлены")

    return result


# ============================================================================
# ПРИМЕР 4: Эволюция агентов (Evolutionary Sandbox™)
# ============================================================================

def example_4_evolutionary_sandbox(genome_A: dict, genome_B: dict):
    """Пример 4: Скрещивание и эволюция агентов"""
    print_header("ПРИМЕР 4: Evolutionary Sandbox™ — Эволюция агентов")

    sandbox = EvolutionarySandbox(mutation_rate=0.02, random_seed=42)

    # Скрещивание двух агентов
    print_subheader("Скрещивание (Breeding)")
    breed_result = sandbox.breed(genome_A, genome_B, BreedingStrategy.BEST_OF_BOTH)
    if breed_result.success:
        child = breed_result.child_genome
        print(f"  ✓ Потомок: {child['meta']['id']}")
        print(f"  ✓ Родители: {child['meta']['parents']}")
        print(f"  ✓ Креативность: {child['cognitive_genes']['creativity_coefficient']}")
        print(f"  ✓ Порог bias: {child['ethics_genes']['bias_threshold']}")

    # Мутация потомка
    print_subheader("Мутация (Mutation)")
    mutate_result = sandbox.mutate(child, rate=0.05)
    if mutate_result.success:
        mutated = mutate_result.child_genome
        print(f"  ✓ Мутировавший: {mutated['meta']['id']}")
        print(f"  ✓ Изменений: {mutate_result.metrics['changes_count']}")

    # Журнал событий (Genome Ledger™)
    print_subheader("Журнал эволюционных событий")
    ledger = sandbox.get_ledger()
    for event in ledger:
        print(f"  📝 {event['event_type']}: {event['child_id']}")

    return sandbox, child


# ============================================================================
# ПРИМЕР 5: Мониторинг дрейфа (Drift Monitor™)
# ============================================================================

def example_5_drift_monitor(baseline_genome: dict):
    """Пример 5: Отслеживание дрейфа и аудит"""
    print_header("ПРИМЕР 5: Drift Monitor™ — Мониторинг дрейфа")

    monitor = DriftMonitor(baseline_genome)

    # Проверка 1: Стабильное состояние
    print_subheader("Проверка 1: Стабильное состояние")
    report_1 = monitor.check_drift(baseline_genome)
    print(f"  ✓ Статус: {report_1.status}")
    print(f"  ✓ Общий дрейф: {report_1.overall_drift_score}")
    print(f"  ✓ Предупреждения: {len(report_1.alerts)}")

    # Проверка 2: Изменённый геном (дрейф)
    print_subheader("Проверка 2: Обнаружен дрейф")
    drifted_genome = baseline_genome.copy()
    drifted_genome["cognitive_genes"]["creativity_coefficient"] = 0.9
    drifted_genome["ethics_genes"]["bias_threshold"] = 0.25
    drifted_genome["meta"]["version"] = "0.2"

    report_2 = monitor.check_drift(drifted_genome)
    print(f"  ✓ Статус: {report_2.status}")
    print(f"  ✓ Общий дрейф: {report_2.overall_drift_score}")
    print(f"  ✓ Предупреждения: {len(report_2.alerts)}")

    if report_2.alerts:
        print_subheader("Предупреждения")
        for alert in report_2.alerts:
            print(f"  ⚠️ [{alert.severity.value}] {alert.alert_type.value}: {alert.description}")

    # Сводка по Genome Ledger™
    print_subheader("Genome Ledger™ — Сводка аудита")
    summary = monitor.get_ledger_summary()
    print(f"  ✓ Всего записей: {summary['total_entries']}")
    print(f"  ✓ Целостность цепочки: {summary['chain_valid']}")
    print(f"  ✓ Последний хеш: {summary['latest_hash'][:32]}...")

    # Верификация целостности
    print_subheader("Верификация целостности журнала")
    integrity = monitor.verify_ledger_integrity()
    print(f"  ✓ Валиден: {integrity['valid']}")
    print(f"  ✓ Проверено записей: {integrity['entries_checked']}")

    return monitor


# ============================================================================
# ГЛАВНЫЙ ЗАПУСК
# ============================================================================

def main():
    """Запуск всех примеров"""
    print("\n" + "█" * 70)
    print("█" + " " * 68 + "█")
    print("█" + "  AGENT GENOME MAPPING™ — QUICK START GUIDE".center(68) + "█")
    print("█" + "  Автор: Dm.Andreyanov | Prizolov Market & Lab".center(68) + "█")
    print("█" + " " * 68 + "█")
    print("█" * 70)

    # Пример 1: Создание генома
    genome = example_1_genome_schema()

    # Пример 2: Прогноз эффективности
    example_2_phenotype_engine(genome)

    # Пример 3: Оценка совместимости
    example_3_compatibility_matrix(genome)

    # Пример 4: Эволюция агентов
    sandbox, child_genome = example_4_evolutionary_sandbox(genome, genome)

    # Пример 5: Мониторинг дрейфа
    example_5_drift_monitor(genome)

    # Финальный итог
    print_header("ИТОГ: Все 5 модулей AGM работают корректно")
    print("""
  ✅ Genome Schema™      — Создание и валидация генома
  ✅ Phenotype Engine™   — Прогноз эффективности
  ✅ Compatibility Matrix™ — Оценка совместимости
  ✅ Evolutionary Sandbox™ — Эволюция агентов
  ✅ Drift Monitor™      — Мониторинг и аудит

  📚 Документация: github.com/GIBDD-DPS/agent-genome-mapping
  📧 Контакты: Dm.Andreyanov | Prizolov Market & Lab
  © 2026 Agent Genome Mapping™ is a trademark of Prizolov Lab.
    """)
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
