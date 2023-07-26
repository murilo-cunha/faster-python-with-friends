"""Time the fibonacci function."""
import argparse
from collections.abc import Callable

from misc import timer


def import_(args: argparse.Namespace) -> Callable[[int], int]:
    """Dynamically import the module."""
    if args.lib == "py":
        from py.fibonacci import fib
    elif args.lib == "rs":
        from rs.fibonacci import fib
    return fib


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)
    parser.add_argument("lib", choices=["py", "rs"])
    return parser.parse_args()


@timer
def calc(args: argparse.Namespace, fib: Callable[[int], int]) -> int:
    """Calculate triangles for graph in file."""
    return fib(args.num)


if __name__ == "__main__":
    args = parse_args()
    f = import_(args)
    fib_num = calc(args, f)
    print(f"{fib_num=}")  # noqa: T201
