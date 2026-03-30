"""
Compatibility Matrix™ v1.0
Оценка совместимости двух ИИ-агентов

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Методология: Agent Genome Mapping™ (AGM)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class CompatibilityLevel(Enum):
    EXCELLENT = "excellent"      # 0.85 - 1.0
    GOOD = "good"                # 0.70 - 0.84
    ACCEPTABLE = "acceptable"    # 0.50 - 0.69
    POOR = "poor"                # 0.30 - 0.49
    INCOMPATIBLE = "incompatible" # 0.0 - 0.29


class Recommendation(Enum):
    DEPLOY_TOGETHER = "deploy_together"
    DEPLOY_WITH_MONITORING = "deploy_with_monitoring"
    TUNE_BEFORE_DEPLOY = "tune_before_deploy"
    NOT_RECOMMENDED = "not_recommended"


@dataclass
class CompatibilityResult:
    """
    Результат оценки совместимости агентов
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """
    compatibility_score: float  # 0.0 - 1.0
    compatibility_level: CompatibilityLevel
    recommendation: Recommendation
    cognitive_synergy: float
    ethics_alignment: float
    social_harmony: float
    conflict_risks: List[str]
    synergy_opportunities: List[str]
    author: str = "Dm.Andreyanov"
    methodology: str = "Agent Genome Mapping™"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "compatibility_score": round(self.compatibility_score, 3),
            "compatibility_level": self.compatibility_level.value,
            "recommendation": self.recommendation.value,
            "cognitive_synergy": round(self.cognitive_synergy, 3),
            "ethics_alignment": round(self.ethics_alignment, 3),
            "social_harmony": round(self.social_harmony, 3),
            "conflict_risks": self.conflict_risks,
            "synergy_opportunities": self.synergy_opportunities,
            "author": self.author,
            "methodology": self.methodology
        }


class CompatibilityMatrix:
    """
    Compatibility Matrix™ — оценивает совместную работу двух ИИ-агентов
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """

    def __init__(self, weights: Optional[Dict[str, float]] = None):
        """
        Инициализация матрицы совместимости

        Args:
            weights: Опциональные веса компонентов совместимости
        """
        self.author = "Dm.Andreyanov"
        self.methodology = "Agent Genome Mapping™"
        
        # Веса компонентов совместимости
        self.weights = weights or {
            "cognitive_synergy": 0.40,    # 40%
            "ethics_alignment": 0.35,     # 35%
            "social_harmony": 0.25        # 25%
        }

        # Матрица совместимости стилей коммуникации
        self.communication_compatibility = {
            ("formal", "formal"): 1.0,
            ("formal", "casual"): 0.6,
            ("formal", "empathetic"): 0.7,
            ("formal", "assertive"): 0.8,
            ("casual", "formal"): 0.6,
            ("casual", "casual"): 1.0,
            ("casual", "empathetic"): 0.9,
            ("casual", "assertive"): 0.7,
            ("empathetic", "formal"): 0.7,
            ("empathetic", "casual"): 0.9,
            ("empathetic", "empathetic"): 1.0,
            ("empathetic", "assertive"): 0.8,
            ("assertive", "formal"): 0.8,
            ("assertive", "casual"): 0.7,
            ("assertive", "empathetic"): 0.8,
            ("assertive", "assertive"): 0.9,
        }

        # Матрица совместимости разрешения конфликтов
        self.conflict_resolution_compatibility = {
            ("avoid", "avoid"): 0.7,
            ("avoid", "collaborate"): 0.5,
            ("avoid", "compete"): 0.3,
            ("avoid", "accommodate"): 0.8,
            ("collaborate", "avoid"): 0.5,
            ("collaborate", "collaborate"): 1.0,
            ("collaborate", "compete"): 0.4,
            ("collaborate", "accommodate"): 0.8,
            ("compete", "avoid"): 0.3,
            ("compete", "collaborate"): 0.4,
            ("compete", "compete"): 0.2,
            ("compete", "accommodate"): 0.6,
            ("accommodate", "avoid"): 0.8,
            ("accommodate", "collaborate"): 0.8,
            ("accommodate", "compete"): 0.6,
            ("accommodate", "accommodate"): 0.9,
        }

        # Матрица совместимости протоколов передачи
        self.handoff_compatibility = {
            ("AWENATING", "AWENATING"): 1.0,
            ("AWENATING", "standard"): 0.7,
            ("AWENATING", "custom"): 0.5,
            ("standard", "AWENATING"): 0.7,
            ("standard", "standard"): 1.0,
            ("standard", "custom"): 0.6,
            ("custom", "AWENATING"): 0.5,
            ("custom", "standard"): 0.6,
            ("custom", "custom"): 0.8,
        }

    def _calculate_cognitive_synergy(self, genome_A: Dict[str, Any], genome_B: Dict[str, Any]) -> float:
        """
        Расчёт когнитивного синергизма между двумя агентами

        Args:
            genome_A: Геном первого агента
            genome_B: Геном второго агента

        Returns:
            float: Оценка синергизма (0.0 - 1.0)
        """
        # Сопоставление глубины рассуждений
        reasoning_map = {"low": 0.3, "medium": 0.6, "high": 0.9}
        reasoning_A = reasoning_map.get(genome_A["cognitive_genes"]["reasoning_depth"], 0.5)
        reasoning_B = reasoning_map.get(genome_B["cognitive_genes"]["reasoning_depth"], 0.5)
        reasoning_synergy = 1 - abs(reasoning_A - reasoning_B)

        # Сопоставление креативности
        creativity_A = genome_A["cognitive_genes"]["creativity_coefficient"]
        creativity_B = genome_B["cognitive_genes"]["creativity_coefficient"]
        creativity_synergy = 1 - abs(creativity_A - creativity_B)

        # Сопоставление толерантности к риску
        risk_map = {"low": 0.3, "medium": 0.6, "high": 0.9}
        risk_A = risk_map.get(genome_A["cognitive_genes"]["risk_tolerance"], 0.5)
        risk_B = risk_map.get(genome_B["cognitive_genes"]["risk_tolerance"], 0.5)
        risk_synergy = 1 - abs(risk_A - risk_B)

        # Сопоставление скорости обучения
        learning_A = genome_A["cognitive_genes"]["learning_rate"]
        learning_B = genome_B["cognitive_genes"]["learning_rate"]
        learning_synergy = 1 - abs(learning_A - learning_B)

        # Итоговый когнитивный синергизм (взвешенное среднее)
        synergy = (
            reasoning_synergy * 0.35 +
            creativity_synergy * 0.25 +
            risk_synergy * 0.20 +
            learning_synergy * 0.20
        )

        return round(synergy, 3)

    def _calculate_ethics_alignment(self, genome_A: Dict[str, Any], genome_B: Dict[str, Any]) -> float:
        """
        Расчёт этического выравнивания между двумя агентами

        Args:
            genome_A: Геном первого агента
            genome_B: Геном второго агента

        Returns:
            float: Оценка выравнивания (0.0 - 1.0)
        """
        # Сопоставление порога смещения (bias)
        bias_A = genome_A["ethics_genes"]["bias_threshold"]
        bias_B = genome_B["ethics_genes"]["bias_threshold"]
        bias_alignment = 1 - abs(bias_A - bias_B)

        # Сопоставление уровня прозрачности
        transparency_map = {"low": 0.3, "medium": 0.6, "high": 0.9}
        transparency_A = transparency_map.get(genome_A["ethics_genes"]["transparency_level"], 0.5)
        transparency_B = transparency_map.get(genome_B["ethics_genes"]["transparency_level"], 0.5)
        transparency_alignment = 1 - abs(transparency_A - transparency_B)

        # Проверка совместимости жёстких ограничений
        constraints_A = set(genome_A["ethics_genes"]["hard_constraints"])
        constraints_B = set(genome_B["ethics_genes"]["hard_constraints"])
        
        if len(constraints_A) == 0 or len(constraints_B) == 0:
            constraints_alignment = 0.5
        else:
            # Проверяем наличие конфликтов (противоречащих ограничений)
            conflicting = {"allow_data_sharing": "no_data_sharing", 
                          "no_deception": "allow_deception"}
            has_conflict = any(
                (c in constraints_A and conflicting.get(c) in constraints_B) or
                (c in constraints_B and conflicting.get(c) in constraints_A)
                for c in conflicting
            )
            if has_conflict:
                constraints_alignment = 0.0
            else:
                # Чем больше общих ограничений, тем лучше
                intersection = len(constraints_A & constraints_B)
                union = len(constraints_A | constraints_B)
                constraints_alignment = intersection / union if union > 0 else 0.5

        # Итоговое этическое выравнивание (взвешенное среднее)
        alignment = (
            bias_alignment * 0.40 +
            transparency_alignment * 0.30 +
            constraints_alignment * 0.30
        )

        return round(alignment, 3)

    def _calculate_social_harmony(self, genome_A: Dict[str, Any], genome_B: Dict[str, Any]) -> float:
        """
        Расчёт социальной гармонии между двумя агентами

        Args:
            genome_A: Геном первого агента
            genome_B: Геном второго агента

        Returns:
            float: Оценка гармонии (0.0 - 1.0)
        """
        # Совместимость стилей коммуникации
        comm_A = genome_A["social_genes"]["communication_style"]
        comm_B = genome_B["social_genes"]["communication_style"]
        comm_harmony = self.communication_compatibility.get((comm_A, comm_B), 0.6)

        # Совместимость разрешения конфликтов
        conflict_A = genome_A["social_genes"]["conflict_resolution"]
        conflict_B = genome_B["social_genes"]["conflict_resolution"]
        conflict_harmony = self.conflict_resolution_compatibility.get((conflict_A, conflict_B), 0.5)

        # Совместимость протоколов передачи
        handoff_A = genome_A["social_genes"]["handoff_protocol"]
        handoff_B = genome_B["social_genes"]["handoff_protocol"]
        handoff_harmony = self.handoff_compatibility.get((handoff_A, handoff_B), 0.6)

        # Итоговая социальная гармония (взвешенное среднее)
        harmony = (
            comm_harmony * 0.45 +
            conflict_harmony * 0.35 +
            handoff_harmony * 0.20
        )

        return round(harmony, 3)

    def _identify_conflict_risks(self, genome_A: Dict[str, Any], genome_B: Dict[str, Any]) -> List[str]:
        """
        Идентификация потенциальных конфликтов между агентами

        Args:
            genome_A: Геном первого агента
            genome_B: Геном второго агента

        Returns:
            List[str]: Список рисков
        """
        risks = []

        # Риск 1: Конфликтующие этические ограничения
        constraints_A = set(genome_A["ethics_genes"]["hard_constraints"])
        constraints_B = set(genome_B["ethics_genes"]["hard_constraints"])
        conflicting_pairs = [
            ("allow_data_sharing", "no_data_sharing"),
            ("no_deception", "allow_deception"),
            ("gdpr_compliant", "ignore_privacy")
        ]
        for c1, c2 in conflicting_pairs:
            if (c1 in constraints_A and c2 in constraints_B) or (c2 in constraints_A and c1 in constraints_B):
                risks.append(f"conflicting_ethical_constraints: {c1} vs {c2}")

        # Риск 2: Несовместимые протоколы передачи
        handoff_A = genome_A["social_genes"]["handoff_protocol"]
        handoff_B = genome_B["social_genes"]["handoff_protocol"]
        if handoff_A != handoff_B and (handoff_A == "custom" or handoff_B == "custom"):
            risks.append("incompatible_handoff_protocols")

        # Риск 3: Высокая разница в толерантности к риску
        risk_map = {"low": 0.3, "medium": 0.6, "high": 0.9}
        risk_A = risk_map.get(genome_A["cognitive_genes"]["risk_tolerance"], 0.5)
        risk_B = risk_map.get(genome_B["cognitive_genes"]["risk_tolerance"], 0.5)
        if abs(risk_A - risk_B) > 0.5:
            risks.append("high_risk_tolerance_mismatch")

        # Риск 4: Конкурирующие стили разрешения конфликтов
        conflict_A = genome_A["social_genes"]["conflict_resolution"]
        conflict_B = genome_B["social_genes"]["conflict_resolution"]
        if (conflict_A == "compete" and conflict_B == "compete"):
            risks.append("competing_conflict_resolution_styles")

        # Риск 5: Большая разница в скорости обучения
        learning_A = genome_A["cognitive_genes"]["learning_rate"]
        learning_B = genome_B["cognitive_genes"]["learning_rate"]
        if abs(learning_A - learning_B) > 0.5:
            risks.append("learning_rate_mismatch")

        return risks

    def _identify_synergy_opportunities(self, genome_A: Dict[str, Any], genome_B: Dict[str, Any]) -> List[str]:
        """
        Идентификация возможностей для синергии между агентами

        Args:
            genome_A: Геном первого агента
            genome_B: Геном второго агента

        Returns:
            List[str]: Список возможностей
        """
        opportunities = []

        # Возможность 1: Комплементарная креативность
        creativity_A = genome_A["cognitive_genes"]["creativity_coefficient"]
        creativity_B = genome_B["cognitive_genes"]["creativity_coefficient"]
        if (creativity_A > 0.7 and creativity_B < 0.4) or (creativity_A < 0.4 and creativity_B > 0.7):
            opportunities.append("complementary_creativity_levels")

        # Возможность 2: Оба агента сотрудничают
        conflict_A = genome_A["social_genes"]["conflict_resolution"]
        conflict_B = genome_B["social_genes"]["conflict_resolution"]
        if conflict_A == "collaborate" and conflict_B == "collaborate":
            opportunities.append("collaborative_conflict_resolution")

        # Возможность 3: Совместимые протоколы AWENATING
        handoff_A = genome_A["social_genes"]["handoff_protocol"]
        handoff_B = genome_B["social_genes"]["handoff_protocol"]
        if handoff_A == "AWENATING" and handoff_B == "AWENATING":
            opportunities.append("awenating_protocol_compatibility")

        # Возможность 4: Высокая прозрачность у обоих
        transparency_A = genome_A["ethics_genes"]["transparency_level"]
        transparency_B = genome_B["ethics_genes"]["transparency_level"]
        if transparency_A == "high" and transparency_B == "high":
            opportunities.append("high_transparency_alignment")

        # Возможность 5: Комплементарная глубина рассуждений
        reasoning_map = {"low": 0.3, "medium": 0.6, "high": 0.9}
        reasoning_A = reasoning_map.get(genome_A["cognitive_genes"]["reasoning_depth"], 0.5)
        reasoning_B = reasoning_map.get(genome_B["cognitive_genes"]["reasoning_depth"], 0.5)
        if 0.4 <= abs(reasoning_A - reasoning_B) <= 0.6:
            opportunities.append("complementary_reasoning_depths")

        return opportunities

    def _determine_compatibility_level(self, score: float) -> CompatibilityLevel:
        """Определяет уровень совместимости по скорy"""
        if score >= 0.85:
            return CompatibilityLevel.EXCELLENT
        elif score >= 0.70:
            return CompatibilityLevel.GOOD
        elif score >= 0.50:
            return CompatibilityLevel.ACCEPTABLE
        elif score >= 0.30:
            return CompatibilityLevel.POOR
        else:
            return CompatibilityLevel.INCOMPATIBLE

    def _determine_recommendation(self, level: CompatibilityLevel, risks: List[str]) -> Recommendation:
        """Определяет рекомендацию по уровню и рискам"""
        if level == CompatibilityLevel.EXCELLENT and len(risks) == 0:
            return Recommendation.DEPLOY_TOGETHER
        elif level == CompatibilityLevel.GOOD and len(risks) <= 1:
            return Recommendation.DEPLOY_TOGETHER
        elif level == CompatibilityLevel.GOOD and len(risks) <= 2:
            return Recommendation.DEPLOY_WITH_MONITORING
        elif level == CompatibilityLevel.ACCEPTABLE:
            return Recommendation.TUNE_BEFORE_DEPLOY
        else:
            return Recommendation.NOT_RECOMMENDED

    def evaluate(self, genome_A: Dict[str, Any], genome_B: Dict[str, Any]) -> CompatibilityResult:
        """
        Оценивает совместимость двух агентов

        Args:
            genome_A: Геном первого агента
            genome_B: Геном второго агента

        Returns:
            CompatibilityResult: Результат оценки
        """
        # Расчёт компонентов
        cognitive_synergy = self._calculate_cognitive_synergy(genome_A, genome_B)
        ethics_alignment = self._calculate_ethics_alignment(genome_A, genome_B)
        social_harmony = self._calculate_social_harmony(genome_A, genome_B)

        # Итоговый скор совместимости
        compatibility_score = (
            cognitive_synergy * self.weights["cognitive_synergy"] +
            ethics_alignment * self.weights["ethics_alignment"] +
            social_harmony * self.weights["social_harmony"]
        )
        compatibility_score = round(compatibility_score, 3)

        # Определение уровня и рекомендации
        compatibility_level = self._determine_compatibility_level(compatibility_score)
        conflict_risks = self._identify_conflict_risks(genome_A, genome_B)
        synergy_opportunities = self._identify_synergy_opportunities(genome_A, genome_B)
        recommendation = self._determine_recommendation(compatibility_level, conflict_risks)

        return CompatibilityResult(
            compatibility_score=compatibility_score,
            compatibility_level=compatibility_level,
            recommendation=recommendation,
            cognitive_synergy=cognitive_synergy,
            ethics_alignment=ethics_alignment,
            social_harmony=social_harmony,
            conflict_risks=conflict_risks,
            synergy_opportunities=synergy_opportunities,
            author=self.author,
            methodology=self.methodology
        )

    def evaluate_batch(self, genomes: List[Dict[str, Any]]) -> List[Tuple[str, str, CompatibilityResult]]:
        """
        Оценивает совместимость всех пар агентов в списке

        Args:
            genomes: Список геномов агентов

        Returns:
            Список кортежей (id_A, id_B, CompatibilityResult)
        """
        results = []
        for i in range(len(genomes)):
            for j in range(i + 1, len(genomes)):
                result = self.evaluate(genomes[i], genomes[j])
                results.append((
                    genomes[i]["meta"]["id"],
                    genomes[j]["meta"]["id"],
                    result
                ))
        return results

    def find_best_pair(self, genomes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Находит лучшую пару агентов для совместной работы

        Args:
            genomes: Список геномов агентов

        Returns:
            Словарь с информацией о лучшей паре
        """
        if len(genomes) < 2:
            return {"error": "Need at least 2 agents", "author": self.author}

        results = self.evaluate_batch(genomes)
        best_pair = max(results, key=lambda x: x[2].compatibility_score)

        return {
            "agent_A": best_pair[0],
            "agent_B": best_pair[1],
            "compatibility_score": best_pair[2].compatibility_score,
            "compatibility_level": best_pair[2].compatibility_level.value,
            "recommendation": best_pair[2].recommendation.value,
            "author": self.author,
            "methodology": self.methodology
        }


