"""Time function utilities."""
import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def timer(f: Callable) -> Callable:
    """Time a function."""

    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:  # noqa: ANN401
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        return (result, end - start)

    return wrapper
