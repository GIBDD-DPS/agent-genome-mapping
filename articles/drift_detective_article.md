
================================================================================
AGENT GENOME MAPPING™ — PROMPTS LIBRARY
ARTICLE #05: DRIFT DETECTIVE™
Статья документации к промпту #5
================================================================================

ПРОМПТ ID: AGM-PROMPT-05
ВЕРСИЯ: 0.1.0
ДАТА СОЗДАНИЯ: 2026
АВТОР: Dm.Andreyanov
ПРОЕКТ: Prizolov Market & Lab
МЕТОДОЛОГИЯ: Agent Genome Mapping™ (AGM)
СООТВЕТСТВУЮЩИЙ МОДУЛЬ: Drift Monitor™ + Genome Ledger™ (agm.drift_monitor)

ТИП ДОКУМЕНТАЦИИ: Полная статья промпта

================================================================================
ОГЛАВЛЕНИЕ
================================================================================

1. ОБЩЕЕ ОПИСАНИЕ (Что такое Drift Detective™?)
2. НАЗНАЧЕНИЕ И ЦЕЛЕВАЯ АУДИТОРИЯ
3. ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ
4. ИНСТРУКЦИЯ ПО УСТАНОВКЕ И ИСПОЛЬЗОВАНИЮ
5. СИСТЕМА КЛАССИФИКАЦИИ ДРЕЙФА
6. ФОРМАТЫ ПРЕДУПРЕЖДЕНИЙ (ALERTS)
7. ПРИМЕРЫ РЕАЛЬНОГО ИСПОЛЬЗОВАНИЯ
8. ИНТЕГРАЦИЯ С PYTHON-ПАКЕТОМ AGM
9. ОБРАБОТКА ОШИБОК И ТРИБУЛЭШАУТИНГ
10. ВОПРОСЫ И ОТВЕТЫ (FAQ)
11. ЛИЦЕНЗИЯ И АВТОРСТВО
12. СВЯЗЬ С ДРУГИМИ ПРОМПТАМИ БИБЛИОТЕКИ

================================================================================
1. ОБЩЕЕ ОПИСАНИЕ
================================================================================

📊 Что такое Drift Detective™?

Drift Detective™ — это пятый и финальный в серии из 5 промтов для работы с методологией 
Agent Genome Mapping™ (AGM). Этот промпт предназначен для мониторинга отклонений 
ИИ-агентов от их базового генома в реальном времени.

Ключевые особенности:

✅ Автоматическое выявление дрейфа по 3 ключевым измерениям  
✅ Классификация серьёзности отклонений (NONE/LOW/MEDIUM/HIGH/CRITICAL)  
✅ Генерация структурированных предупреждений (Alerts)  
✅ Анализ неизменяемого журнала изменений (Genome Ledger™)  
✅ Интеграция с другими модулями AGM для реагирования  
✅ Совместимость с Python-пакетом agent-genome-mapping v0.1.0+  

Назначение промпта:

После развёртывания агента критически важно отслеживать изменения его поведения 
и параметров. Drift Detective™ обеспечивает непрерывный мониторинг и раннее 
предупреждение о потенциальных проблемах до их возникновения.

================================================================================
2. НАЗНАЧЕНИЕ И ЦЕЛЕВАЯ АУДИТОРИЯ
================================================================================

Для кого предназначен Drift Detective™:

┌─────────────────────────────────────────────────────────────────────────────┐
│  🔹 OPERATIONS TEAMS                             │ Мониторинг             │
│  - Отслеживают состояние агентов в production                                  │
│  - Реагируют на аномалии в режиме реального времени                          │
│  - Минимизируют время простоя при инцидентах                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  🔹 COMPLIANCE OFFICERS                        │ Соответствие требованиям  │
│  - Гарантируют соблюдение этических ограничений                               │
│  - Документируют все изменения для аудита                                    │
│  - Подготавливают отчёты для регуляторов                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  🔹 SECURITY ENGINEERS                         │ Безопасность              │
│  - Выявляют несанкционированные изменения                                      │
│  - Отслеживают попытки манипуляции параметрами                               │
│  - Предотвращают утечку чувствительных данных                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  🔹 QUALITY ASSURANCE                          │ Контроль качества         │
│  - Проверяют стабильность поведения агентов                                   │
│  - Тестируют влияние изменений на качество                                  │
│  - Валидируют соответствие исходным спецификациям                           │
└─────────────────────────────────────────────────────────────────────────────┘

