"""Fibonacci numbers."""


def fib(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)
