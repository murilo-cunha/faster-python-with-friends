"""Time the fibonacci function."""
import argparse
import sys
from collections.abc import Callable

from py.timing import timer


def import_(args: argparse.Namespace) -> Callable[[int], int]:
    """Dynamically import the module."""
    if args.lib == "py":
        from py.fibonacci import fib as f
    elif args.lib == "cy":
        from cy.fibonacci import fib as f
    elif args.lib == "rs":
        from rs.fibonacci import fib as f
    return f


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)
    parser.add_argument("-l", "--lib", choices=["py", "cy", "rs"], required=True)
    return parser.parse_args()


@timer
def calc(args: argparse.Namespace, fib: Callable[[int], int]) -> int:
    """Calculate triangles for graph in file."""
    return fib(args.num)


if __name__ == "__main__":
    print("version:", sys.version)  # noqa: T201
    args = parse_args()
    f = import_(args)
    fib_num = calc(args, f)
    print(f"{fib_num=}")  # noqa: T201
