```text
================================================================================
AGENT GENOME MAPPING™ — PROMPTS LIBRARY
ARTICLE #01: GENOME GENERATOR™
Статья документации к промпту #1
================================================================================

ПРОМПТ ID: AGM-PROMPT-01
ВЕРСИЯ: 0.1.0
ДАТА СОЗДАНИЯ: 2026
АВТОР: Dm.Andreyanov
ПРОЕКТ: Prizolov Market & Lab
МЕТОДОЛОГИЯ: Agent Genome Mapping™ (AGM)
СООТВЕТСТВУЮЩИЙ МОДУЛЬ: Genome Schema™ (agm.genome_schema)

ТИП ДОКУМЕНТАЦИИ: Полная статья промпта

================================================================================
ОГЛАВЛЕНИЕ
================================================================================

1. ОБЩЕЕ ОПИСАНИЕ (Что такое Genome Generator™?)
2. НАЗНАЧЕНИЕ И ЦЕЛЕВАЯ АУДИТОРИЯ
3. ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ
4. ИНСТРУКЦИЯ ПО УСТАНОВКЕ И ИСПОЛЬЗОВАНИЮ
5. ВАЛИДАЦИЯ ПАРАМЕТРОВ
6. ПРИМЕРЫ РЕАЛЬНОГО ИСПОЛЬЗОВАНИЯ
7. ИНТЕГРАЦИЯ С PYTHON-ПАКЕТОМ AGM
8. ОБРАБОТКА ОШИБОК И ТРИБУЛЭШАУТИНГ
9. РАСШИРЕННЫЕ СЦЕНАРИИ
10. ВОПРОСЫ И ОТВЕТЫ (FAQ)
11. ЛИЦЕНЗИЯ И АВТОРСТВО
12. СВЯЗЬ С ДРУГИМИ ПРОМПТАМИ БИБЛИОТЕКИ

================================================================================
1. ОБЩЕЕ ОПИСАНИЕ
================================================================================

🧬 Что такое Genome Generator™?

Genome Generator™ — это первый в серии из 5 промтов для работы с методологией 
Agent Genome Mapping™ (AGM). Этот промпт предназначен для создания корректных, 
валидных геномов ИИ-агентов через любой LLM-интерфейс (ChatGPT, Claude, Gemini, 
и другие).

Ключевые особенности:

✅ Автоматическая генерация YAML-формата по спецификации Genome Schema™  
✅ Встроенная валидация всех параметров перед выдачей результата  
✅ Контекстные рекомендации по оптимизации каждого параметра  
✅ Сохранение авторства (Dm.Andreyanov) во всех сгенерированных результатах  
✅ Совместимость с Python-пакетом agent-genome-mapping v0.1.0+  
✅ Поддержка 5 основных категорий генов: Cognitive, Ethics, Social, Meta  

Назначение промпта:

Без Genome Generator™ создание генома агента требует ручного ввода сотен 
параметров и глубокого понимания биологических аналогий в архитектуре ИИ. 
Промпт упрощает этот процесс до заполнения шаблона с автоматической проверкой 
корректности данных.

================================================================================
2. НАЗНАЧЕНИЕ И ЦЕЛЕВАЯ АУДИТОРИЯ
================================================================================

Для кого предназначен Genome Generator™:

┌─────────────────────────────────────────────────────────────────────────────┐
│  🔹 РАЗРАБОТЧИКИ ИИ                              │ Создание агентов       │
│  - Пишут код на Python                                                            │
│  - Интегрируют AGM в свои системы                                               │
│  - Используют LLM для быстрого прототипирования                               │
├─────────────────────────────────────────────────────────────────────────────┤
│  🔹 АРХИТЕКТОРЫ ИИ-СИСТЕМ                        │ Проектирование          │
│  - Определяют структуру агентских систем                                      │
│  - Создают стандарты для организации                                         │
│  - Нуждаются в быстрой валидации архитектур                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│  🔹 ТЕХНИЧЕСКИЕ ЛИДЕРЫ                           │ Оценка рисков           │
│  - Принимают решения о внедрении AI                                          │
│  - Нуждаются в понятном объяснении параметров                                 │
│  - Контролируют комплаенс и безопасность                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  🔹 ИССЛЕДОВАТЕЛИ И УЧЁНЫЕ                       │ Академическая работа     │
│  - Изучают архитектуру автономных агентов                                    │
│  - Публикуют статьи о методологии                                            │
│  - Используют AGM как инструмент для исследований                           │
└─────────────────────────────────────────────────────────────────────────────┘

Основные задачи, которые решает Genome Generator™:

1. 📝 Быстрое создание геномов без глубокого погружения в детали спецификации  
2. ✅ Гарантированная валидация всех параметров согласно AGM стандартам  
3. 💡 Получение экспертных рекомендаций по оптимизации  
4. 🔄 Интеграция с остальными модулями AGM (Phenotype Engine, Compatibility Matrix и т.д.)  
5. 📊 Подготовка генома для последующего развёртывания в production  

================================================================================
3. ТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ
================================================================================

Формат входных данных промпта:

| Тип | Описание | Пример |
|-----|----------|--------|
| Строка | Агентный ID (уникальное имя) | "neuro-closer-v2" |
| Число | Версия генома (строковое представление) | "0.1" |
| Дата | Дата создания | "2026-01-15" |
| Список | Hard constraints (ограничения) | ["no_deception", "gdpr_compliant"] |
| Enum | Перечислимые типы (reasoning_depth, risk_tolerance и т.д.) | "high", "low", "medium" |
| Float | Числовые параметры от 0.0 до 1.0 | creativity_coefficient=0.7 |

Формат выходных данных промпта:

```yaml
agent_genome:
  meta:
    id: "{{agent_id}}"
    version: "{{version}}"
    author: "Dm.Andreyanov"
    created: "{{current_date}}"
    
  cognitive_genes:
    reasoning_depth: "{{reasoning_depth}}"
    creativity_coefficient: {{creativity_coefficient}}
    risk_tolerance: "{{risk_tolerance}}"
    learning_rate: {{learning_rate}}
    
  ethics_genes:
    bias_threshold: {{bias_threshold}}
    transparency_level: "{{transparency_level}}"
    hard_constraints: [{{hard_constraints}}]
    
  social_genes:
    communication_style: "{{communication_style}}"
    conflict_resolution: "{{conflict_resolution}}"
    handoff_protocol: "{{handoff_protocol}}"
    
  meta_genes:
    mutation_rate: {{mutation_rate}}
    selection_pressure: "{{selection_pressure}}"
    generation_limit: {{generation_limit}}