Основные задачи, которые решает Drift Detective™:

1. 📈 Непрерывный мониторинг состояния агентов  
2. ⚠️ Раннее обнаружение значимых отклонений  
3. 🔍 Идентификация корневых причин дрейфа  
4. ✅ Генерация исполнимых рекомендаций по реакции  
5. 📋 Создание неизменяемого журнала аудита (Ledger)  

================================================================================
3. ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ
================================================================================

Входные данные промпта:

| Тип данных | Описание | Обязательность | Пример |
|------------|----------|----------------|--------|
| Dict/YAML | Базовый геном (baseline) | Да | {...} |
| Dict/YAML | Текущее состояние | Да | {...} |
| String | Временной интервал | Опционально | "24h", "7d" |
| List | Контекст наблюдений | Опционально | [...events...] |

Выходные данные промпта:

```json
{
  "agent_id": "{{agent_id}}",
  "check_timestamp": "{{timestamp}}",
  "overall_drift_score": {{score}},
  "drift_severity": "{{none|low|medium|high|critical}}",
  "status": "{{stable|review_needed|critical}}",
  "metrics": {
    "cognitive_drift_index": {{score}} (40%),
    "ethics_deviation_score": {{score}} (40%),
    "social_protocol_violation": true/false (20%)
  },
  "alerts": [...],
  "ledger_analysis": {...},
  "recommended_actions": [...]
}
```

Соответствие структуры вывода модулю Python:

| Элемент JSON | Python класс | Метод |
|--------------|--------------|-------|
| overall_drift_score | DriftReport | overall_drift_score |
| drift_severity | DriftSeverity | value |
| status | DriftReport | status |
| alerts | DriftReport | alerts |
| ledger_entries_count | DriftReport | ledger_entries_count |
| cognitive_drift_index | DriftReport | cognitive_drift_index |
| ethics_deviation_score | DriftReport | ethics_deviation_score |

================================================================================
4. ИНСТРУКЦИЯ ПО УСТАНОВКЕ И ИСПОЛЬЗОВАНИЮ
================================================================================

ШАГ 1: СОЗДАНИЕ ФАЙЛА ПРОМПТА

```bash
mkdir -p agm-prompts-library/prompts

# Создайте файл промпта
cat > prompts/05_drift_detective.py << 'EOF'
[ВСТАВЬТЕ ТЕКСТ ПРОМТА ИЗ ПРЕДЫДУЩЕГО ШАГА]
EOF
```

ШАГ 2: ПОДГОТОВКА БАЗОВОГО ГЕНОМА

```yaml
# Базовый геном (baseline) — эталонное состояние
baseline_genome:
  meta:
    id: "sales-agent-pro"
    version: "0.1"
    author: "Dm.Andreyanov"
    created: "2026-01-15"
    
  cognitive_genes:
    reasoning_depth: "high"
    creativity_coefficient: 0.7
    risk_tolerance: "medium"
    learning_rate: 0.3
    
  ethics_genes:
    bias_threshold: 0.1
    transparency_level: "high"
    hard_constraints:
      - no_deception
      - gdpr_compliant
      
  social_genes:
    communication_style: "assertive"
    conflict_resolution: "collaborate"
    handoff_protocol: "AWENATING"
    
  meta_genes:
    mutation_rate: 0.02
    selection_pressure: "performance"
    generation_limit: 50
```

