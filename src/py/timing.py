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
        print(f"`{f.__name__}` took {end - start:0.4f} seconds")  # noqa: T201
        return result

    return wrapper
