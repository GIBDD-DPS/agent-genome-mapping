"""
Unit-тесты для Agent Genome Mapping™ (AGM)
Тестирование всех 5 модулей методологии

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Методология: Agent Genome Mapping™ (AGM)
"""

import unittest
import sys
import os

# Добавляем путь к пакету
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from agm.genome_schema import (
    AgentGenome, CognitiveGenes, EthicsGenes, SocialGenes, MetaGenes,
    ReasoningDepth, RiskTolerance, TransparencyLevel, CommunicationStyle,
    ConflictResolution, HandoffProtocol, SelectionPressure
)
from agm.phenotype_engine import PhenotypeEngine, Recommendation
from agm.compatibility_matrix import CompatibilityMatrix, CompatibilityLevel
from agm.evolutionary_sandbox import EvolutionarySandbox, BreedingStrategy
from agm.drift_monitor import DriftMonitor, DriftSeverity


class TestGenomeSchema(unittest.TestCase):
    """Тесты для модуля Genome Schema™"""

    def setUp(self):
        """Создание тестового генома"""
        self.genome = AgentGenome(
            id="test-agent-v1",
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

    def test_genome_creation(self):
        """Тест создания генома"""
        self.assertEqual(self.genome.id, "test-agent-v1")
        self.assertEqual(self.genome.author, "Dm.Andreyanov")
        self.assertEqual(self.genome.cognitive_genes.creativity_coefficient, 0.7)

    def test_genome_validation_valid(self):
        """Тест валидации корректного генома"""
        result = self.genome.validate()
        self.assertTrue(result["is_valid"])
        self.assertEqual(result["author"], "Dm.Andreyanov")
        self.assertEqual(result["methodology"], "Agent Genome Mapping™")

    def test_genome_validation_invalid_creativity(self):
        """Тест валидации с некорректной креативностью"""
        self.genome.cognitive_genes.creativity_coefficient = 1.5
        result = self.genome.validate()
        self.assertFalse(result["is_valid"])
        self.assertIn("creativity_coefficient must be between 0.0 and 1.0", 
                      result["errors"]["cognitive_genes"])

    def test_genome_to_yaml(self):
        """Тест экспорта в YAML"""
        yaml_output = self.genome.to_yaml()
        self.assertIn("agent_genome", yaml_output)
        self.assertIn("test-agent-v1", yaml_output)
        self.assertIn("Dm.Andreyanov", yaml_output)

    def test_genome_to_dict(self):
        """Тест экспорта в словарь"""
        dict_output = self.genome.to_dict()
        self.assertEqual(dict_output["meta"]["id"], "test-agent-v1")
        self.assertEqual(dict_output["cognitive_genes"]["creativity_coefficient"], 0.7)


class TestPhenotypeEngine(unittest.TestCase):
    """Тесты для модуля Phenotype Engine™"""

    def setUp(self):
        """Создание тестового генома и двигателя"""
        self.genome = {
            "meta": {"id": "test-agent-v1", "author": "Dm.Andreyanov"},
            "cognitive_genes": {
                "reasoning_depth": "high",
                "creativity_coefficient": 0.7,
                "risk_tolerance": "medium",
                "learning_rate": 0.3
            },
            "ethics_genes": {
                "bias_threshold": 0.1,
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
        self.engine = PhenotypeEngine()

    def test_prediction_basic(self):
        """Тест базового прогноза"""
        prediction = self.engine.predict(self.genome)
        self.assertGreater(prediction.predicted_effectiveness, 0)
        self.assertLessEqual(prediction.predicted_effectiveness, 100)
        self.assertEqual(prediction.author, "Dm.Andreyanov")

    def test_prediction_with_context(self):
        """Тест прогноза с контекстом"""
        context = {"domain": "sales", "preferred_styles": ["assertive"]}
        prediction = self.engine.predict(self.genome, context)
        self.assertIsInstance(prediction.breakdown, dict)
        self.assertIn("reasoning", prediction.breakdown)

    def test_prediction_risk_detection(self):
        """Тест обнаружения рисков"""
        risky_genome = self.genome.copy()
        risky_genome["ethics_genes"]["bias_threshold"] = 0.5
        prediction = self.engine.predict(risky_genome)
        self.assertIn("potential_bias_detected", prediction.risk_flags)

    def test_compare_agents(self):
        """Тест сравнения двух агентов"""
        genome_B = self.genome.copy()
        genome_B["meta"]["id"] = "test-agent-v2"
        genome_B["cognitive_genes"]["creativity_coefficient"] = 0.3
        
        comparison = self.engine.compare_agents(self.genome, genome_B)
        self.assertIn("winner", comparison)
        self.assertEqual(comparison["author"], "Dm.Andreyanov")


class TestCompatibilityMatrix(unittest.TestCase):
    """Тесты для модуля Compatibility Matrix™"""

    def setUp(self):
        """Создание тестовых геномов"""
        self.genome_A = {
            "meta": {"id": "agent-A", "author": "Dm.Andreyanov"},
            "cognitive_genes": {
                "reasoning_depth": "high",
                "creativity_coefficient": 0.7,
                "risk_tolerance": "medium",
                "learning_rate": 0.3
            },
            "ethics_genes": {
                "bias_threshold": 0.1,
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
        self.genome_B = self.genome_A.copy()
        self.genome_B["meta"]["id"] = "agent-B"
        self.matrix = CompatibilityMatrix()

    def test_compatibility_identical(self):
        """Тест совместимости идентичных агентов"""
        result = self.matrix.evaluate(self.genome_A, self.genome_A)
        self.assertGreaterEqual(result.compatibility_score, 0.8)
        self.assertEqual(result.compatibility_level, CompatibilityLevel.EXCELLENT)

    def test_compatibility_different(self):
        """Тест совместимости разных агентов"""
        self.genome_B["social_genes"]["communication_style"] = "formal"
        result = self.matrix.evaluate(self.genome_A, self.genome_B)
        self.assertGreater(result.compatibility_score, 0)
        self.assertLessEqual(result.compatibility_score, 1)

    def test_conflict_risk_detection(self):
        """Тест обнаружения конфликтов"""
        self.genome_B["ethics_genes"]["hard_constraints"] = ["ignore_privacy"]
        result = self.matrix.evaluate(self.genome_A, self.genome_B)
        self.assertGreater(len(result.conflict_risks), 0)

    def test_synergy_opportunities(self):
        """Тест обнаружения синергии"""
        result = self.matrix.evaluate(self.genome_A, self.genome_B)
        self.assertIsInstance(result.synergy_opportunities, list)


class TestEvolutionarySandbox(unittest.TestCase):
    """Тесты для модуля Evolutionary Sandbox™"""

    def setUp(self):
        """Создание тестового генома и песочницы"""
        self.genome = {
            "meta": {"id": "base-agent", "author": "Dm.Andreyanov"},
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
        self.sandbox = EvolutionarySandbox(random_seed=42)

    def test_breeding(self):
        """Тест скрещивания"""
        parent_A = self.genome.copy()
        parent_A["meta"]["id"] = "parent-A"
        parent_B = self.genome.copy()
        parent_B["meta"]["id"] = "parent-B"
        
        result = self.sandbox.breed(parent_A, parent_B)
        self.assertTrue(result.success)
        self.assertIsNotNone(result.child_genome)
        self.assertIn("hybrid", result.child_genome["meta"]["id"])

    def test_mutation(self):
        """Тест мутации"""
        result = self.sandbox.mutate(self.genome, rate=0.1)
        self.assertTrue(result.success)
        self.assertIn("mutated", result.child_genome["meta"]["id"])

    def test_ledger_logging(self):
        """Тест журналирования событий"""
        parent_A = self.genome.copy()
        parent_A["meta"]["id"] = "parent-A"
        parent_B = self.genome.copy()
        parent_B["meta"]["id"] = "parent-B"
        
        self.sandbox.breed(parent_A, parent_B)
        ledger = self.sandbox.get_ledger()
        self.assertGreater(len(ledger), 0)
        self.assertEqual(ledger[0]["event_type"], "breed")


class TestDriftMonitor(unittest.TestCase):
    """Тесты для модуля Drift Monitor™"""

    def setUp(self):
        """Создание базового генома и монитора"""
        self.baseline = {
            "meta": {"id": "monitored-agent", "author": "Dm.Andreyanov"},
            "cognitive_genes": {
                "reasoning_depth": "high",
                "creativity_coefficient": 0.7,
                "risk_tolerance": "medium",
                "learning_rate": 0.3
            },
            "ethics_genes": {
                "bias_threshold": 0.1,
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
        self.monitor = DriftMonitor(self.baseline)

    def test_drift_check_stable(self):
        """Тест проверки без дрейфа"""
        report = self.monitor.check_drift(self.baseline)
        self.assertEqual(report.status, "stable")
        self.assertEqual(report.drift_severity, DriftSeverity.NONE)

    def test_drift_check_changed(self):
        """Тест проверки с изменениями"""
        drifted = self.baseline.copy()
        drifted["cognitive_genes"]["creativity_coefficient"] = 0.9
        drifted["ethics_genes"]["bias_threshold"] = 0.3
        
        report = self.monitor.check_drift(drifted)
        self.assertGreater(report.overall_drift_score, 0)
        self.assertGreater(len(report.alerts), 0)

    def test_ledger_integrity(self):
        """Тест целостности журнала"""
        self.monitor.check_drift(self.baseline)
        integrity = self.monitor.verify_ledger_integrity()
        self.assertTrue(integrity["valid"])

    def test_ledger_summary(self):
        """Тест сводки журнала"""
        self.monitor.check_drift(self.baseline)
        summary = self.monitor.get_ledger_summary()
        self.assertGreater(summary["total_entries"], 0)
        self.assertTrue(summary["chain_valid"])


class TestAGMIntegration(unittest.TestCase):
    """Интеграционные тесты для всей системы AGM"""

    def test_full_workflow(self):
        """Тест полного рабочего процесса"""
        # 1. Создание генома
        genome = {
            "meta": {"id": "workflow-agent", "author": "Dm.Andreyanov"},
            "cognitive_genes": {
                "reasoning_depth": "high",
                "creativity_coefficient": 0.7,
                "risk_tolerance": "medium",
                "learning_rate": 0.3
            },
            "ethics_genes": {
                "bias_threshold": 0.1,
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

        # 2. Прогноз эффективности
        engine = PhenotypeEngine()
        prediction = engine.predict(genome)
        self.assertGreater(prediction.predicted_effectiveness, 50)

        # 3. Проверка совместимости с самим собой
        matrix = CompatibilityMatrix()
        compatibility = matrix.evaluate(genome, genome)
        self.assertGreater(compatibility.compatibility_score, 0.8)

        # 4. Мониторинг дрейфа
        monitor = DriftMonitor(genome)
        report = monitor.check_drift(genome)
        self.assertEqual(report.status, "stable")

        # 5. Проверка авторства во всех модулях
        self.assertEqual(prediction.author, "Dm.Andreyanov")
        self.assertEqual(compatibility.author, "Dm.Andreyanov")
        self.assertEqual(report.author, "Dm.Andreyanov")


if __name__ == "__main__":
    print("=" * 60)
    print("Agent Genome Mapping™ — Unit Tests")
    print("Автор: Dm.Andreyanov | Проект: Prizolov Market & Lab")
    print("=" * 60)
    
    unittest.main(verbosity=2)
