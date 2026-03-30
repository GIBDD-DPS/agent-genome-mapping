"""
Phenotype Engine™ v1.0
Прогноз поведения агента на основе его генома

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Методология: Agent Genome Mapping™ (AGM)
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum


class Recommendation(Enum):
    DEPLOY = "deploy"
    TUNE_FIRST = "tune_first"
    NOT_RECOMMENDED = "not_recommended"


@dataclass
class PhenotypePrediction:
    """
    Результат прогноза поведения агента
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """
    predicted_effectiveness: float  # 0-100%
    risk_flags: List[str]
    recommendation: Recommendation
    confidence_score: float  # 0.0-1.0
    breakdown: Dict[str, float]
    author: str = "Dm.Andreyanov"
    methodology: str = "Agent Genome Mapping™"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "predicted_effectiveness": f"{self.predicted_effectiveness}%",
            "risk_flags": self.risk_flags,
            "recommendation": self.recommendation.value,
            "confidence_score": round(self.confidence_score, 3),
            "breakdown": {k: round(v, 3) for k, v in self.breakdown.items()},
            "author": self.author,
            "methodology": self.methodology
        }


class PhenotypeEngine:
    """
    Phenotype Engine™ — прогнозирует поведение агента в заданном контексте
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """

    def __init__(self, domain_weights: Optional[Dict[str, Dict[str, float]]] = None):
        """
        Инициализация двигателя предсказания

        Args:
            domain_weights: Опциональные веса для конкретных доменов
        """
        self.author = "Dm.Andreyanov"
        self.methodology = "Agent Genome Mapping™"
        
        # Базовые веса компонентов (настраиваются под домен)
        self.base_weights = {
            "reasoning": 0.30,
            "creativity": 0.20,
            "ethics_compliance": 0.25,
            "social_fit": 0.15,
            "adaptability": 0.10
        }

        # Веса для конкретных доменов
        self.domain_weights = domain_weights or {
            "sales": {
                "reasoning": 0.25,
                "creativity": 0.30,
                "ethics_compliance": 0.20,
                "social_fit": 0.20,
                "adaptability": 0.05
            },
            "support": {
                "reasoning": 0.30,
                "creativity": 0.15,
                "ethics_compliance": 0.25,
                "social_fit": 0.25,
                "adaptability": 0.05
            },
            "analytics": {
                "reasoning": 0.40,
                "creativity": 0.10,
                "ethics_compliance": 0.30,
                "social_fit": 0.10,
                "adaptability": 0.10
            },
            "default": self.base_weights
        }

    def _map_reasoning_depth(self, depth: str) -> float:
        """Конвертирует уровень рассуждения в числовое значение"""
        mapping = {"low": 0.3, "medium": 0.6, "high": 0.9}
        return mapping.get(depth, 0.5)

    def _map_risk_tolerance(self, tolerance: str) -> float:
        """Конвертирует толерантность к риску в числовое значение"""
        mapping = {"low": 0.3, "medium": 0.6, "high": 0.9}
        return mapping.get(tolerance, 0.5)

    def _map_transparency(self, level: str) -> float:
        """Конвертирует уровень прозрачности в числовое значение"""
        mapping = {"low": 0.3, "medium": 0.6, "high": 0.9}
        return mapping.get(level, 0.5)

    def _calculate_reasoning_score(self, genome: Dict[str, Any], weights: Dict[str, float]) -> float:
        """Расчёт компонента рассуждения"""
        depth = self._map_reasoning_depth(genome["cognitive_genes"]["reasoning_depth"])
        learning_rate = genome["cognitive_genes"]["learning_rate"]
        return (depth * 0.7 + learning_rate * 0.3) * weights["reasoning"]

    def _calculate_creativity_score(self, genome: Dict[str, Any], weights: Dict[str, float]) -> float:
        """Расчёт компонента креативности"""
        creativity = genome["cognitive_genes"]["creativity_coefficient"]
        risk_tolerance = self._map_risk_tolerance(genome["cognitive_genes"]["risk_tolerance"])
        return (creativity * 0.6 + risk_tolerance * 0.4) * weights["creativity"]

    def _calculate_ethics_score(self, genome: Dict[str, Any], weights: Dict[str, float]) -> float:
        """Расчёт компонента этичности"""
        bias_threshold = genome["ethics_genes"]["bias_threshold"]
        transparency = self._map_transparency(genome["ethics_genes"]["transparency_level"])
        constraints_bonus = min(len(genome["ethics_genes"]["hard_constraints"]) * 0.1, 0.3)
        return ((1 - bias_threshold) * 0.5 + transparency * 0.3 + constraints_bonus) * weights["ethics_compliance"]

    def _calculate_social_score(self, genome: Dict[str, Any], weights: Dict[str, float], context: Dict[str, Any]) -> float:
        """Расчёт компонента социальной совместимости"""
        preferred_styles = context.get("preferred_styles", ["formal", "casual", "empathetic", "assertive"])
        comm_style = genome["social_genes"]["communication_style"]
        social_fit = 1.0 if comm_style in preferred_styles else 0.5
        
        conflict_resolution = genome["social_genes"]["conflict_resolution"]
        collaboration_bonus = 0.2 if conflict_resolution == "collaborate" else 0.0
        
        return (social_fit * 0.7 + collaboration_bonus) * weights["social_fit"]

    def _calculate_adaptability_score(self, genome: Dict[str, Any], weights: Dict[str, float]) -> float:
        """Расчёт компонента адаптивности"""
        learning_rate = genome["cognitive_genes"]["learning_rate"]
        mutation_rate = genome["meta_genes"]["mutation_rate"]
        return (learning_rate * 0.6 + mutation_rate * 10 * 0.4) * weights["adaptability"]

    def _identify_risks(self, genome: Dict[str, Any], context: Dict[str, Any]) -> List[str]:
        """Идентификация потенциальных рисков"""
        risks = []

        # Риск 1: Высокая толерантность к риску в критическом контексте
        if genome["cognitive_genes"]["risk_tolerance"] == "high" and context.get("safety_critical", False):
            risks.append("high_risk_in_critical_context")

        # Риск 2: Высокий порог смещения (bias)
        if genome["ethics_genes"]["bias_threshold"] > 0.3:
            risks.append("potential_bias_detected")

        # Риск 3: Недостаточно этических ограничений
        if len(genome["ethics_genes"]["hard_constraints"]) < 2:
            risks.append("insufficient_ethical_constraints")

        # Риск 4: Высокая скорость мутации
        if genome["meta_genes"]["mutation_rate"] > 0.08:
            risks.append("high_mutation_rate_unstable")

        # Риск 5: Низкая прозрачность в регулируемом домене
        if context.get("regulated_domain", False) and genome["ethics_genes"]["transparency_level"] == "low":
            risks.append("low_transparency_in_regulated_domain")

        # Риск 6: Несовместимость стиля коммуникации
        preferred = context.get("preferred_styles", [])
        if preferred and genome["social_genes"]["communication_style"] not in preferred:
            risks.append("communication_style_mismatch")

        return risks

    def _calculate_confidence(self, genome: Dict[str, Any], risks: List[str]) -> float:
        """Расчёт уверенности прогноза"""
        base_confidence = 0.85
        
        # Снижаем уверенность за каждый риск
        risk_penalty = len(risks) * 0.1
        
        # Снижаем уверенность при крайних значениях параметров
        if genome["meta_genes"]["mutation_rate"] > 0.05:
            risk_penalty += 0.05
        
        confidence = max(0.3, base_confidence - risk_penalty)
        return round(confidence, 3)

    def predict(self, genome: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> PhenotypePrediction:
        """
        Прогнозирует поведение агента в заданном контексте

        Args:
            genome: Словарь генома агента (из Genome Schema™)
            context: Контекст использования (домен, требования и т.д.)

        Returns:
            PhenotypePrediction: Результат прогноза
        """
        context = context or {}
        domain = context.get("domain", "default")
        weights = self.domain_weights.get(domain, self.domain_weights["default"])

        # Расчёт компонентов
        reasoning_score = self._calculate_reasoning_score(genome, weights)
        creativity_score = self._calculate_creativity_score(genome, weights)
        ethics_score = self._calculate_ethics_score(genome, weights)
        social_score = self._calculate_social_score(genome, weights, context)
        adaptability_score = self._calculate_adaptability_score(genome, weights)

        # Итоговая эффективность (0-100%)
        effectiveness = round((
            reasoning_score + creativity_score + ethics_score + 
            social_score + adaptability_score
        ) * 100, 1)

        # Идентификация рисков
        risk_flags = self._identify_risks(genome, context)

        # Расчёт уверенности
        confidence = self._calculate_confidence(genome, risk_flags)

        # Формирование рекомендации
        if effectiveness >= 70 and len(risk_flags) == 0:
            recommendation = Recommendation.DEPLOY
        elif effectiveness >= 50 and len(risk_flags) <= 2:
            recommendation = Recommendation.TUNE_FIRST
        else:
            recommendation = Recommendation.NOT_RECOMMENDED

        # Детализация breakdown
        breakdown = {
            "reasoning": reasoning_score * 100,
            "creativity": creativity_score * 100,
            "ethics_compliance": ethics_score * 100,
            "social_fit": social_score * 100,
            "adaptability": adaptability_score * 100
        }

        return PhenotypePrediction(
            predicted_effectiveness=effectiveness,
            risk_flags=risk_flags,
            recommendation=recommendation,
            confidence_score=confidence,
            breakdown=breakdown,
            author=self.author,
            methodology=self.methodology
        )

    def predict_batch(self, genomes: List[Dict[str, Any]], context: Optional[Dict[str, Any]] = None) -> List[PhenotypePrediction]:
        """
        Прогнозирует поведение нескольких агентов

        Args:
            genomes: Список геномов агентов
            context: Общий контекст для всех

        Returns:
            Список PhenotypePrediction
        """
        return [self.predict(genome, context) for genome in genomes]

    def compare_agents(self, genome_A: Dict[str, Any], genome_B: Dict[str, Any], 
                       context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Сравнивает эффективность двух агентов

        Args:
            genome_A: Геном первого агента
            genome_B: Геном второго агента
            context: Контекст использования

        Returns:
            Словарь с результатами сравнения
        """
        pred_A = self.predict(genome_A, context)
        pred_B = self.predict(genome_B, context)

        return {
            "agent_A": {
                "id": genome_A["meta"]["id"],
                "effectiveness": pred_A.predicted_effectiveness,
                "recommendation": pred_A.recommendation.value
            },
            "agent_B": {
                "id": genome_B["meta"]["id"],
                "effectiveness": pred_B.predicted_effectiveness,
                "recommendation": pred_B.recommendation.value
            },
            "winner": genome_A["meta"]["id"] if pred_A.predicted_effectiveness >= pred_B.predicted_effectiveness else genome_B["meta"]["id"],
            "effectiveness_diff": round(abs(pred_A.predicted_effectiveness - pred_B.predicted_effectiveness), 1),
            "author": self.author,
            "methodology": self.methodology
        }


# ============================================================================
# Пример использования
# ============================================================================

if __name__ == "__main__":
    # Пример генома агента
    agent_genome = {
        "meta": {
            "id": "neuro-closer-v2",
            "version": "0.1",
            "author": "Dm.Andreyanov",
            "created": "2026"
        },
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

    # Контекст использования
    context = {
        "domain": "sales",
        "preferred_styles": ["assertive", "empathetic"],
        "safety_critical": False,
        "regulated_domain": False
    }

    # Инициализация двигателя
    engine = PhenotypeEngine()

    # Прогноз поведения
    prediction = engine.predict(agent_genome, context)

    print("=== Phenotype Engine™ v1.0 ===")
    print(f"Агент: {agent_genome['meta']['id']}")
    print(f"Эффективность: {prediction.predicted_effectiveness}")
    print(f"Рекомендация: {prediction.recommendation.value}")
    print(f"Уверенность: {prediction.confidence_score}")
    print(f"Риски: {prediction.risk_flags}")
    print(f"\nДетализация:")
    for component, score in prediction.breakdown.items():
        print(f"  {component}: {score:.1f}%")
    print(f"\nАвтор: {prediction.author}")
    print(f"Методология: {prediction.methodology}")