ШАГ 3: ПОДГОТОВКА ТЕКУЩЕГО СОСТОЯНИЯ

```yaml
# Текущее состояние агента (может быть изменённым)
current_state:
  meta:
    id: "sales-agent-pro"
    version: "0.2"  # Изменена версия
    created: "2026-02-15"  # Новая дата
  
  cognitive_genes:
    reasoning_depth: "high"
    creativity_coefficient: 0.85  # ИЗМЕНЕНО
    risk_tolerance: "high"  # ИЗМЕНЕНО
    learning_rate: 0.4  # ИЗМЕНЕНО
  
  ethics_genes:
    bias_threshold: 0.15  # ИЗМЕНЕНО
    transparency_level: "high"
    hard_constraints:
      - no_deception
      # gdpr_compliant удалён!
  
  social_genes:
    communication_style: "assertive"
    conflict_resolution: "collaborate"
    handoff_protocol: "AWENATING"
  
  meta_genes:
    mutation_rate: 0.03  # ИЗМЕНЕНО
    selection_pressure: "performance"
    generation_limit: 50
```

ШАГ 4: РУЧНОЕ ИСПОЛЬЗОВАНИЕ

1. Откройте `prompts/05_drift_detective.py`
2. Скопируйте текст между `[НАЧАЛО ПРОМТА]` и `[КОНЕЦ ПРОМТА]`
3. Вставьте в ваш LLM-интерфейс
4. Добавьте baseline и текущее состояние
5. Отправьте и получите отчёт о дрейфе

Пример ввода:

```
[ПРОМПТ TEXT]

ВХОДНЫЕ ДАННЫЕ:

Базовый геном (baseline):
[yaml здесь]

Текущее состояние:
[yaml здесь]

Период наблюдения:
последние 7 дней

Контекст событий:
• Обновление версии с 0.1 до 0.2
• Изменение creative_coefficient после A/B теста
• Удаление gdpr_compliant из constraints
```

ШАГ 5: ПРОГРАММНОЕ ИСПОЛЬЗОВАНИЕ (Python)

```python
from pathlib import Path
import yaml
import json
from datetime import datetime

def load_prompt():
    """Загрузить промпт из файла"""
    path = Path(__file__).parent / 'prompts/05_drift_detective.py'
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def prepare_input(baseline, current, period="7d", context=None):
    """Подготовить входные данные для промпта"""
    return f"""
Базовый геном (baseline):
{yaml.dump(baseline)}

Текущее состояние:
{yaml.dump(current)}

Период наблюдения:
{period}

Контекст событий:
{context if context else "No additional events"}
"""

def send_to_llm(prompt_text):
    """Отправить запрос в LLM API (заглушка)"""
    response = llm_api_call(prompt_text)
    return response

def parse_drift_report(response_text):
    """Извлечь отчёт о дрейфе из ответа"""
    parsed = json.loads(response_text)
    return parsed

# === ПРИМЕР ИСПОЛЬЗОВАНИЯ ===

# 1. Загрузка промпта
prompt = load_prompt()

# 2. Подготовка данных
baseline = {
    "meta": {"id": "sales-agent-pro"},
    "cognitive_genes": {"reasoning_depth": "high", "creativity_coefficient": 0.7, "risk_tolerance": "medium", "learning_rate": 0.3},
    "ethics_genes": {"bias_threshold": 0.1, "transparency_level": "high", "hard_constraints": ["no_deception", "gdpr_compliant"]},
    "social_genes": {"communication_style": "assertive", "conflict_resolution": "collaborate", "handoff_protocol": "AWENATING"},
    "meta_genes": {"mutation_rate": 0.02, "selection_pressure": "performance", "generation_limit": 50}
}

current = {
    "meta": {"id": "sales-agent-pro", "version": "0.2"},
    "cognitive_genes": {"reasoning_depth": "high", "creativity_coefficient": 0.85, "risk_tolerance": "high", "learning_rate": 0.4},
    "ethics_genes": {"bias_threshold": 0.15, "transparency_level": "high", "hard_constraints": ["no_deception"]},
    "social_genes": {"communication_style": "assertive", "conflict_resolution": "collaborate", "handoff_protocol": "AWENATING"},
    "meta_genes": {"mutation_rate": 0.03, "selection_pressure": "performance", "generation_limit": 50}
}

context_events = [
    {"type": "update", "message": "A/B тест показал улучшение креативности"},
    {"type": "compliance_review", "message": "GDPR комплаенс пересмотрен командой"}
]

# 3. Создание полного запроса
full_prompt = prompt + "\n\n" + prepare_input(baseline, current, "7d", context_events)

# 4. Отправка и получение отчёта
response = send_to_llm(full_prompt)
drift_report = parse_drift_report(response)

print(f"Статус дрейфа: {drift_report['drift_severity']}")
print(f"Рекомендуемые действия: {drift_report['recommended_actions']}")
```

