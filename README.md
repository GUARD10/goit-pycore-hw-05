## 🤖 AI Usage Disclaimer / Дісклеймер щодо використання ШІ

🇬🇧 **Note:** Artificial Intelligence (AI) was used **only** for writing this README file and for general consultation and documentation.  
All source code, algorithms, and logic were **written and designed by the author**.

🇺🇦 **Примітка:** Штучний інтелект (AI) використовувався **лише** для створення цього README-файлу та отримання консультацій й оформлення.  
Увесь код, алгоритми та логіка були **написані й продумані автором**.

---

# 🧠 GOIT Python Core — Homework #5
### Functional Programming & Built-in Python Modules
*(English & Ukrainian bilingual README)*

---

## 🌐 Quick Links
- [🇬🇧 English Version](#-english-version)
- [🇺🇦 Українська Версія](#-українська-версія)

---

---

## 🇬🇧 English Version

### 📘 Overview
This project contains implementations for **Homework #5** of the GOIT Python Core course.  
It focuses on **functional programming concepts**, **recursion**, **closures**, **generators**, and **decorators**.

The repository is structured into four tasks, each located in its own folder.

---

### 🗂 Project Structure
```
📦 goit-pycore-hw-05
┣━━ .gitignore
┣━━ README.md
┣━━ task_1
┃   ┣━━ __init__.py
┃   ┣━━ task_1.py
┃   ┗━━ test_task_1.py
┣━━ task_2
┃   ┣━━ __init__.py
┃   ┣━━ task_2.py
┃   ┗━━ test_task_2.py
┣━━ task_3
┃   ┣━━ __init__.py
┃   ┣━━ task_3.py
┃   ┣━━ test_logfile.log
┃   ┗━━ test_task_3.py
┗━━ task_4
    ┣━━ __init__.py
    ┣━━ task_4_command_handlers.py
    ┣━━ task_4_custom_exceptions.py
    ┣━━ task_4_main.py
    ┗━━ test_task_4.py
```

---

### 🧩 Task 1 — Caching Fibonacci Numbers

**Goal:** Implement recursive Fibonacci computation with **memoization using a closure**.

**File:** `task_1/task_1.py`

**Functionality:**
- `caching_fibonacci()` returns an inner function `fibonacci(n)` that uses a cache.
- Repeated calls with the same `n` are retrieved from memory instead of recalculated.

**Example:**
```
from task_1.task_1 import caching_fibonacci

fib = caching_fibonacci()
print(fib(10))  # ➜ 55
print(fib(15))  # ➜ 610
```

---

### 🧮 Task 2 — Income Sum Generator

**Goal:** Extract valid numbers from a text using a **generator** and calculate the total profit.

**File:** `task_2/task_2.py`

**Functions:**
- `generator_numbers(text: str)` → yields numbers found in the text.
- `sum_profit(text: str, func: Callable)` → sums all numbers from the generator.

**Example:**
```
from task_2.task_2 import generator_numbers, sum_profit

text = "The total income includes 1000.01 base, 27.45 bonus, and 324.00 extra."
print(sum_profit(text, generator_numbers))  # ➜ 1351.46
```

---

### 🧾 Task 3 — Log File Analyzer

**Goal:** Parse a log file and show statistics for each log level (INFO, ERROR, DEBUG, etc.).

**File:** `task_3/task_3.py`

**Functions:**
- `parse_log_line(line: str) -> dict`
- `load_logs(file_path: str) -> list`
- `filter_logs_by_level(logs: list, level: str) -> list`
- `count_logs_by_level(logs: list) -> dict`
- `display_log_counts(counts: dict)`

**Usage:**
```
python task_3/task_3.py path/to/logfile.log
python task_3/task_3.py path/to/logfile.log error
```

**Example output:**
```
Log Level | Count
-----------|-------
INFO       | 4
DEBUG      | 3
ERROR      | 2
WARNING    | 1
```

---

### 🤖 Task 4 — Console Assistant Bot with Decorator Error Handling

**Goal:** Improve a command-line contact bot by adding **error-handling decorators**.

**Files:**
- `task_4/task_4_main.py` — main script
- `task_4/task_4_command_handlers.py` — command logic
- `task_4/task_4_custom_exceptions.py` — custom exceptions
- `task_4/test_task_4.py` — tests

**Key concept:**  
The decorator `@input_error` wraps handler functions and catches `KeyError`, `ValueError`, `IndexError`, returning user-friendly messages instead of crashing.

**Example:**
```
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
```

---

### 🧪 Tests
Each task includes a `test_task_X.py` file with unit tests.  
To run all tests:
```
pytest
```

---

### 🧰 Requirements
- Python 3.10+
- No external dependencies required.

---

### 👨‍💻 Author
Project completed as part of the **GOIT Python Core Course (Homework #5)**.

---

---

## 🇺🇦 Українська Версія

### 📘 Опис
Цей проєкт містить реалізацію **Домашньої роботи №5** курсу **GOIT Python Core**.  
Основна мета — освоїти **функціональне програмування**, **рекурсію**, **замикання**, **генератори** та **декоратори**.

---

### 🗂 Структура проєкту
```
📦 goit-pycore-hw-05
┣━━ .gitignore
┣━━ README.md
┣━━ task_1
┃   ┣━━ __init__.py
┃   ┣━━ task_1.py
┃   ┗━━ test_task_1.py
┣━━ task_2
┃   ┣━━ __init__.py
┃   ┣━━ task_2.py
┃   ┗━━ test_task_2.py
┣━━ task_3
┃   ┣━━ __init__.py
┃   ┣━━ task_3.py
┃   ┣━━ test_logfile.log
┃   ┗━━ test_task_3.py
┗━━ task_4
    ┣━━ __init__.py
    ┣━━ task_4_command_handlers.py
    ┣━━ task_4_custom_exceptions.py
    ┣━━ task_4_main.py
    ┗━━ test_task_4.py
```

---

### 🧩 Завдання 1 — Кешування чисел Фібоначчі

**Мета:** Реалізувати рекурсивне обчислення чисел Фібоначчі з **кешуванням через замикання**.

**Файл:** `task_1/task_1.py`

**Приклад:**
```
from task_1.task_1 import caching_fibonacci

fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))  # 610
```

---

### 🧮 Завдання 2 — Генератор чисел доходу

**Мета:** Знайти всі дійсні числа у тексті за допомогою **генератора** і обчислити загальний прибуток.

**Файл:** `task_2/task_2.py`

**Приклад:**
```
from task_2.task_2 import generator_numbers, sum_profit

text = "Загальний дохід: 1000.01 основний, 27.45 бонус і 324.00 додатково."
print(sum_profit(text, generator_numbers))  # 1351.46
```

---

### 🧾 Завдання 3 — Аналізатор лог-файлів

**Мета:** Створити скрипт для читання логів, підрахунку записів за рівнем логування та фільтрації за рівнем.

**Файл:** `task_3/task_3.py`

**Приклади запуску:**
```
python task_3/task_3.py path/to/logfile.log
python task_3/task_3.py path/to/logfile.log error
```

**Приклад виводу:**
```
Рівень логування | Кількість
-----------------|-----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1
```

---

### 🤖 Завдання 4 — Консольний бот із декораторами для обробки помилок

**Мета:** Додати декоратор `@input_error`, який обробляє помилки введення користувача (KeyError, ValueError, IndexError).

**Файли:**
- `task_4/task_4_main.py` — головна логіка
- `task_4/task_4_command_handlers.py` — команди
- `task_4/task_4_custom_exceptions.py` — винятки
- `task_4/test_task_4.py` — тести

**Приклад декоратора:**
```
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
    return inner
```

---

### 🧪 Тести
У кожній папці є файл з тестами `test_task_X.py`.  
Для запуску:
```
pytest
```

---

### ⚙️ Вимоги
- Python 3.10+
- Без зовнішніх бібліотек

---

### ✍️ Автор
Проєкт виконано в рамках курсу **GOIT Python Core (Домашня робота №5)**.
