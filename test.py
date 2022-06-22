import pytest

from infinite_numbers import fibonacci

class TestInfiniteNumbers:
    def test_fibonacci_yields_correct_numbers(self):
        fib_generator = fibonacci()
        num1 = next(fib_generator)
        num2 = next(fib_generator)
        num3 = next(fib_generator)
        num4 = next(fib_generator)
        assert num1 == 0
        assert num2 == 1
        assert num3 == 1
        assert num4 == 2

    def test_fibonacci_with_higher_number(self):
        fib_generator = fibonacci()
        for i in range(100):
            next(fib_generator)
        num100 = next(fib_generator)
        assert num100 == 354224848179261915075