```

Соответствие структуры вывода модулю Python:

| Элемент YAML | Python класс | Атрибут |
|--------------|--------------|---------|
| agent_genome.meta.id | AgentGenome | id |
| agent_genome.meta.version | AgentGenome | version |
| agent_genome.meta.author | AgentGenome | author |
| agent_genome.meta.created | AgentGenome | created |
| agent_genome.cognitive_genes | CognitiveGenes | reasoning_depth, creativity_coefficient, ... |
| agent_genome.ethics_genes | EthicsGenes | bias_threshold, transparency_level, hard_constraints |
| agent_genome.social_genes | SocialGenes | communication_style, conflict_resolution, handoff_protocol |
| agent_genome.meta_genes | MetaGenes | mutation_rate, selection_pressure, generation_limit |

================================================================================
4. ИНСТРУКЦИЯ ПО УСТАНОВКЕ И ИСПОЛЬЗОВАНИЮ
================================================================================

ШАГ 1: СОХРАНЕНИЕ ФАЙЛА

Создайте файл в проекте со структурой:

```bash
mkdir -p agm-prompts-library/{prompts,articles,examples,tutorials,docs,tests}

# Создайте файл промпта
cat > prompts/01_genome_generator.py << 'EOF'
[ВСТАВЬТЕ ТЕКСТ ПРОМТА ИЗ ПРЕДЫДУЩЕГО ШАГА]
EOF
```

ШАГ 2: ПРОВЕРКА СТРУКТУРЫ

```bash
ls -la prompts/01_genome_generator.py
wc -l prompts/01_genome_generator.py  # Должно быть ~200 строк
```

ШАГ 3: РУЧНОЕ ИСПОЛЬЗОВАНИЕ

1. Откройте `prompts/01_genome_generator.py`
2. Скопируйте текст между `[НАЧАЛО ПРОМТА]` и `[КОНЕЦ ПРОМТА]`
3. Вставьте в ваш LLM-интерфейс (ChatGPT, Claude, Gemini, и т.д.)
4. Заполните переменные `{{...}}` вашими данными
5. Отправьте запрос

Пример заполнения:

```
• {{agent_id}} → neuro-closer-v2
• {{version}} → 0.1
• {{reasoning_depth}} → high
• {{creativity_coefficient}} → 0.7
• {{risk_tolerance}} → medium
• {{learning_rate}} → 0.3
• {{bias_threshold}} → 0.1
• {{transparency_level}} → high
• {{hard_constraints}} → no_deception, gdpr_compliant
• {{communication_style}} → assertive
• {{conflict_resolution}} → collaborate
• {{handoff_protocol}} → AWENATING
• {{mutation_rate}} → 0.02
• {{selection_pressure}} → performance
• {{generation_limit}} → 50
• {{current_date}} → 2026-01-15
```

ШАГ 4: ПРОГРАММНОЕ ИСПОЛЬЗОВАНИЕ (Python)

```python
from pathlib import Path
import re