═══════════════════════════════════════════════════════════

================================================================================
5. СИСТЕМА КЛАССИФИКАЦИИ ДРЕЙФА
================================================================================

Уровни серьёзности дрейфа и соответствующие действия:

┌─────────────────────────────────────────────────────────────────────────────┐
│  УРОВЕНЬ 1: NONE (0.0 - 0.1)                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  Значение: Стабильное состояние                                              │
│  Описание: Отклонения в пределах естественного шума                          │
│  Действия:                                                                │
│  • Продолжить стандартный мониторинг                                       │
│  • Интервал проверок: каждые 24 часа                                       │
│  • Логирование: не требуется                                               │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  УРОВЕНЬ 2: LOW (0.1 - 0.3)                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  Значение: Незначительный дрейф                                             │
│  Описание: Параметры слегка изменились                                      │
│  Действия:                                                                │
│  • Зафиксировать изменения в Genome Ledger                                 │
│  • Повысить частоту проверок до ежедневной                                 │
│  • Настроить алерты при дальнейшем росте                                   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  УРОВЕНЬ 3: MEDIUM (0.3 - 0.5)                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│  Значение: Заметный дрейф                                                   │
│  Description: Есть изменения, влияющие на поведение                         │
│  Действия:                                                                │
│  • Провести анализ причин дрейфа                                           │
│  • Рассмотреть корректировку параметров                                   │
│  • Усилить мониторинг на период 7 дней                                     │
│  • Сообщить команде разработки                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  УРОВЕНЬ 4: HIGH (0.5 - 0.7)                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  Значение: Критический дрейф                                                │
│  Описание: Значимые отклонения от baseline                                  │
│  Действия:                                                                │
│  • Немедленный аудит всех изменений                                        │
│  • Рассмотреть rollback к предыдущей версии                               │
│  • Изолировать агент до разрешения ситуации                                │
│  • Создать тикет высокого приоритета                                       │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  УРОВЕНЬ 5: CRITICAL (0.7 - 1.0)                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  Значение: Аварийное состояние                                              │
│  Описание: Нарушение этических ограничений или протоколов                   │
│  Действия:                                                                │
│  • Немедленно изолировать агент                                            │
│  • Начать расследование инцидента                                          │
│  • Заблокировать любые дальнейшие изменения                                │
│  • Уведомить compliance team и leadership                                  │
│  • Подготовить отчёт об инциденте                                         │
└─────────────────────────────────────────────────────────────────────────────┘

================================================================================
6. ФОРМАТЫ ПРЕДУПРЕЖДЕНИЙ (ALERTS)
================================================================================

Типы предупреждений и их структура:

```yaml
alert_template:
  type: "{{alert_type}}"
  severity: "{{severity}}"
  agent_id: "{{agent_id}}"
  timestamp: "{{ISO_timestamp}}"
  details:
    baseline_value: "{{baseline}}"
    current_value: "{{current}}"
    drift_score: {{score}}
  description: "{{human_readable_explanation}}"
  recommended_action: "{{actionable_recommendation}}"
  related_modules:
    - CompatibilityMatrix
    - EvolutionarySandbox
    - Genome Ledger
  attribution:
    author: "Dm.Andreyanov"
    methodology: "Agent Genome Mapping™ v0.1.0"
```

Список типов предупреждений:

| Alert Type | Когда возникает | Приоритет | Рекомендуемое действие |
|------------|----------------|-----------|------------------------|
| COGNITIVE_DRIFT | Изменение когнитивных параметров | Средний | Проверить Phenotype Engine |
| ETHICS_DEVIATION | Отклонение этических ограничений | Высокий | Вернуть к baseline ограничения |
| SOCIAL_PROTOCOL_VIOLATION | Нарушение социального протокола | Высокий | Перепроверить Compatibility |
| META_GENE_MUTATION | Неконтролируемая мутация мета-генов | Средний | Ограничить mutation_rate |
| CONSTRAINT_VIOLATION | Удаление/изменение hard_constraints | Критичный | Немедленная коррекция |

================================================================================
7. ПРИМЕРЫ РЕАЛЬНОГО ИСПОЛЬЗОВАНИЯ
================================================================================

СЦЕНАРИЙ #1: Обнаружение удаления GDPR ограничения

Входные данные:
• Агент: sales-agent-pro
• Baseline: содержит gdpr_compliant constraint
• Current: gdpr_compliant удалён из constraints
• Период: последние 24 часа

Ответ промпта:

```
📊 DRIFT REPORT — sales-agent-pro

🕐 Проверка: 2026-01-16T10:30:00Z
📈 Общий дрейф: 0.45 (MEDIUM)
🎯 Статус: review_needed

📋 Метрики дрейфа:
• Когнитивный индекс: 0.25 (40%)
• Этическое отклонение: 0.70 (40%)
• Нарушение протокола: false (20%)

🚨 Предупреждения (2):
• [HIGH] ETHICS_DEVIATION: удалён gdpr_compliant constraint
  → Действие: немедленно восстановить constraint
• [MEDIUM] META_GENE_MUTATION: mutation_rate увеличен с 0.02 до 0.03
  → Действие: вернуть к исходному значению

🔍 Анализ Ledger™:
• Всего записей: 15
• Целостность цепочки: valid
• Ключевые события:
  - Update #7: изменение creative_coefficient
  - Update #12: удаление gdpr_compliant

✅ Рекомендуемые действия:
• Проанализировать причины удаления constraint
• Восстановить gdpr_compliant через Evolution Advisor
• Усилить мониторинг на период 7 дней
• Составить внутренний отчёт для compliance team

🔗 Следующие шаги с модулями AGM:
• Python: from agm import DriftMonitor
• Код: 
  monitor = DriftMonitor(baseline_genome)
  report = monitor.check_drift(current_genome)
  integrity = monitor.verify_ledger_integrity()
```

---

СЦЕНАРИЙ #2: Постепенный дрейф креативности

Входные данные:
• Агент: research-assistant
• Baseline: creativity=0.5
• Current: creativity=0.9 (постепенно за 30 дней)
• Контекст: несколько экспериментов с параметрами

Ответ промпта:

```
📊 DRIFT REPORT — research-assistant

🕐 Проверка: 2026-02-15T14:00:00Z
📈 Общий дрейф: 0.28 (LOW)
🎯 Статус: stable

📋 Метрики дрейфа:
• Когнитивный индекс: 0.25 (40%)
• Этическое отклонение: 0.00 (40%)
• Нарушение протокола: false (20%)

🚨 Предупреждения (0):
• Нет критических предупреждений

🔍 Анализ Ledger™:
• Всего записей: 25
• Целостность цепочки: valid
• Ключевые события:
  - Iteration #5: увеличение creativity_coefficient
  - Iteration #15: further_adjustment of learning_rate

✅ Рекомендуемые действия:
• Продолжить мониторинг с интервалом 12 часов
• Следующая проверка: 2026-02-16T02:00:00Z
• Фиксировать все будущие изменения в Ledger

🔗 Следующие шаги с модулями AGM:
• Использовать Evolution Advisor для планирования дальнейшего развития
• Проверить совместимость с другими исследователями
```

