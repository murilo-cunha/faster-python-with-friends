"""Fibonacci numbers."""


def fib(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    return n if n <= 1 else fib(n - 2) + fib(n - 1)
