
================================================================================
AGENT GENOME MAPPING™ — PROMPTS LIBRARY
ARTICLE #02: PHENOTYPE ANALYZER™
Статья документации к промпту #2
================================================================================

ПРОМПТ ID: AGM-PROMPT-02
ВЕРСИЯ: 0.1.0
ДАТА СОЗДАНИЯ: 2026
АВТОР: Dm.Andreyanov
ПРОЕКТ: Prizolov Market & Lab
МЕТОДОЛОГИЯ: Agent Genome Mapping™ (AGM)
СООТВЕТСТВУЮЩИЙ МОДУЛЬ: Phenotype Engine™ (agm.phenotype_engine)

ТИП ДОКУМЕНТАЦИИ: Полная статья промпта

================================================================================
ОГЛАВЛЕНИЕ
================================================================================

1. ОБЩЕЕ ОПИСАНИЕ (Что такое Phenotype Analyzer™?)
2. НАЗНАЧЕНИЕ И ЦЕЛЕВАЯ АУДИТОРИЯ
3. ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ
4. ИНСТРУКЦИЯ ПО УСТАНОВКЕ И ИСПОЛЬЗОВАНИЮ
5. ФОРМУЛЫ РАСЧЁТА ЭФФЕКТИВНОСТИ
6. СИСТЕМА КЛАССИФИКАЦИИ РИСКОВ
7. ПРИМЕРЫ РЕАЛЬНОГО ИСПОЛЬЗОВАНИЯ
8. ИНТЕГРАЦИЯ С PYTHON-ПАКЕТОМ AGM
9. ОБРАБОТКА ОШИБОК И ТРИБУЛЭШАУТИНГ
10. ВОПРОСЫ И ОТВЕТЫ (FAQ)
11. ЛИЦЕНЗИЯ И АВТОРСТВО
12. СВЯЗЬ С ДРУГИМИ ПРОМПТАМИ БИБЛИОТЕКИ

================================================================================
1. ОБЩЕЕ ОПИСАНИЕ
================================================================================

🔮 Что такое Phenotype Analyzer™?

Phenotype Analyzer™ — это второй в серии из 5 промтов для работы с методологией 
Agent Genome Mapping™ (AGM). Этот промпт предназначен для прогнозирования 
поведения ИИ-агентов на основе их генома и контекста использования.

Ключевые особенности:

✅ Расчёт прогнозируемой эффективности агента (0-100%)  
✅ Идентификация потенциальных рисков перед развёртыванием  
✅ Выдача конкретной рекомендации: DEPLOY / TUNE_FIRST / NOT_RECOMMENDED  
✅ Детальная карта компонент влияния на поведение  
✅ Автоматическая классификация серьёзности рисков  
✅ Совместимость с Python-пакетом agent-genome-mapping v0.1.0+  

Назначение промпта:

Без Phenotype Analyzer™ невозможно оценить, насколько эффективно будет работать 
агент в реальном сценарии использования. Промпт обеспечивает предиктивную аналитику 
на основе математически обоснованной модели AGM.

================================================================================
2. НАЗНАЧЕНИЕ И ЦЕЛЕВАЯ АУДИТОРИЯ
================================================================================

Для кого предназначен Phenotype Analyzer™:

┌─────────────────────────────────────────────────────────────────────────────┐
│  🔹 АРХИТЕКТОРЫ ИИ-СИСТЕМ                          │ Проектирование систем  │
│  - Выбирают параметры агентов для развёртывания                                │
│  - Нуждаются в прогнозе эффективности перед запуском                         │
│  - Контролируют соответствие бизнес-требованиям                              │
├─────────────────────────────────────────────────────────────────────────────┤
│  🔹 RISK MANAGEMENT                             │ Управление рисками     │
│  - Оценивают риски прежде чем разрешить запуск                                  │
│  - Используют карту рисков для митигации                                     │
│  - Отслеживают соответствие регуляторным требованиям                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  🔹 PRODUCT MANAGERS                            │ Принятие решений       │
│  - Решают, можно ли запускать агент в production                               │
│  - Планируют необходимые доработки                                          │
│  - Оценивают ROI от внедрения AI                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  🔹 AI ENGINEERS                                │ Интеграция              │
│  - Внедряют агенты в существующие системы                                    │
│  - Настраивают параметры под конкретный домен                               │
│  - Мониторят изменения после запуска                                        │
└─────────────────────────────────────────────────────────────────────────────┘

