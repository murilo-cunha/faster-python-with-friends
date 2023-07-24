"""Time the fibonacci function."""
import argparse

from misc import timer
from py.fibonacci import fib


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)
    return parser.parse_args()


@timer
def calc(args: argparse.Namespace) -> int:
    """Calculate triangles for graph in file."""
    return fib(args.num)


if __name__ == "__main__":
    args = parse_args()
    fib_num = calc(args)
    print(f"{fib_num=}")  # noqa: T201