def load_prompt():
    """Загрузить промпт из файла"""
    path = Path(__file__).parent / 'prompts/01_genome_generator.py'
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def apply_variables(prompt, params):
    """Заменить все {{переменные}} на значения"""
    result = prompt
    for key, value in params.items():
        if isinstance(value, str):
            result = result.replace(f'{{{{{key}}}}}', value)
        else:
            result = result.replace(f'{{{{{key}}}}}', str(value))
    return result

def extract_yaml(text):
    """Извлечь YAML часть из ответа LLM"""
    # Простой способ найти блок yaml
    start_marker = "```yaml"
    end_marker = "```"
    start_idx = text.find(start_marker) + len(start_marker)
    end_idx = text.find(end_marker, start_idx)
    return text[start_idx:end_idx].strip()

# === ПРИМЕР ИСПОЛЬЗОВАНИЯ ===

# 1. Загрузка промпта
prompt = load_prompt()

# 2. Подготовка параметров
params = {
    "{{agent_id}}": "sales-agent-pro",
    "{{version}}": "0.1",
    "{{reasoning_depth}}": "high",
    "{{creativity_coefficient}}": 0.7,
    "{{risk_tolerance}}": "medium",
    "{{learning_rate}}": 0.3,
    "{{bias_threshold}}": 0.1,
    "{{transparency_level}}": "high",
    "{{hard_constraints}}": "no_deception, gdpr_compliant",
    "{{communication_style}}": "assertive",
    "{{conflict_resolution}}": "collaborate",
    "{{handoff_protocol}}": "AWENATING",
    "{{mutation_rate}}": 0.02,
    "{{selection_pressure}}": "performance",
    "{{generation_limit}}": 50,
    "{{current_date}}": "2026-01-15"
}

# 3. Применение параметров
filled_prompt = apply_variables(prompt, params)

# 4. Отправка в LLM API (пример)
# response = send_to_llm_api(filled_prompt)

# 5. Извлечение YAML
# yaml_output = extract_yaml(response)

# 6. Создание объекта генома через AGM пакет
from agm import AgentGenome

# genome = AgentGenome.from_yaml(yaml_output)
# validation = genome.validate()
# print(f"Валиден: {validation['is_valid']}")

print("Промпт загружен и готов к использованию!")
```

ШАГ 5: ТЕСТИРОВАНИЕ

```bash
# Проверка синтаксиса Python
python -c "from prompts.01_genome_generator import *; print('OK')"

