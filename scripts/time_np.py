"""Based off https://stackoverflow.com/questions/31322632/."""
import sys

import numpy as np
from py.timing import timer


@timer
def np_mean() -> None:
    """Time 5x numpy mean operation."""
    for _ in range(5):
        vv = np.random.rand(10_000_000).astype(np.float32)
        _ = np.mean(vv)


if __name__ == "__main__":
    print("version:", sys.version)  # noqa: T201
    np_mean()
