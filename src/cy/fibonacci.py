"""Fibonacci numbers."""
import cython


def fib(n: cython.int) -> cython.int:
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)