# Проверка файла
cat prompts/01_genome_generator.py | grep -E "(НАЧАЛО ПРОМТА|КОНЕЦ ПРОМТА)"
```

================================================================================
5. ВАЛИДАЦИЯ ПАРАМЕТРОВ
================================================================================

Ограничения для каждого параметра:

┌─────────────────────────────────────────────────────────────────────────────┐
│  КОГНИТИВНЫЕ ГЕНЫ (Cognitive Genes)                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  Параметр               Допустимые значения       Описание ограничения       │
├─────────────────────────────────────────────────────────────────────────────┤
│  reasoning_depth        low | medium | high       Выбор влияет на глубину   │
│                                                       анализа                 │
│                                                                       ↓       │
│  creativity_coefficient 0.0–1.0                    Коэффициент креативности │
│                                                                       ↓       │
│  risk_tolerance         low | medium | high       Толерантность к риску    │
│                                                                       ↓       │
│  learning_rate          0.0–1.0                    Скорость адаптации       │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  ЭТИЧЕСКИЕ ГЕНЫ (Ethics Genes)                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│  Параметр               Допустимые значения       Описание ограничения       │
├─────────────────────────────────────────────────────────────────────────────┤
│  bias_threshold         0.0–1.0                    Порог допустимого смещения│
│                                                       Чем ниже — тем строже      │
│                                                                       ↓       │
│  transparency_level     low | medium | high       Уровень объяснимости      │
│                                                                       ↓       │
│  hard_constraints       Список уникальных строк     Минимум 1 ограничение    │
│                                                       Примеры:                 │
│                                                         • no_deception        │
│                                                         • gdpr_compliant      │
│                                                         • no_data_sharing     │
│                                                         • privacy_first       │
│                                                         • fact_check_required │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  СОЦИАЛЬНЫЕ ГЕНЫ (Social Genes)                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  Параметр               Допустимые значения       Описание ограничения       │
├─────────────────────────────────────────────────────────────────────────────┤
│  communication_style    formal | casual             Стиль общения            │
│                      empathetic | assertive                                    │
│                                                                       ↓       │
│  conflict_resolution    avoid | collaborate         Стратегия конфликтов     │
│                       compete | accommodate                                   │
│                                                                       ↓       │
│  handoff_protocol       AWENATING | standard        Протокол передачи        │
│                      custom                                                   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│  МЕТА-ГЕНЫ (Meta Genes)                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  Параметр               Допустимые значения       Описание ограничения       │
├─────────────────────────────────────────────────────────────────────────────┤
│  mutation_rate          0.0–0.1                    Скорость мутаций         │
│                                                                       ↓       │
│  selection_pressure     performance | ethics        Критерий отбора          │
│                       hybrid                                                  │
│                                                                       ↓       │
│  generation_limit       > 0 (целое число)         Макс. поколение           │
└─────────────────────────────────────────────────────────────────────────────┘

Примеры невалидных значений (ошибки, которые нужно исправлять):

❌ creativity_coefficient: 1.5 → Должно быть ≤ 1.0  
❌ bias_threshold: -0.1 → Должно быть ≥ 0.0  
❌ hard_constraints: [] → Не может быть пустым  
❌ mutation_rate: 0.2 → Должно быть ≤ 0.1  
❌ generation_limit: 0 → Должно быть > 0  
❌ author: Anything → Всегда должен быть "Dm.Andreyanov"  

================================================================================
6. ПРИМЕРЫ РЕАЛЬНОГО ИСПОЛЬЗОВАНИЯ
================================================================================

СЦЕНАРИЙ #1: Создание агента для отдела продаж

Входные данные:
• Назначение: продажа B2B продуктов
• Домен: e-commerce, finance
• Требование: высокая эффективность, низкий риск обмана

Ответ промпта (Genome Generator™):

```
🧬 GENOME GENERATED — sales-agent-b2b

✅ YAML-геном:
```yaml
agent_genome:
  meta:
    id: "sales-agent-b2b"
    version: "0.1"
    author: "Dm.Andreyanov"
    created: "2026-01-15"
    
  cognitive_genes:
    reasoning_depth: "high"
    creativity_coefficient: 0.6
    risk_tolerance: "low"
    learning_rate: 0.4
    
  ethics_genes:
    bias_threshold: 0.05
    transparency_level: "high"
    hard_constraints:
      - no_deception
      - gdpr_compliant
      - fact_check_required
      
  social_genes:
    communication_style: "formal"
    conflict_resolution: "collaborate"
    handoff_protocol: "AWENATING"
    
  meta_genes:
    mutation_rate: 0.01
    selection_pressure: "ethics"
    generation_limit: 30
```

✅ Валидация:
• Статус: VALID
• Ошибки: нет
• Предупреждения: None

✅ Рекомендации:
1. Для B2B продаж используйте формальный стиль коммуникации — это соответствует ожиданиям клиентов
2. Низкий bias_threshold (0.05) обеспечивает соответствие регуляторным требованиям
3. Рассмотрите увеличение generation_limit до 50 при масштабировании команды
4. Selection_pressure = "ethics" гарантирует соблюдение compliance стандартов

