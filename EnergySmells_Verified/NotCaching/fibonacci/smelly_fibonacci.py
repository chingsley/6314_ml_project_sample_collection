def fibonacci(n: int) -> int:
    """Computes the nth Fibonacci number recursively without caching."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
