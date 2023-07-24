"""Time function utilities."""
import time
from abc.collections import Callable
from functools import wraps
from typing import Any


def timer(f: Callable) -> Callable:
    """Time a function."""

    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:  # noqa: ANN401
        time.perf_counter()
        result = f(*args, **kwargs)
        time.perf_counter()
        return result

    return wrapper