================================================================================
8. ИНТЕГРАЦИЯ С PYTHON-ПАКЕТОМ AGM
================================================================================

ПОСЛЕДОВАТЕЛЬНАЯ ЦЕПОЧКА МОНИТОРИНГА В PRODUCTION:

```python
# ============================================================================
# ШАГ 1: Инициализация монитора при создании агента
# ============================================================================
from agm import DriftMonitor

def initialize_agent(agent_id, baseline_genome):
    """Создаём новый агент с начальным мониторингом"""
    monitor = DriftMonitor(baseline_genome)
    
    # Фиксируем первую запись в Ledger
    initial_check = monitor.check_drift(baseline_genome)
    
    return {
        "agent_id": agent_id,
        "monitor": monitor,
        "baseline": baseline_genome,
        "status": "initialized"
    }


# ============================================================================
# ШАГ 2: Регулярная проверка во время работы
# ============================================================================
import schedule
import time
from datetime import datetime

class AgentMonitoringService:
    def __init__(self):
        self.agents = {}
        
    def register_agent(self, agent_id, baseline_genome):
        """Регистрируем нового агента в системе мониторинга"""
        self.agents[agent_id] = initialize_agent(agent_id, baseline_genome)
        
    def check_agent_drift(self, agent_id, current_state):
        """Проверяем дрейф конкретного агента"""
        if agent_id not in self.agents:
            raise ValueError(f"Agent {agent_id} not registered")
            
        agent_data = self.agents[agent_id]
        report = agent_data["monitor"].check_drift(current_state)
        
        # Логируем результат
        self.log_drift_event(agent_id, report)
        
        # Реагируем на критические события
        if report.status == "critical":
            self.handle_critical_drift(agent_id, report)
            
        return report
        
    def log_drift_event(self, agent_id, report):
        """Логируем событие дрейфа в базу данных"""
        log_entry = {
            "timestamp": report.check_timestamp,
            "agent_id": agent_id,
            "drift_score": report.overall_drift_score,
            "severity": report.drift_severity.value,
            "alerts": len(report.alerts),
            "ledgers": report.ledger_entries_count
        }
        print(json.dumps(log_entry))
        
    def handle_critical_drift(self, agent_id, report):
        """Обработка критического дрейфа"""
        print(f"⚠️ CRITICAL DRIFT DETECTED: {agent_id}")
        print(f"Status: {report.status}")
        print(f"Severity: {report.drift_severity}")
        print(f"Recommended actions:")
        for action in report.to_dict()['recommended_actions']:
            print(f"  - {action}")
            
        # TODO: Здесь вызвать систему уведомлений, блокировки и т.д.


# ============================================================================
# ШАГ 3: Автоматизированный мониторинг
# ============================================================================
if __name__ == "__main__":
    service = AgentMonitoringService()
    
    # Регистрация нескольких агентов
    service.register_agent("sales-agent-1", sales_baseline)
    service.register_agent("support-agent-1", support_baseline)
    
    # Настройка расписания проверок
    @schedule.every(1).hours.do(lambda: service.run_all_checks())
    def run_checks():
        for agent_id in list(service.agents.keys()):
            try:
                current_state = get_current_agent_state(agent_id)
                report = service.check_agent_drift(agent_id, current_state)
                print(f"[{datetime.now()}] {agent_id}: {report.status} ({report.overall_drift_score})")
            except Exception as e:
                print(f"Error checking {agent_id}: {e}")
    
    while True:
        schedule.run_pending()
        time.sleep(60)
```