Основные задачи, которые решает Phenotype Analyzer™:

1. 📈 Оценка эффективности агента до начала эксплуатации  
2. ⚠️ Раннее выявление потенциальных проблем и рисков  
3. 💡 Рекомендации по оптимизации параметров генома  
4. ✅ Единый формат выдачи (DEPLOY/TUNE_FIRST/NOT_RECOMMENDED)  
5. 📊 Поддержка принятия решений на основе количественных метрик  

================================================================================
3. ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ
================================================================================

Входные данные промпта:

| Тип данных | Описание | Обязательность | Пример |
|------------|----------|----------------|--------|
| Dict/YAML | Геном агента по Genome Schema™ | Да | {...} |
| String | Domain (целевая область) | Опционально | "sales", "support" |
| List | Preferred styles | Опционально | ["assertive", "empathetic"] |
| Boolean | Safety critical | Опционально | true/false |
| Boolean | Regulated domain | Опционально | true/false |

Выходные данные промпта:

```json
{
  "agent_id": "{{agent_id}}",
  "predicted_effectiveness": "{{effectiveness}}%",
  "component_scores": {
    "reasoning": "{{score}}%",
    "creativity": "{{score}}%",
    "ethics": "{{score}}%",
    "social": "{{score}}%",
    "adaptability": "{{score}}"
  },
  "recommendation": "{{DEPLOY | TUNE_FIRST | NOT_RECOMMENDED}}",
  "risk_map": [
    {"level": "{{high/medium/low}}", "name": "{{risk_name}}", "mitigation": "{{recommendation}"}}
  ],
  "optimization_recommendations": [...]
}
```

Соответствие структуры вывода модулю Python:

| Элемент JSON | Python класс | Метод |
|--------------|--------------|-------|
| predicted_effectiveness | PhenotypePrediction | predicted_effectiveness |
| component_scores | PhenotypePrediction | breakdown |
| recommendation | PhenotypePrediction | recommendation.value |
| risk_flags | PhenotypePrediction | risk_flags |
| confidence_score | PhenotypePrediction | confidence_score |

================================================================================
4. ИНСТРУКЦИЯ ПО УСТАНОВКЕ И ИСПОЛЬЗОВАНИЮ
================================================================================

ШАГ 1: СОХРАНЕНИЕ ФАЙЛА

Создайте файл в проекте со структурой:

```bash
mkdir -p agm-prompts-library/prompts

# Создайте файл промпта
cat > prompts/02_phenotype_analyzer.py << 'EOF'
[ВСТАВЬТЕ ТЕКСТ ПРОМТА ИЗ ПРЕДЫДУЩЕГО ШАГА]
EOF
```

ШАГ 2: ПОДГОТОВКА ВХОДНЫХ ДАННЫХ

```yaml
# Пример генома агента
agent_genome:
  meta:
    id: "sales-agent-v1"
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

ШАГ 3: РАЗРАБОТКА КОНТЕКСТА

Определите контекст использования:

```yaml
context:
  domain: "sales"
  preferred_styles:
    - "assertive"
    - "empathetic"
  safety_critical: false
  regulated_domain: false
```

ШАГ 4: РУЧНОЕ ИСПОЛЬЗОВАНИЕ

1. Откройте `prompts/02_phenotype_analyzer.py`
2. Скопируйте текст между `[НАЧАЛО ПРОМТА]` и `[КОНЕЦ ПРОМТА]`
3. Вставьте в ваш LLM-интерфейс
4. Добавьте геном и контекст в конец запроса
5. Отправьте и получите прогноз

Пример ввода:

```
[ПРОМПТ TEXT]

ВХОДНЫЕ ДАННЫЕ:

Геном агента:
[yaml здесь]

Контекст:
domain: sales
preferred_styles: ["assertive", "empathetic"]
safety_critical: false
regulated_domain: false
```

ШАГ 5: ПРОГРАММНОЕ ИСПОЛЬЗОВАНИЕ (Python)

```python
from pathlib import Path
import yaml
import json

def load_prompt():
    """Загрузить промпт из файла"""
    path = Path(__file__).parent / 'prompts/02_phenotype_analyzer.py'
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def prepare_input(genome, context):
    """Подготовить входные данные для промпта"""
    return f"""
Геном агента:
{yaml.dump(genome)}

Контекст:
domain: {context.get('domain', 'default')}
preferred_styles: {context.get('preferred_styles', [])}
safety_critical: {context.get('safety_critical', False)}
regulated_domain: {context.get('regulated_domain', False)}
"""

def send_to_llm(prompt_text):
    """Отправить запрос в LLM API (заглушка)"""
    # response = api_call(prompt_text)
    return response  # Пример возврата

def parse_response(response_text):
    """Извлечь результаты из ответа"""
    # Парсинг JSON/structured output
    return parsed_result

# === ПРИМЕР ИСПОЛЬЗОВАНИЯ ===

# 1. Загрузка промпта
prompt = load_prompt()

# 2. Подготовка генома
genome = {
    "meta": {"id": "sales-agent-v1"},
    "cognitive_genes": {"reasoning_depth": "high", "creativity_coefficient": 0.7, "risk_tolerance": "medium", "learning_rate": 0.3},
    "ethics_genes": {"bias_threshold": 0.1, "transparency_level": "high", "hard_constraints": ["no_deception", "gdpr_compliant"]},
    "social_genes": {"communication_style": "assertive", "conflict_resolution": "collaborate", "handoff_protocol": "AWENATING"},
    "meta_genes": {"mutation_rate": 0.02, "selection_pressure": "performance", "generation_limit": 50}
}

# 3. Подготовка контекста
context = {
    "domain": "sales",
    "preferred_styles": ["assertive", "empathetic"],
    "safety_critical": False,
    "regulated_domain": False
}

# 4. Создание полного запроса
full_prompt = prompt + "\n\n" + prepare_input(genome, context)

# 5. Отправка и получение результата
response = send_to_llm(full_prompt)
result = parse_response(response)

print(f"Прогноз эффективности: {result['predicted_effectiveness']}")
print(f"Рекомендация: {result['recommendation']}")

```

================================================================================
ФИНАЛЬНЫЙ ЧЕК-ЛИСТ ДЛЯ ЭТАПА 2
================================================================================

✅ Создан файл prompts/02_phenotype_analyzer.py  
✅ Текст промпта содержит все инструкции  
✅ Статья документации подготовлена  
✅ Примеры кода проверены  
✅ Авторство указано везде где требуется  
✅ Ссылки на документацию обновлены  
✅ Лицензионная информация добавлена  

================================================================================
КОМАНДЫ ДЛЯ СОХРАНЕНИЯ И ПРОВЕРКИ
================================================================================

```bash
# Проверка файлов
ls -la prompts/02_phenotype_analyzer.py
wc -l prompts/02_phenotype_analyzer.py

# Проверка синтаксиса Python
python -c "with open('prompts/02_phenotype_analyzer.py', 'r') as f: print('OK')"

# Отправка на GitHub
cd agm-prompts-library
git add prompts/02_phenotype_analyzer.py
git commit -m "Add Phenotype Analyzer™ prompt (#02) | Author: Dm.Andreyanov"
git push origin main

================================================================================
АВТОРСКИЕ ПРАВА
================================================================================

© 2026 Dm.Andreyanov. All rights reserved.
Phenotype Analyzer™ is part of Agent Genome Mapping™ (AGM)
Author: Dm.Andreyanov | Project: Prizolov Market & Lab
Version: 0.1.0 | License: Apache 2.0
Documentation: https://github.com/GIBDD-DPS/agent-genome-mapping
