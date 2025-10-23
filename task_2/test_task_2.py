import pytest
from types import GeneratorType
from task_2.task_2 import generator_numbers, sum_profit


# ---------- generator_numbers ----------

def test_generator_numbers_returns_generator():
    text = "100.5 200 300.75"
    gen = generator_numbers(text)
    assert isinstance(gen, GeneratorType)


def test_generator_numbers_extracts_floats_correctly():
    text = "Дохід: 1000.01 і бонус 27.45 а також 324.00"
    result = list(generator_numbers(text))
    assert result == [1000.01, 27.45, 324.00]


def test_generator_numbers_handles_integers_and_floats():
    text = "50 100.5 25 0.5"
    result = list(generator_numbers(text))
    assert result == [50.0, 100.5, 25.0, 0.5]


def test_generator_numbers_ignores_text_without_numbers():
    text = "немає жодного числа тут"
    result = list(generator_numbers(text))
    assert result == []


def test_generator_numbers_ignores_numbers_with_letters():
    text = "100a 200 3b.5 400.25"
    result = list(generator_numbers(text))
    assert result == [200.0, 400.25]


# ---------- sum_profit ----------

def test_sum_profit_correct_sum():
    text = "Основний дохід 1000.01 додатково 27.45 і 324.00"
    total = sum_profit(text, generator_numbers)
    assert round(total, 2) == 1351.46


def test_sum_profit_with_integers():
    text = "100 200 300"
    assert sum_profit(text, generator_numbers) == 600.0


def test_sum_profit_with_empty_text():
    text = "тут немає чисел"
    assert sum_profit(text, generator_numbers) == 0.0


def test_sum_profit_with_mixed_content():
    text = "зарплата 500.5 бонус 99 податок 25.5"
    total = sum_profit(text, generator_numbers)
    assert total == pytest.approx(625.0, rel=1e-5)


# ---------- Технічні перевірки ----------

def test_generator_numbers_yields_incrementally():
    text = "10 20 30"
    gen = generator_numbers(text)
    assert next(gen) == 10.0
    assert next(gen) == 20.0
    assert next(gen) == 30.0
    with pytest.raises(StopIteration):
        next(gen)


def test_sum_profit_accepts_custom_generator():
    def custom_gen(text):
        for n in [1.1, 2.2, 3.3]:
            yield n

    text = "неважливо"
    assert sum_profit(text, custom_gen) == pytest.approx(6.6, rel=1e-5)