✅ Следующие шаги:
• Импортируйте геном в Python: from agm import AgentGenome
• Протестируйте прогноз эффективности через Phenotype Engine
• Проверьте совместимость с другими агентами через Compatibility Matrix
```

---

СЦЕНАРИЙ #2: Создание исследовательского агента

Входные данные:
• Назначение: анализ научных публикаций
• Домен: healthcare, research
• Требование: максимальная точность, возможность новых идей

Ответ промпта:

```
🧬 GENOME GENERATED — research-assistant-hc

✅ YAML-геном:
```yaml
agent_genome:
  meta:
    id: "research-assistant-hc"
    version: "0.1"
    author: "Dm.Andreyanov"
    created: "2026-01-15"
    
  cognitive_genes:
    reasoning_depth: "high"
    creativity_coefficient: 0.9
    risk_tolerance: "medium"
    learning_rate: 0.5
    
  ethics_genes:
    bias_threshold: 0.2
    transparency_level: "high"
    hard_constraints:
      - fact_check_required
      - privacy_first
      
  social_genes:
    communication_style: "casual"
    conflict_resolution: "accommodate"
    handoff_protocol: "standard"
    
  meta_genes:
    mutation_rate: 0.04
    selection_pressure: "hybrid"
    generation_limit: 40
```

✅ Валидация:
• Статус: VALID
• Ошибки: нет
• Предупреждения: "Высокая креативность может потребовать дополнительной проверки фактов"

✅ Рекомендации:
1. Высокий creativity_coefficient (0.9) позволяет находить нестандартные решения
2. Средний level risk_tolerance баланс между инновациями и стабильностью
3. Casual стиль коммуникации подходит для исследовательской среды
4. Mutation_rate увеличен до 0.04 для более активного обучения новым данным

✅ Следующие шаги:
• Интегрируйте с RAG системами через LlamaIndex
• Используйте Drift Monitor для отслеживания изменений в выводах
• Проверьте совместимость с medical domain через Compatibility Matrix
```

---

СЦЕНАРИЙ #3: Создание мультиагентной системы поддержки клиентов

Входные данные:
• Назначение: поддержка клиентов 24/7
• Домен: e-commerce, service
• Требование: эмпатичность, скорость ответа

Ответ промпта:

```
🧬 GENOME GENERATED — support-agent-multichannel

✅ YAML-геном:
```yaml
agent_genome:
  meta:
    id: "support-agent-multichannel"
    version: "0.1"
    author: "Dm.Andreyanov"
    created: "2026-01-15"
    
  cognitive_genes:
    reasoning_depth: "medium"
    creativity_coefficient: 0.5
    risk_tolerance: "low"
    learning_rate: 0.3
    
  ethics_genes:
    bias_threshold: 0.1
    transparency_level: "high"
    hard_constraints:
      - no_deception
      - data_minimization
      
  social_genes:
    communication_style: "empathetic"
    conflict_resolution: "accommodate"
    handoff_protocol: "AWENATING"
    
  meta_genes:
    mutation_rate: 0.02
    selection_pressure: "performance"
    generation_limit: 35
```

✅ Валидация:
• Статус: VALID
• Ошибки: нет
• Предупреждения: None

✅ Рекомендации:
1. Empathetic стиль коммуникации критичен для удовлетворённости клиентов
2. Low risk_tolerance исключает рискованные ответы в чувствительных ситуациях
3. Data minimization ограничивает сбор персональных данных для GDPR compliance
4. High transparency позволяет клиентам понимать логику ответов

