"""Time the fibonacci function."""
import argparse
import sys
from collections.abc import Callable
from textwrap import dedent

from py.timing import timer


def import_(args: argparse.Namespace) -> Callable[[int], int]:
    """Dynamically import the module."""
    if args.lib == "py":
        from py.fibonacci import fib as f
    elif args.lib == "cy":
        from cy.fibonacci import fib as f
    elif args.lib == "rs":
        import rs  # https://github.com/PyO3/pyo3/issues/759

        f = rs.fibonacci.fib
    return f  # noqa: RET504


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)
    parser.add_argument("-l", "--lib", choices=["py", "cy", "rs"], required=True)
    parser.add_argument("-s", "--silent", action="store_true")
    return parser.parse_args()


@timer
def calc(args: argparse.Namespace, fib: Callable[[int], int]) -> int:
    """Calculate triangles for graph in file."""
    return fib(args.num)


if __name__ == "__main__":
    args = parse_args()
    f = import_(args)
    fib_num, time = calc(args, f)
    if not args.silent:
        print(  # noqa: T201
            dedent(
                f"""\
                version: {sys.version}
                `fibonacci` took {time:0.4f} seconds
                {fib_num=}""",
            ),
        )
    else:
        print(f"{time:0.4f}")  # noqa: T201
