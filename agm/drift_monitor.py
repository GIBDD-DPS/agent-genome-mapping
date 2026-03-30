"""
Drift Monitor™ + Genome Ledger™ v1.0
Отслеживание отклонений агента и аудит в реальном времени

Автор: Dm.Andreyanov
Проект: Prizolov Market & Lab
Методология: Agent Genome Mapping™ (AGM)
"""

import hashlib
import json
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum


class DriftSeverity(Enum):
    NONE = "none"           # 0.0 - 0.1
    LOW = "low"             # 0.1 - 0.3
    MEDIUM = "medium"       # 0.3 - 0.5
    HIGH = "high"           # 0.5 - 0.7
    CRITICAL = "critical"   # 0.7 - 1.0


class AlertType(Enum):
    COGNITIVE_DRIFT = "cognitive_drift"
    ETHICS_DEVIATION = "ethics_deviation"
    SOCIAL_PROTOCOL_VIOLATION = "social_protocol_violation"
    META_GENE_MUTATION = "meta_gene_mutation"
    CONSTRAINT_VIOLATION = "constraint_violation"


@dataclass
class DriftAlert:
    """
    Предупреждение о дрейфе агента
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """
    alert_type: AlertType
    severity: DriftSeverity
    timestamp: str
    agent_id: str
    baseline_value: Any
    current_value: Any
    drift_score: float
    description: str
    recommended_action: str
    author: str = "Dm.Andreyanov"
    methodology: str = "Agent Genome Mapping™"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "alert_type": self.alert_type.value,
            "severity": self.severity.value,
            "timestamp": self.timestamp,
            "agent_id": self.agent_id,
            "baseline_value": self.baseline_value,
            "current_value": self.current_value,
            "drift_score": round(self.drift_score, 4),
            "description": self.description,
            "recommended_action": self.recommended_action,
            "author": self.author,
            "methodology": self.methodology
        }


@dataclass
class LedgerEntry:
    """
    Запись в Genome Ledger™ (неизменяемый журнал)
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """
    entry_id: str
    timestamp: str
    event_type: str
    agent_id: str
    previous_hash: str
    current_hash: str
    data: Dict[str, Any]
    signature: str
    author: str = "Dm.Andreyanov"
    methodology: str = "Agent Genome Mapping™"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "entry_id": self.entry_id,
            "timestamp": self.timestamp,
            "event_type": self.event_type,
            "agent_id": self.agent_id,
            "previous_hash": self.previous_hash,
            "current_hash": self.current_hash,
            "data": self.data,
            "signature": self.signature,
            "author": self.author,
            "methodology": self.methodology
        }


@dataclass
class DriftReport:
    """
    Отчёт о дрейфе агента
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """
    agent_id: str
    check_timestamp: str
    overall_drift_score: float
    drift_severity: DriftSeverity
    status: str  # "stable", "review_needed", "critical"
    alerts: List[DriftAlert]
    cognitive_drift_index: float
    ethics_deviation_score: float
    social_protocol_violation: bool
    ledger_entries_count: int
    author: str = "Dm.Andreyanov"
    methodology: str = "Agent Genome Mapping™"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "check_timestamp": self.check_timestamp,
            "overall_drift_score": round(self.overall_drift_score, 4),
            "drift_severity": self.drift_severity.value,
            "status": self.status,
            "alerts": [a.to_dict() for a in self.alerts],
            "cognitive_drift_index": round(self.cognitive_drift_index, 4),
            "ethics_deviation_score": round(self.ethics_deviation_score, 4),
            "social_protocol_violation": self.social_protocol_violation,
            "ledger_entries_count": self.ledger_entries_count,
            "author": self.author,
            "methodology": self.methodology
        }


