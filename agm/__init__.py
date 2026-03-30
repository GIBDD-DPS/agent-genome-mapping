"""
Agent Genome Mapping™ (AGM)
Evolutionary Architecture for Autonomous AI Systems

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Версия: 0.1.0
"""

__version__ = "0.1.0"
__author__ = "Dm.Andreyanov"
__project__ = "Prizolov Market & Lab"

# Импорт основных классов из всех модулей
from .genome_schema import (
    AgentGenome,
    CognitiveGenes,
    EthicsGenes,
    SocialGenes,
    MetaGenes,
    ReasoningDepth,
    RiskTolerance,
    TransparencyLevel,
    CommunicationStyle,
    ConflictResolution,
    HandoffProtocol,
    SelectionPressure
)

from .phenotype_engine import (
    PhenotypeEngine,
    PhenotypePrediction,
    Recommendation
)

from .compatibility_matrix import (
    CompatibilityMatrix,
    CompatibilityResult,
    CompatibilityLevel
)

from .evolutionary_sandbox import (
    EvolutionarySandbox,
    EvolutionResult,
    EvolutionEvent,
    BreedingStrategy,
    MutationType,
    SelectionMethod
)

from .drift_monitor import (
    DriftMonitor,
    DriftReport,
    DriftAlert,
    LedgerEntry,
    DriftSeverity,
    AlertType
)

# Экспортируем всё для удобного импорта
__all__ = [
    # Genome Schema™
    "AgentGenome",
    "CognitiveGenes",
    "EthicsGenes",
    "SocialGenes",
    "MetaGenes",
    "ReasoningDepth",
    "RiskTolerance",
    "TransparencyLevel",
    "CommunicationStyle",
    "ConflictResolution",
    "HandoffProtocol",
    "SelectionPressure",
    
    # Phenotype Engine™
    "PhenotypeEngine",
    "PhenotypePrediction",
    "Recommendation",
    
    # Compatibility Matrix™
    "CompatibilityMatrix",
    "CompatibilityResult",
    "CompatibilityLevel",
    
    # Evolutionary Sandbox™
    "EvolutionarySandbox",
    "EvolutionResult",
    "EvolutionEvent",
    "BreedingStrategy",
    "MutationType",
    "SelectionMethod",
    
    # Drift Monitor™
    "DriftMonitor",
    "DriftReport",
    "DriftAlert",
    "LedgerEntry",
    "DriftSeverity",
    "AlertType"
]