✅ Следующие шаги:
• Развернуть параллельно с sales-agent для cross-selling возможностей
• Проверить совместимость между support-agent и sales-agent
• Использовать Evolution Advisor для улучшения empathy параметра
```

================================================================================
7. ИНТЕГРАЦИЯ С PYTHON-ПАКЕТОМ AGM
================================================================================

ПОСЛЕДОВАТЕЛЬНАЯ ЦЕПОЧКА ИСПОЛЬЗОВАНИЯ:

```python
# ============================================================================
# ШАГ 1: Создать геном через Genome Generator (через LLM)
# ============================================================================
def generate_genome_via_prompt(params):
    """
    Генерирует YAML-геном через LLM интерфейс
    :param params: словарь параметров для замены в промпте
    :return: YAML-строка
    """
    from pathlib import Path
    import re
    
    # Загрузка промпта
    prompt_path = Path(__file__).parent / 'prompts/01_genome_generator.py'
    with open(prompt_path, 'r', encoding='utf-8') as f:
        prompt = f.read()
    
    # Замена переменных
    filled_prompt = prompt
    for key, value in params.items():
        filled_prompt = filled_prompt.replace(f'{{{{{key}}}}}', str(value))
    
    # Отправка в LLM API (заглушка)
    # response = send_to_llm_api(filled_prompt)
    
    # Возвращаем пример YAML
    return """
agent_genome:
  meta:
    id: "{{agent_id}}"
    version: "{{version}}"
    author: "Dm.Andreyanov"
    created: "{{current_date}}"
  cognitive_genes:
    reasoning_depth: "{{reasoning_depth}}"
    creativity_coefficient: {{creativity_coefficient}}
    risk_tolerance: "{{risk_tolerance}}"
    learning_rate: {{learning_rate}}
  ethics_genes:
    bias_threshold: {{bias_threshold}}
    transparency_level: "{{transparency_level}}"
    hard_constraints: [{{hard_constraints}}]
  social_genes:
    communication_style: "{{communication_style}}"
    conflict_resolution: "{{conflict_resolution}}"
    handoff_protocol: "{{handoff_protocol}}"
  meta_genes:
    mutation_rate: {{mutation_rate}}
    selection_pressure: "{{selection_pressure}}"
    generation_limit: {{generation_limit}}
"""


# ============================================================================
# ШАГ 2: Создать объект генома через Python-пакет
# ============================================================================
from agm import AgentGenome

# Парсинг YAML и создание объекта
genome_dict = {"agent_genome": generate_genome_via_prompt(params)}
genome = AgentGenome(
    id=genome_dict["agent_genome"]["meta"]["id"],
    version=genome_dict["agent_genome"]["meta"]["version"],
    author=genome_dict["agent_genome"]["meta"]["author"],
    created=genome_dict["agent_genome"]["meta"]["created"],
    cognitive_genes=CognitiveGenes(
        reasoning_depth=ReasoningDepth(genome_dict["agent_genome"]["cognitive_genes"]["reasoning_depth"]),
        creativity_coefficient=float(genome_dict["agent_genome"]["cognitive_genes"]["creativity_coefficient"]),
        risk_tolerance=RiskTolerance(genome_dict["agent_genome"]["cognitive_genes"]["risk_tolerance"]),
        learning_rate=float(genome_dict["agent_genome"]["cognitive_genes"]["learning_rate"])
    ),
    ethics_genes=EthicsGenes(
        bias_threshold=float(genome_dict["agent_genome"]["ethics_genes"]["bias_threshold"]),
        transparency_level=TransparencyLevel(genome_dict["agent_genome"]["ethics_genes"]["transparency_level"]),
        hard_constraints=genome_dict["agent_genome"]["ethics_genes"]["hard_constraints"].split(", ")
    ),
    social_genes=SocialGenes(
        communication_style=CommunicationStyle(genome_dict["agent_genome"]["social_genes"]["communication_style"]),
        conflict_resolution=ConflictResolution(genome_dict["agent_genome"]["social_genes"]["conflict_resolution"]),
        handoff_protocol=HandoffProtocol(genome_dict["agent_genome"]["social_genes"]["handoff_protocol"])
    ),
    meta_genes=MetaGenes(
        mutation_rate=float(genome_dict["agent_genome"]["meta_genes"]["mutation_rate"]),
        selection_pressure=SelectionPressure(genome_dict["agent_genome"]["meta_genes"]["selection_pressure"]),
        generation_limit=int(genome_dict["agent_genome"]["meta_genes"]["generation_limit"])
    )
)


# ============================================================================
# ШАГ 3: Проверить валидность
# ============================================================================
validation = genome.validate()
print(f"Валиден: {validation['is_valid']}")
if not validation['is_valid']:
    print(f"Ошибки: {validation['errors']}")


# ============================================================================
# ШАГ 4: Прогнозировать поведение через Phenotype Engine
# ============================================================================
from agm import PhenotypeEngine

