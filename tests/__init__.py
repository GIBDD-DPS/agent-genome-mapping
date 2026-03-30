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

from .genome_schema import GenomeSchema
from .phenotype_engine import PhenotypeEngine
from .compatibility_matrix import CompatibilityMatrix
from .evolutionary_sandbox import EvolutionarySandbox
from .drift_monitor import DriftMonitor

__all__ = [
    "GenomeSchema",
    "PhenotypeEngine",
    "CompatibilityMatrix",
    "EvolutionarySandbox",
    "DriftMonitor"
]