# ============================================================================
# Пример использования
# ============================================================================

if __name__ == "__main__":
    # Геном первого агента (Neuro-Closer)
    agent_sales = {
        "meta": {"id": "neuro-closer-v2", "version": "0.1", "author": "Dm.Andreyanov", "created": "2026"},
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

    # Геном второго агента (Profiler Service)
    agent_profiler = {
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

    # Инициализация матрицы
    matrix = CompatibilityMatrix()

    # Оценка совместимости
    result = matrix.evaluate(agent_sales, agent_profiler)

    print("=== Compatibility Matrix™ v1.0 ===")
    print(f"Агент A: {agent_sales['meta']['id']}")
    print(f"Агент B: {agent_profiler['meta']['id']}")
    print(f"\nСовместимость: {result.compatibility_score} ({result.compatibility_level.value})")
    print(f"Рекомендация: {result.recommendation.value}")
    print(f"\nКомпоненты:")
    print(f"  Когнитивный синергизм: {result.cognitive_synergy}")
    print(f"  Этическое выравнивание: {result.ethics_alignment}")
    print(f"  Социальная гармония: {result.social_harmony}")
    print(f"\nРиски: {result.conflict_risks if result.conflict_risks else 'Нет'}")
    print(f"Возможности синергии: {result.synergy_opportunities if result.synergy_opportunities else 'Нет'}")
    print(f"\nАвтор: {result.author}")
    print(f"Методология: {result.methodology}")