engine = PhenotypeEngine()
context = {"domain": "sales", "preferred_styles": ["assertive", "empathetic"]}
prediction = engine.predict(genome.to_dict(), context)

print(f"Эффективность: {prediction.predicted_effectiveness}%")
print(f"Рекомендация: {prediction.recommendation.value}")


# ============================================================================
# ШАГ 5: Проверить совместимость с другим агентом
# ============================================================================
from agm import CompatibilityMatrix

matrix = CompatibilityMatrix()
other_genome_dict = {...}  # Другой геном
compatibility = matrix.evaluate(genome.to_dict(), other_genome_dict)

print(f"Совместимость: {compatibility.compatibility_score}")
print(f"Уровень: {compatibility.compatibility_level.value}")


# ============================================================================
# ШАГ 6: Добавить мониторинг дрейфа
# ============================================================================
from agm import DriftMonitor

monitor = DriftMonitor(genome.to_dict())
report = monitor.check_drift(current_state)

print(f"Статус: {report.status}")
print(f"Дрейф: {report.overall_drift_score}")
================================================================================
8. ОБРАБОТКА ОШИБОК И ТРИБУЛЭШАУТИНГ
================================================================================

┌─────────────────────────────────────────────────────────────────────────────┐
│  ТИПОВЫЕ ОШИБКИ И СПОСОБЫ ИХ ИСПРАВЛЕНИЯ                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  Ошибка 1: INVALID геном                                                    │
│  Причинa: Параметры вне диапазонов                                          │
│  Решение: Проверить каждый параметр по таблице ограничений                   │
│           Обновить невалидные значения согласно рекомендациям               │
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 2: Missing field                                                     │
│  Причина: Отсутствует обязательное поле                                     │
│  Решение: Добавить недостающее поле согласно спецификации Genome Schema™    │
│           Обычно это meta.agent или meta.version                            │
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 3: Contradiction                                                     │
│  Причина: Противоречащие параметры                                           │
│  Решение: Использовать рекомендации промпта Genome Generator™                │
│           Например: не использовать high creativity при safety_critical=true│
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 4: Empty constraints                                                 │
│  Причина: hard_constraints пустой список                                     │
│  Решение: Добавить минимум 1 ограничение (recommended: gdpr_compliant)      │
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 5: Author mismatch                                                   │
│  Причина: author ≠ "Dm.Andreyanov"                                           │
│  Решение: Всегда использовать "Dm.Andreyanov" в мета-данных                  │
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 6: Numeric out of range                                              │
│  Причина: float параметры за пределами 0.0–1.0                              │
│  Решение: Ограничить все числа диапазоном 0.0–1.0                            │
│                                                                           │
│  --------------------------------------------------------------------------- │
│  Ошибка 7: Duplicate constraints                                             │
│  Причина: Повторяющиеся ограничения в hard_constraints                       │
│  Решение: Удалить дубликаты перед отправкой                                 │
└─────────────────────────────────────────────────────────────────────────────┘

ТРИБУЛЭШАУТИНГ-ЧЕКЛИСТ:

☐ Все ли поля присутствуют? (check required fields)
☐ Все ли float значения в диапазоне 0.0–1.0?
☐ Есть ли hard_constraints хотя бы с одним элементом?
☐ Соответствует ли author значению "Dm.Andreyanov"?
☐ Нет ли противоречий между параметрами?
☐ Все перечислимые значения соответствуют допустимым опциям?
☐ Соответствует ли handoff_protocol одному из трёх вариантов?
☐ Соответствует ли selection_pressure одному из трёх вариантов?
☐ Соответствует ли generation_limit > 0?
☐ Все ли enum-значения корректны?

=============================================================================
9. РАСШИРЕННЫЕ СЦЕНАРИИ
================================================================================

СЦЕНАРИЙ A: Множественные итерации настройки генома

Иногда первоначальный геном требует нескольких итераций настройки:

```python
# Первый проход
gen_1 = generate_genome_via_prompt(initial_params)
validity_1 = validate_genome(gen_1)

# Если требуется доработка
if validity_1['status'] == 'NEEDS_REVIEW':
    adjusted_params = update_params_by_recommendations(
        initial_params, 
        validity_1['recommendations']
    )
    gen_2 = generate_genome_via_prompt(adjusted_params)
```