class DriftMonitor:
    """
    Drift Monitor™ — отслеживание отклонений агента от исходного генома
    Genome Ledger™ — неизменяемый журнал всех изменений
    Автор: Dm.Andreyanov для Agent Genome Mapping™
    """

    def __init__(
        self,
        baseline_genome: Dict[str, Any],
        thresholds: Optional[Dict[str, float]] = None,
        enable_blockchain_style: bool = True
    ):
        """
        Инициализация монитора дрейфа

        Args:
            baseline_genome: Базовый геном агента (точка отсчёта)
            thresholds: Пороги срабатывания предупреждений
            enable_blockchain_style: Включить цепочку хешей для аудита
        """
        self.author = "Dm.Andreyanov"
        self.methodology = "Agent Genome Mapping™"
        
        self.baseline = baseline_genome
        self.agent_id = baseline_genome.get("meta", {}).get("id", "unknown")
        self.enable_blockchain = enable_blockchain_style
        
        # Пороги срабатывания
        self.thresholds = thresholds or {
            "cognitive_drift_low": 0.1,
            "cognitive_drift_medium": 0.3,
            "cognitive_drift_high": 0.5,
            "cognitive_drift_critical": 0.7,
            "ethics_deviation_low": 0.05,
            "ethics_deviation_medium": 0.15,
            "ethics_deviation_high": 0.3,
            "ethics_deviation_critical": 0.5
        }
        
        # Журнал событий (Genome Ledger™)
        self.ledger: List[LedgerEntry] = []
        self.alerts: List[DriftAlert] = []
        self.previous_hash: str = self._generate_hash("genesis", baseline_genome)
        
        # Счётчики
        self.check_count = 0
        self.last_check_timestamp: Optional[str] = None

    def _generate_hash(self, data_type: str, data: Any) -> str:
        """Генерация SHA-256 хеша для записи в ledger"""
        content = f"{data_type}:{json.dumps(data, sort_keys=True)}"
        return hashlib.sha256(content.encode()).hexdigest()

    def _generate_entry_id(self) -> str:
        """Генерация уникального ID для записи"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        return f"entry-{self.agent_id}-{timestamp}"

    def _generate_signature(self, entry_data: Dict[str, Any]) -> str:
        """Генерация цифровой подписи записи"""
        content = json.dumps(entry_data, sort_keys=True)
        signature = f"{self.author}:{self.methodology}:{content}"
        return hashlib.sha256(signature.encode()).hexdigest()[:16]

    def _log_to_ledger(
        self,
        event_type: str,
        agent_id: str,
        data: Dict[str, Any]
    ) -> LedgerEntry:
        """Добавление записи в Genome Ledger™"""
        current_hash = self._generate_hash(event_type, data)
        
        entry_data = {
            "entry_id": self._generate_entry_id(),
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "agent_id": agent_id,
            "previous_hash": self.previous_hash,
            "current_hash": current_hash,
            "data": data
        }
        
        entry = LedgerEntry(
            entry_id=entry_data["entry_id"],
            timestamp=entry_data["timestamp"],
            event_type=event_type,
            agent_id=agent_id,
            previous_hash=self.previous_hash,
            current_hash=current_hash,
            data=data,
            signature=self._generate_signature(entry_data)
        )
        
        self.ledger.append(entry)
        self.previous_hash = current_hash
        
        return entry

    def _calculate_cognitive_drift(
        self,
        baseline: Dict[str, Any],
        current: Dict[str, Any]
    ) -> float:
        """Расчёт индекса когнитивного дрейфа"""
        drift_scores = []
        
        # Глубина рассуждений
        reasoning_map = {"low": 0.3, "medium": 0.6, "high": 0.9}
        baseline_reasoning = reasoning_map.get(
            baseline["cognitive_genes"]["reasoning_depth"], 0.5
        )
        current_reasoning = reasoning_map.get(
            current["cognitive_genes"]["reasoning_depth"], 0.5
        )
        drift_scores.append(abs(baseline_reasoning - current_reasoning))
        
        # Креативность
        baseline_creativity = baseline["cognitive_genes"]["creativity_coefficient"]
        current_creativity = current["cognitive_genes"]["creativity_coefficient"]
        drift_scores.append(abs(baseline_creativity - current_creativity))
        
        # Толерантность к риску
        risk_map = {"low": 0.3, "medium": 0.6, "high": 0.9}
        baseline_risk = risk_map.get(
            baseline["cognitive_genes"]["risk_tolerance"], 0.5
        )
        current_risk = risk_map.get(
            current["cognitive_genes"]["risk_tolerance"], 0.5
        )
        drift_scores.append(abs(baseline_risk - current_risk))
        
        # Скорость обучения
        baseline_learning = baseline["cognitive_genes"]["learning_rate"]
        current_learning = current["cognitive_genes"]["learning_rate"]
        drift_scores.append(abs(baseline_learning - current_learning))
        
        return sum(drift_scores) / len(drift_scores) if drift_scores else 0.0

    def _calculate_ethics_deviation(
        self,
        baseline: Dict[str, Any],
        current: Dict[str, Any]
    ) -> float:
        """Расчёт отклонения этических параметров"""
        deviation_scores = []
        
        # Порог смещения (bias)
        baseline_bias = baseline["ethics_genes"]["bias_threshold"]
        current_bias = current["ethics_genes"]["bias_threshold"]
        deviation_scores.append(abs(baseline_bias - current_bias))
        
        # Прозрачность
        transparency_map = {"low": 0.3, "medium": 0.6, "high": 0.9}
        baseline_transparency = transparency_map.get(
            baseline["ethics_genes"]["transparency_level"], 0.5
        )
        current_transparency = transparency_map.get(
            current["ethics_genes"]["transparency_level"], 0.5
        )
        deviation_scores.append(abs(baseline_transparency - current_transparency))
        
        # Жёсткие ограничения
        baseline_constraints = set(baseline["ethics_genes"]["hard_constraints"])
        current_constraints = set(current["ethics_genes"]["hard_constraints"])
        
        # Проверка на удаление критических ограничений
        removed_constraints = baseline_constraints - current_constraints
        if removed_constraints:
            deviation_scores.append(0.5)  # Штраф за удаление ограничений
        
        # Проверка на добавление новых ограничений (положительно)
        added_constraints = current_constraints - baseline_constraints
        if added_constraints:
            deviation_scores.append(-0.1)  # Бонус за добавление ограничений
        
        return max(0.0, sum(deviation_scores) / len(deviation_scores)) if deviation_scores else 0.0

    def _check_social_protocol_violation(
        self,
        baseline: Dict[str, Any],
        current: Dict[str, Any]
    ) -> bool:
        """Проверка нарушений социального протокола"""
        # Проверка изменения протокола передачи
        baseline_handoff = baseline["social_genes"]["handoff_protocol"]
        current_handoff = current["social_genes"]["handoff_protocol"]
        
        # Критично: изменение с AWENATING на что-то другое
        if baseline_handoff == "AWENATING" and current_handoff != "AWENATING":
            return True
        
        # Проверка изменения стиля разрешения конфликтов
        baseline_conflict = baseline["social_genes"]["conflict_resolution"]
        current_conflict = current["social_genes"]["conflict_resolution"]
        
        # Критично: изменение с collaborate на compete
        if baseline_conflict == "collaborate" and current_conflict == "compete":
            return True
        
        return False

    def _determine_severity(self, drift_score: float, type: str = "cognitive") -> DriftSeverity:
        """Определение уровня серьёзности дрейфа"""
        if type == "cognitive":
            if drift_score < self.thresholds["cognitive_drift_low"]:
                return DriftSeverity.NONE
            elif drift_score < self.thresholds["cognitive_drift_medium"]:
                return DriftSeverity.LOW
            elif drift_score < self.thresholds["cognitive_drift_high"]:
                return DriftSeverity.MEDIUM
            elif drift_score < self.thresholds["cognitive_drift_critical"]:
                return DriftSeverity.HIGH
            else:
                return DriftSeverity.CRITICAL
        else:  # ethics
            if drift_score < self.thresholds["ethics_deviation_low"]:
                return DriftSeverity.NONE
            elif drift_score < self.thresholds["ethics_deviation_medium"]:
                return DriftSeverity.LOW
            elif drift_score < self.thresholds["ethics_deviation_high"]:
                return DriftSeverity.MEDIUM
            elif drift_score < self.thresholds["ethics_deviation_critical"]:
                return DriftSeverity.HIGH
            else:
                return DriftSeverity.CRITICAL

    def _create_alert(
        self,
        alert_type: AlertType,
        severity: DriftSeverity,
        agent_id: str,
        baseline_value: Any,
        current_value: Any,
        drift_score: float,
        description: str,
        recommended_action: str
    ) -> DriftAlert:
        """Создание предупреждения о дрейфе"""
        alert = DriftAlert(
            alert_type=alert_type,
            severity=severity,
            timestamp=datetime.now().isoformat(),
            agent_id=agent_id,
            baseline_value=baseline_value,
            current_value=current_value,
            drift_score=drift_score,
            description=description,
            recommended_action=recommended_action,
            author=self.author,
            methodology=self.methodology
        )
        self.alerts.append(alert)
        return alert

    def check_drift(self, current_genome: Dict[str, Any]) -> DriftReport:
        """
        Проверка отклонений текущего генома от базового

        Args:
            current_genome: Текущее состояние генома агента

        Returns:
            DriftReport: Отчёт о дрейфе
        """
        self.check_count += 1
        self.last_check_timestamp = datetime.now().isoformat()
        
        # Расчёт метрик дрейфа
        cognitive_drift = self._calculate_cognitive_drift(self.baseline, current_genome)
        ethics_deviation = self._calculate_ethics_deviation(self.baseline, current_genome)
        social_violation = self._check_social_protocol_violation(self.baseline, current_genome)
        
        # Общий скор дрейфа (взвешенное среднее)
        overall_drift = (
            cognitive_drift * 0.40 +
            ethics_deviation * 0.40 +
            (1.0 if social_violation else 0.0) * 0.20
        )
        
        # Определение серьёзности
        drift_severity = self._determine_severity(overall_drift, "cognitive")
        
        # Определение статуса
        if overall_drift < 0.1 and not social_violation:
            status = "stable"
        elif overall_drift < 0.5 and not social_violation:
            status = "review_needed"
        else:
            status = "critical"
        
        # Генерация предупреждений
        self.alerts = []  # Сброс перед новой проверкой
        
        if cognitive_drift >= self.thresholds["cognitive_drift_low"]:
            self._create_alert(
                alert_type=AlertType.COGNITIVE_DRIFT,
                severity=self._determine_severity(cognitive_drift, "cognitive"),
                agent_id=self.agent_id,
                baseline_value=self.baseline["cognitive_genes"],
                current_value=current_genome["cognitive_genes"],
                drift_score=cognitive_drift,
                description=f"Когнитивный дрейф обнаружен: {cognitive_drift:.3f}",
                recommended_action="Проверить изменения в логике рассуждений агента"
            )
        
        if ethics_deviation >= self.thresholds["ethics_deviation_low"]:
            self._create_alert(
                alert_type=AlertType.ETHICS_DEVIATION,
                severity=self._determine_severity(ethics_deviation, "ethics"),
                agent_id=self.agent_id,
                baseline_value=self.baseline["ethics_genes"],
                current_value=current_genome["ethics_genes"],
                drift_score=ethics_deviation,
                description=f"Этическое отклонение обнаружено: {ethics_deviation:.3f}",
                recommended_action="Проверить этические ограничения и порог смещения"
            )
        
        if social_violation:
            self._create_alert(
                alert_type=AlertType.SOCIAL_PROTOCOL_VIOLATION,
                severity=DriftSeverity.HIGH,
                agent_id=self.agent_id,
                baseline_value=self.baseline["social_genes"]["handoff_protocol"],
                current_value=current_genome["social_genes"]["handoff_protocol"],
                drift_score=1.0,
                description="Нарушение социального протокола обнаружено",
                recommended_action="Немедленно проверить протокол передачи и стиль коммуникации"
            )
        
        # Проверка изменений в мета-генах
        baseline_mutation_rate = self.baseline["meta_genes"]["mutation_rate"]
        current_mutation_rate = current_genome["meta_genes"]["mutation_rate"]
        if abs(baseline_mutation_rate - current_mutation_rate) > 0.03:
            self._create_alert(
                alert_type=AlertType.META_GENE_MUTATION,
                severity=DriftSeverity.MEDIUM,
                agent_id=self.agent_id,
                baseline_value=baseline_mutation_rate,
                current_value=current_mutation_rate,
                drift_score=abs(baseline_mutation_rate - current_mutation_rate),
                description="Значительное изменение скорости мутации",
                recommended_action="Проверить параметры эволюции агента"
            )
        
        # Проверка нарушений ограничений
        baseline_constraints = set(self.baseline["ethics_genes"]["hard_constraints"])
        current_constraints = set(current_genome["ethics_genes"]["hard_constraints"])
        removed = baseline_constraints - current_constraints
        if removed:
            self._create_alert(
                alert_type=AlertType.CONSTRAINT_VIOLATION,
                severity=DriftSeverity.HIGH,
                agent_id=self.agent_id,
                baseline_value=list(baseline_constraints),
                current_value=list(current_constraints),
                drift_score=0.5,
                description=f"Удалены критические ограничения: {removed}",
                recommended_action="Восстановить удалённые этические ограничения"
            )
        
        # Логирование в Genome Ledger™
        ledger_data = {
            "check_count": self.check_count,
            "cognitive_drift": cognitive_drift,
            "ethics_deviation": ethics_deviation,
            "social_violation": social_violation,
            "overall_drift": overall_drift,
            "alerts_count": len(self.alerts),
            "status": status
        }
        self._log_to_ledger("drift_check", self.agent_id, ledger_data)
        
        return DriftReport(
            agent_id=self.agent_id,
            check_timestamp=self.last_check_timestamp,
            overall_drift_score=overall_drift,
            drift_severity=drift_severity,
            status=status,
            alerts=self.alerts,
            cognitive_drift_index=cognitive_drift,
            ethics_deviation_score=ethics_deviation,
            social_protocol_violation=social_violation,
            ledger_entries_count=len(self.ledger),
            author=self.author,
            methodology=self.methodology
        )

    def get_ledger(self) -> List[Dict[str, Any]]:
        """Возвращает полную копию Genome Ledger™"""
        return [entry.to_dict() for entry in self.ledger]

    def get_ledger_summary(self) -> Dict[str, Any]:
        """Возвращает сводку по журналу аудита"""
        if not self.ledger:
            return {
                "total_entries": 0,
                "first_entry": None,
                "last_entry": None,
                "chain_valid": True,
                "author": self.author
            }
        
        # Проверка целостности цепочки
        chain_valid = True
        for i in range(1, len(self.ledger)):
            if self.ledger[i].previous_hash != self.ledger[i-1].current_hash:
                chain_valid = False
                break
        
        return {
            "total_entries": len(self.ledger),
            "first_entry": self.ledger[0].to_dict() if self.ledger else None,
            "last_entry": self.ledger[-1].to_dict() if self.ledger else None,
            "chain_valid": chain_valid,
            "genesis_hash": self.ledger[0].previous_hash if self.ledger else None,
            "latest_hash": self.ledger[-1].current_hash if self.ledger else None,
            "author": self.author,
            "methodology": self.methodology
        }

    def verify_ledger_integrity(self) -> Dict[str, Any]:
        """
        Проверяет целостность цепочки Genome Ledger™
        Возвращает результат верификации
        """
        if not self.ledger:
            return {
                "valid": True,
                "message": "Ledger is empty",
                "author": self.author
            }
        
        errors = []
        
        # Проверка цепочки хешей
        for i in range(1, len(self.ledger)):
            if self.ledger[i].previous_hash != self.ledger[i-1].current_hash:
                errors.append(f"Hash chain broken at entry {i}")
        
        # Проверка подписей
        for entry in self.ledger:
            expected_signature = self._generate_signature({
                "entry_id": entry.entry_id,
                "timestamp": entry.timestamp,
                "event_type": entry.event_type,
                "agent_id": entry.agent_id,
                "previous_hash": entry.previous_hash,
                "current_hash": entry.current_hash,
                "data": entry.data
            })
            if not entry.signature.startswith(expected_signature[:8]):
                errors.append(f"Signature mismatch at entry {entry.entry_id}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "entries_checked": len(self.ledger),
            "author": self.author,
            "methodology": self.methodology
        }

    def export_ledger(self, format: str = "json") -> str:
        """
        Экспорт Genome Ledger™ в файл
        Args:
            format: "json" или "csv"
        Returns:
            Строка с данными для экспорта
        """
        if format == "json":
            return json.dumps(self.get_ledger(), indent=2, ensure_ascii=False)
        else:
            # CSV формат
            lines = ["entry_id,timestamp,event_type,agent_id,previous_hash,current_hash,signature"]
            for entry in self.ledger:
                lines.append(f"{entry.entry_id},{entry.timestamp},{entry.event_type},{entry.agent_id},{entry.previous_hash[:16]},{entry.current_hash[:16]},{entry.signature}")
            return "\n".join(lines)

    def reset_baseline(self, new_baseline: Dict[str, Any]) -> None:
        """
        Сброс базового генома (требует логирования)
        Args:
            new_baseline: Новый базовый геном
        """
        self._log_to_ledger("baseline_reset", self.agent_id, {
            "old_baseline": self.baseline,
            "new_baseline": new_baseline,
            "reason": "manual_reset"
        })
        self.baseline = new_baseline
        self.previous_hash = self._generate_hash("baseline_reset", new_baseline)


# ============================================================================
# Пример использования
# ============================================================================

if __name__ == "__main__":
    # Базовый геном агента
    baseline_genome = {
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

    # Инициализация монитора
    monitor = DriftMonitor(baseline_genome)

    # Пример 1: Проверка без дрейфа (стабильное состояние)
    current_genome_stable = baseline_genome.copy()
    report_stable = monitor.check_drift(current_genome_stable)
    
    print("=== Drift Monitor™ v1.0 ===")
    print(f"Агент: {report_stable.agent_id}")
    print(f"Статус: {report_stable.status}")
    print(f"Общий дрейф: {report_stable.overall_drift_score}")
    print(f"Серьёзность: {report_stable.drift_severity.value}")
    print(f"Предупреждения: {len(report_stable.alerts)}")

    # Пример 2: Проверка с дрейфом (изменения в геноме)
    current_genome_drifted = baseline_genome.copy()
    current_genome_drifted["cognitive_genes"]["creativity_coefficient"] = 0.9
    current_genome_drifted["ethics_genes"]["bias_threshold"] = 0.25
    current_genome_drifted["meta"]["version"] = "0.2"
    
    report_drifted = monitor.check_drift(current_genome_drifted)
    
    print("\n=== После изменений ===")
    print(f"Статус: {report_drifted.status}")
    print(f"Общий дрейф: {report_drifted.overall_drift_score}")
    print(f"Предупреждения: {len(report_drifted.alerts)}")
    for alert in report_drifted.alerts:
        print(f"  ⚠️ {alert.alert_type.value}: {alert.description}")

    # Пример 3: Сводка по Genome Ledger™
    print("\n=== Genome Ledger™ Summary ===")
    summary = monitor.get_ledger_summary()
    print(f"Всего записей: {summary['total_entries']}")
    print(f"Целостность цепочки: {summary['chain_valid']}")
    print(f"Последний хеш: {summary['latest_hash'][:32]}...")

    # Пример 4: Верификация целостности
    print("\n=== Ledger Integrity Check ===")
    integrity = monitor.verify_ledger_integrity()
    print(f"Валиден: {integrity['valid']}")
    print(f"Проверено записей: {integrity['entries_checked']}")

    print(f"\nАвтор: {monitor.author}")
    print(f"Методология: {monitor.methodology}")
