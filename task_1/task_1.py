def caching_fibonacci() -> callable:
    cache = {0: 0, 1: 1}

    def fibonacci(number: int) -> int:

        if not isinstance(number, int):
            raise TypeError("Input must be an integer type.")

        if number < 0:
            raise ValueError("Input must be a non-negative integer.")

        if number in cache:
            return cache[number]

        cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return cache[number]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))