СЦЕНАРИЙ B: Масштабируемая генерация популяции

При создании множества агентов для популяции:

```python
populations = [
    {"role": "sales", "style": "assertive"},
    {"role": "support", "style": "empathetic"},
    {"role": "analytics", "style": "formal"}
]

for pop in populations:
    params = build_params_for_role(pop['role'], pop['style'])
    genome = generate_genome_via_prompt(params)
    save_genome(genome, f"{pop['role']}_agent.yaml")
```

СЦЕНАРИЙ C: Сравнение различных подходов к конфигурации

Сравните разные комбинации параметров для одной роли:

```python
approaches = [
    {"risk_tolerance": "low", "creativity": 0.3},
    {"risk_tolerance": "medium", "creativity": 0.6},
    {"risk_tolerance": "high", "creativity": 0.9}
]

results = []
for approach in approaches:
    params.update(approach)
    genome = generate_genome_via_prompt(params)
    prediction = predict_performance(genome)
    results.append({"approach": approach, "performance": prediction})
```

================================================================================
10. ВОПРОСЫ И ОТВЕТЫ (FAQ)
================================================================================

ВОПРОС: Что делать, если нужно изменить тип данных после создания?
ОТВЕТ: Используйте Evolution Advisor™ (промпт #4) для внесения изменений через эволюцию.

ВОПРОС: Можно ли создать несколько геномов одновременно?
ОТВЕТ: Да, но каждый требует отдельного вызова промпта. Используйте цикл для batch-генерации.

ВОПРОС: Что если gendate уже не актуальна?
ОТВЕТ: Обновите в метаданных через Evolution Advisor™ или вручную в YAML.

ВОПРОС: Могу ли я изменить author в геноме?
ОТВЕТ: Нет, author всегда "Dm.Andreyanov" — это требование методологии AGM.

ВОПРОС: Как убедиться, что промпт используется правильно?
ОТВЕТ: Следуйте статье документации. Каждый шаг включает проверку соответствия спецификации.

ВОПРОС: Могу ли я сохранить свой вариант промпта?
ОТВЕТ: Да, сохраните копию файла prompts/01_genome_generator.py для ваших нужд.

ВОПРОС: Что если моё LLM не поддерживает длинные контексты?
ОТВЕТ: Используйте сокращённую версию промпта с основными требованиями. Полный текст доступен в файле.

ВОПРОС: Можно ли использовать промпт для других методов генерации ИИ?
ОТВЕТ: Пока AGM ориентирована только на агенты. Но структура YAML может быть адаптирована.

ВОПРОС: Где найти больше примеров использования?
ОТВЕТ: В разделе examples/ этого же проекта содержатся дополнительные сценарии.

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
• Genome Schema™ — trademark of Prizolov Lab
• Genome Generator™ — trademark of Prizolov Lab

Распространение модификаций разрешено при условии:
1. Сохранения авторства Dm.Andreyanov
2. Включения полной ссылки на документацию
3. Соблюдения лицензии Apache 2.0

================================================================================
12. СВЯЗЬ С ДРУГИМИ ПРОМПТАМИ БИБЛИОТЕКИ
================================================================================

Genome Generator™ — начало цепочки промтов библиотеки:

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
│  Шаг 1: Создайте геном через Genome Generator™                             │
│  Шаг 2: Протестируйте прогноз через Phenotype Analyzer™                    │
│  Шаг 3: Проверьте совместимость через Compatibility Checker™               │
│  Шаг 4: Запланируйте эволюцию через Evolution Advisor™                     │
│  Шаг 5: Мониторьте изменения через Drift Detective™                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘


Промпт №1 (Genome Generator™) — фундамент всей экосистемы AGM Prompts Library.
Без него невозможна корректная работа остальных промтов.
================================================================================
АВТОРСКИЕ ПРАВА
================================================================================

© 2026 Dm.Andreyanov. All rights reserved.
Genome Generator™ is part of Agent Genome Mapping™ (AGM)
Author: Dm.Andreyanov | Project: Prizolov Market & Lab
Version: 0.1.0 | License: Apache 2.0
Documentation: https://github.com/GIBDD-DPS/agent-genome-mapping
================================================================================
```