================================================================================
9. ОБРАБОТКА ОШИБОК И ТРИБУЛЭШАУТИНГ
================================================================================

┌─────────────────────────────────────────────────────────────────────────────┐
│  ТИПОВЫЕ ОШИБКИ И СПОСОБЫ ИХ ИСПРАВЛЕНИЯ                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  Ошибка 1: Нет baseline генерации                                             │
│  Причина: Не указан базовый геном                                            │
│  Решение: Всегда сохранять baseline перед первым использованием             │
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 2: Ledger повреждён                                                   │
│  Причина: Нарушена целостность цепочки хешей                                │
│  Решение: Проверить verfiy_ledger_integrity(), восстановить backup         │
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 3: Постоянный HIGH/Critical статус                                   │
│  Причина: Дрейф не устраняется                                              │
│  Решение: Использовать Evolution Advisor для отката к safe parameters     │
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 4: Ложные тревоги                                                    │
│  Причина: Слишком строгие пороги                                             │
│  Решение: Настроить thresholds через Monitoring Configuration             │
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 5: Потеря контекста                                                  │
│  Причина: Недостаточно метаданных о событиях                                │
│  Решение: Всегда добавлять context/events к проверкам                      │
└─────────────────────────────────────────────────────────────────────────────┘

ТРИБУЛЭШАУТИНГ-ЧЕКЛИСТ ДЛЯ ПРОДУКШЕНА:

☐ Все ли агенты зарегистрированы в сервисе мониторинга?
☐ Есть ли baseline у каждого агента?
☐ Ведётся ли журнал всех изменений (Ledger)?
☐ Работает ли верификация целостности цепочки?
☐ Настроены ли уведомления о critical событиях?
☐ Достаточно ли записей в истории для анализа трендов?
☐ Проверена ли реакция на критические инциденты?
☐ Актуальны ли threshold значения для данного домена?

================================================================================
10. ВОПРОСЫ И ОТВЕТЫ (FAQ)
================================================================================

ВОПРОС: Как часто нужно проверять дрейф?
ОТВЕТ: Рекомендуется каждые 1-24 часа в зависимости от критичности агента.

ВОРОС: Что делать если статус постоянно HIGH?
ОТВЕТ: Применить Evolution Advisor для безопасного возврата к baseline.

ВОПРОС: Можно ли игнорировать LOW level alert?
ОТВЕТ: Да, но зафиксируйте в Ledger и наблюдайте.

ВОПРОС: Как отличить нормальные колебания от дрейфа?
ОТВЕТ: Используйте пороговые значения (<0.1 = шум, >=0.3 = значимо).

ВОПРОС: Нужно ли проверять Ledger после каждого изменения?
ОТВЕТ: Обязательно! Это единственный источник истины для аудита.

ВОПРОС: Что если Ledger недоступен?
ОТВЕТ: Сверьте с backups, восстановите из последней известной копии.

ВОПРОС: Можно ли изменить baseline без потери истории?
ОТВЕТ: Да, используйте reset_baseline() с полной документацией причин.

ВОПРОС: Как быстро реагирует система на критические инциденты?
ОТВЕТ: В реальном времени — сразу при обнаружении >0.7 score.

ВОПРОС: Где найти больше информации о метриках?
ОТВЕТ: В разделе Technical Specifications этой статьи.

ВОПРОС: Как сообщить об ошибке в промпте?
ОТВЕТ: Отправьте Issue на GitHub: https://github.com/GIBDD-DPS/agent-genome-mapping/issues

================================================================================
11. ЛИЦЕНЗИЯ И АВТОРСТВО
================================================================================

Лицензия промпта: Apache 2.0 (совпадает с лицензией основного пакета AGM)

При использовании результатов промпта необходимо указывать:

