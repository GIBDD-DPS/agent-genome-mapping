"""
Genome Schema™ v1.0
Стандартизированное описание «ДНК агента»

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Методология: Agent Genome Mapping™ (AGM)
"""

import yaml
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum


class ReasoningDepth(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class RiskTolerance(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TransparencyLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class CommunicationStyle(Enum):
    FORMAL = "formal"
    CASUAL = "casual"
    EMPATHETIC = "empathetic"
    ASSERTIVE = "assertive"


class ConflictResolution(Enum):
    AVOID = "avoid"
    COLLABORATE = "collaborate"
    COMPETE = "compete"
    ACCOMMODATE = "accommodate"


class HandoffProtocol(Enum):
    AWENATING = "AWENATING"
    STANDARD = "standard"
    CUSTOM = "custom"


class SelectionPressure(Enum):
    PERFORMANCE = "performance"
    ETHICS = "ethics"
    HYBRID = "hybrid"


@dataclass
class CognitiveGenes:
    reasoning_depth: ReasoningDepth
    creativity_coefficient: float  # 0.0 - 1.0
    risk_tolerance: RiskTolerance
    learning_rate: float  # 0.0 - 1.0

    def validate(self) -> List[str]:
        errors = []
        if not 0.0 <= self.creativity_coefficient <= 1.0:
            errors.append("creativity_coefficient must be between 0.0 and 1.0")
        if not 0.0 <= self.learning_rate <= 1.0:
            errors.append("learning_rate must be between 0.0 and 1.0")
        return errors


@dataclass
class EthicsGenes:
    bias_threshold: float  # 0.0 - 1.0
    transparency_level: TransparencyLevel
    hard_constraints: List[str]

    def validate(self) -> List[str]:
        errors = []
        if not 0.0 <= self.bias_threshold <= 1.0:
            errors.append("bias_threshold must be between 0.0 and 1.0")
        if len(self.hard_constraints) == 0:
            errors.append("hard_constraints cannot be empty")
        return errors


@dataclass
class SocialGenes:
    communication_style: CommunicationStyle
    conflict_resolution: ConflictResolution
    handoff_protocol: HandoffProtocol

    def validate(self) -> List[str]:
        return []


@dataclass
class MetaGenes:
    mutation_rate: float  # 0.0 - 0.1
    selection_pressure: SelectionPressure
    generation_limit: int

    def validate(self) -> List[str]:
        errors = []
        if not 0.0 <= self.mutation_rate <= 0.1:
            errors.append("mutation_rate must be between 0.0 and 0.1")
        if self.generation_limit < 1:
            errors.append("generation_limit must be at least 1")
        return errors


@dataclass
class AgentGenome:
    """
    Genome Schema™ — стандартизированное описание «ДНК агента»
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """
    id: str
    version: str
    author: str
    created: str
    cognitive_genes: CognitiveGenes
    ethics_genes: EthicsGenes
    social_genes: SocialGenes
    meta_genes: MetaGenes

    def validate(self) -> Dict[str, Any]:
        """Проверка валидности генома"""
        errors = {
            "cognitive_genes": self.cognitive_genes.validate(),
            "ethics_genes": self.ethics_genes.validate(),
            "social_genes": self.social_genes.validate(),
            "meta_genes": self.meta_genes.validate()
        }
        
        is_valid = all(len(v) == 0 for v in errors.values())
        
        return {
            "is_valid": is_valid,
            "errors": errors,
            "author": "Dm.Andreyanov",
            "methodology": "Agent Genome Mapping™"
        }

    def to_yaml(self) -> str:
        """Экспорт генома в YAML-формат"""
        data = {
            "agent_genome": {
                "meta": {
                    "id": self.id,
                    "version": self.version,
                    "author": self.author,
                    "created": self.created
                },
                "cognitive_genes": {
                    "reasoning_depth": self.cognitive_genes.reasoning_depth.value,
                    "creativity_coefficient": self.cognitive_genes.creativity_coefficient,
                    "risk_tolerance": self.cognitive_genes.risk_tolerance.value,
                    "learning_rate": self.cognitive_genes.learning_rate
                },
                "ethics_genes": {
                    "bias_threshold": self.ethics_genes.bias_threshold,
                    "transparency_level": self.ethics_genes.transparency_level.value,
                    "hard_constraints": self.ethics_genes.hard_constraints
                },
                "social_genes": {
                    "communication_style": self.social_genes.communication_style.value,
                    "conflict_resolution": self.social_genes.conflict_resolution.value,
                    "handoff_protocol": self.social_genes.handoff_protocol.value
                },
                "meta_genes": {
                    "mutation_rate": self.meta_genes.mutation_rate,
                    "selection_pressure": self.meta_genes.selection_pressure.value,
                    "generation_limit": self.meta_genes.generation_limit
                }
            }
        }
        return yaml.dump(data, allow_unicode=True, default_flow_style=False)

    @classmethod
    def from_yaml(cls, yaml_string: str) -> "AgentGenome":
        """Импорт генома из YAML-формата"""
        data = yaml.safe_load(yaml_string)["agent_genome"]
        
        return cls(
            id=data["meta"]["id"],
            version=data["meta"]["version"],
            author=data["meta"]["author"],
            created=data["meta"]["created"],
            cognitive_genes=CognitiveGenes(
                reasoning_depth=ReasoningDepth(data["cognitive_genes"]["reasoning_depth"]),
                creativity_coefficient=data["cognitive_genes"]["creativity_coefficient"],
                risk_tolerance=RiskTolerance(data["cognitive_genes"]["risk_tolerance"]),
                learning_rate=data["cognitive_genes"]["learning_rate"]
            ),
            ethics_genes=EthicsGenes(
                bias_threshold=data["ethics_genes"]["bias_threshold"],
                transparency_level=TransparencyLevel(data["ethics_genes"]["transparency_level"]),
                hard_constraints=data["ethics_genes"]["hard_constraints"]
            ),
            social_genes=SocialGenes(
                communication_style=CommunicationStyle(data["social_genes"]["communication_style"]),
                conflict_resolution=ConflictResolution(data["social_genes"]["conflict_resolution"]),
                handoff_protocol=HandoffProtocol(data["social_genes"]["handoff_protocol"])
            ),
            meta_genes=MetaGenes(
                mutation_rate=data["meta_genes"]["mutation_rate"],
                selection_pressure=SelectionPressure(data["meta_genes"]["selection_pressure"]),
                generation_limit=data["meta_genes"]["generation_limit"]
            )
        )

    def to_dict(self) -> Dict[str, Any]:
        """Экспорт генома в словарь (для совместимости с другими модулями AGM)"""
        return {
            "meta": {
                "id": self.id,
                "version": self.version,
                "author": self.author,
                "created": self.created
            },
            "cognitive_genes": {
                "reasoning_depth": self.cognitive_genes.reasoning_depth.value,
                "creativity_coefficient": self.cognitive_genes.creativity_coefficient,
                "risk_tolerance": self.cognitive_genes.risk_tolerance.value,
                "learning_rate": self.cognitive_genes.learning_rate
            },
            "ethics_genes": {
                "bias_threshold": self.ethics_genes.bias_threshold,
                "transparency_level": self.ethics_genes.transparency_level.value,
                "hard_constraints": self.ethics_genes.hard_constraints
            },
            "social_genes": {
                "communication_style": self.social_genes.communication_style.value,
                "conflict_resolution": self.social_genes.conflict_resolution.value,
                "handoff_protocol": self.social_genes.handoff_protocol.value
            },
            "meta_genes": {
                "mutation_rate": self.meta_genes.mutation_rate,
                "selection_pressure": self.meta_genes.selection_pressure.value,
                "generation_limit": self.meta_genes.generation_limit
            }
        }


# ============================================================================
# Пример использования
# ============================================================================

if __name__ == "__main__":
    # Создание генома агента
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
    print(f"Валидность: {validation['is_valid']}")
    print(f"Ошибки: {validation['errors']}")

    # Экспорт в YAML
    print("\n=== YAML-экспорт ===")
    print(genome.to_yaml())

    # Экспорт в словарь
    print("\n=== Dict-экспорт ===")
    print(genome.to_dict())

    print(f"\nАвтор: {validation['author']}")
    print(f"Методология: {validation['methodology']}")
