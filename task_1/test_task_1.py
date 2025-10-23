import pytest
import inspect
import time

from types import FunctionType
from task_1.task_1 import caching_fibonacci


# ---------- FIXTURE ----------

@pytest.fixture
def fib_func():
    return caching_fibonacci()


# ---------- BASIC EXAMPLES ----------

def test_returns_function():
    result = caching_fibonacci()
    assert isinstance(result, FunctionType)
    assert callable(result)


def test_fibonacci_base_cases(fib_func):
    assert fib_func(0) == 0
    assert fib_func(1) == 1


def test_fibonacci_small_numbers(fib_func):
    assert fib_func(2) == 1
    assert fib_func(3) == 2
    assert fib_func(4) == 3
    assert fib_func(5) == 5


def test_fibonacci_medium_numbers(fib_func):
    assert fib_func(10) == 55
    assert fib_func(15) == 610
    assert fib_func(20) == 6765


# ---------- EXCEPTIONS ----------

def test_fibonacci_type_error(fib_func):
    with pytest.raises(TypeError) as e:
        fib_func("10")
    assert "integer type" in str(e.value)


def test_fibonacci_negative_value(fib_func):
    with pytest.raises(ValueError) as e:
        fib_func(-5)
    assert "non-negative" in str(e.value)


# ---------- CACHE ----------

def test_fibonacci_caching_behavior():
    fib = caching_fibonacci()

    result_first = fib(10)
    closure_vars = [cell.cell_contents for cell in fib.__closure__]
    cache = next(var for var in closure_vars if isinstance(var, dict))

    assert 10 in cache
    assert cache[10] == result_first

    result_second = fib(10)
    assert result_first == result_second


def test_fibonacci_repeated_calls_are_consistent(fib_func):
    first = fib_func(12)
    second = fib_func(12)
    assert first == second == 144

# ---------- INSPECTION ----------

def test_fibonacci_signature():
    fib = caching_fibonacci()
    sig = inspect.signature(fib)
    assert len(sig.parameters) == 1
    assert "number" in sig.parameters
    assert sig.parameters["number"].annotation is int


def test_fibonacci_return_type_hint():
    fib = caching_fibonacci()
    sig = inspect.signature(fib)
    assert sig.return_annotation is int


def test_caching_fibonacci_return_type_hint():
    sig = inspect.signature(caching_fibonacci)
    assert sig.return_annotation == callable

# ---------- PRODUCTIVITY ----------

@pytest.mark.performance
def test_large_input_completes_quickly(fib_func):
    start = time.time()
    result = fib_func(30)
    duration = time.time() - start

    assert result == 832040
    assert duration < 0.3