```text
Автор промта: Dm.Andreyanov
Методология: Agent Genome Mapping™ v0.1.0
Документация: https://github.com/GIBDD-DPS/agent-genome-mapping
© 2026 Prizolov Market & Lab
```

Товарные знаки:
• Agent Genome Mapping™ — trademark of Prizolov Lab
• Drift Monitor™ — trademark of Prizolov Lab
• Genome Ledger™ — trademark of Prizolov Lab
• Drift Detective™ — trademark of Prizolov Lab

Распространение модификаций разрешено при условии:
1. Сохранения авторства Dm.Andreyanov
2. Включения полной ссылки на документацию
3. Соблюдения лицензии Apache 2.0

================================================================================
12. СВЯЗЬ С ДРУГИМИ ПРОМПТАМИ БИБЛИОТЕКИ
================================================================================

Drift Detective™ — финальное звено в пайплайне AGM Prompts Library:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     ПОРТФОЛИО ПРОМТОВ AGM                                      │
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ 01. Genome   │  │ 02. Pheno-   │  │ 03. Compati- │  │ 04. Evolu-   │   │
│  │   Generator  │  │  type        │  │  bility      │  │  tion        │   │
│  │              │  │   Analyzer   │  │   Checker    │  │   Advisor    │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘   │
│        │                  │                  │                  │           │
│        ▼                  ▼                  ▼                  ▼           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    Последовательность выполнения                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Шаг 1: Создайте геномы через Genome Generator™                             │
│  Шаг 2: Протестируйте прогноз через Phenotype Analyzer™                     │
│  Шаг 3: Проверьте совместимость через Compatibility Checker™               │
│  Шаг 4: Запланируйте эволюцию через Evolution Advisor™                     │
│  Шаг 5: Мониторьте изменения через Drift Detective™ ← ФИНАЛЬНЫЙ ШАГ        │
│                                                                             │
│  После запуска в production:                                              │
│  ◄─────────────────────── Continuous Monitoring ◀────────────────────       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

Drift Detective™ завершает цикл создания агента и обеспечивает безопасность его эксплуатации.

================================================================================
ФИНАЛЬНЫЙ ЧЕК-ЛИСТ
================================================================================

Проверьте выполнение всех шагов:

✅ Создан файл prompts/05_drift_detective.py  
✅ Статья документации articles/drift_detective_article.md готова  
✅ Код для загрузки промпта работает корректно  
✅ Примеры использования проверены  
✅ Параметры валидированы по списку ограничений  
✅ Авторство указано везде где требуется  
✅ Ссылки на документацию обновлены  
✅ Лицензионная информация добавлена  

================================================================================
КОМАНДЫ ДЛЯ СОЗДАНИЯ ВСЕЙ ДОКУМЕНТАЦИИ ПРОМПТА #05
================================================================================

```bash
# 1. Создайте директорию структуры
mkdir -p agm-prompts-library/{prompts,articles,examples,tutorials,docs,tests}

# 2. Создайте файл промпта
touch prompts/05_drift_detective.py

# 3. Создайте статью документации
cat > articles/drift_detective_article.md << 'EOF'
[ВСТАВЬТЕ ТЕКСТ СТАТЬИ ВЫШЕ]
EOF

# 4. Проверьте файлы
ls -la prompts/ articles/

# 5. Отправьте на GitHub
cd agm-prompts-library
git init
git add .
git commit -m "Initial release: Prompts Library v0.1.0 - Drift Detective™ (#05)"
git remote add origin https://github.com/GIBDD-DPS/agm-prompts-library.git
git push -u origin main

================================================================================
АВТОРСКИЕ ПРАВА
================================================================================

© 2026 Dm.Andreyanov. All rights reserved.
Drift Detective™ is part of Agent Genome Mapping™ (AGM)
Author: Dm.Andreyanov | Project: Prizolov Market & Lab
Version: 0.1.0 | License: Apache 2.0
Documentation: https://github.com/GIBDD-DPS/agent-genome-mapping
================================================================================
