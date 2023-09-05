import time


def fib(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fib(n - 2) + fib(n - 1)


def time_fib(n):
    start = time.time_ns()
    result = fib(n)
    end = time.time_ns()
    print("`fib` took ", (end - start) / 1_000_000_000, "secs")


def main():
    time_fib(40)

if __name__ == "__main__":
    main()
