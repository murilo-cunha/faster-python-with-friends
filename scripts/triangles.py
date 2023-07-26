"""Time the triangles calculation."""
import argparse
from collections.abc import Callable
from pathlib import Path

from misc import timer


def import_(args: argparse.Namespace) -> Callable[[Path], int]:
    """Dynamically import the module."""
    if args.lib == "py":
        from py.triangles import load_and_calc as f
    elif args.lib == "rs":
        from rs.triangles import load_and_calc as f
    return f


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("graph", type=Path)
    parser.add_argument("lib", choices=["py", "rs"])
    return parser.parse_args()


@timer
def calc(args: argparse.Namespace, load_and_calc: Callable[[Path], int]) -> int:
    """Calculate triangles for graph in file."""
    return load_and_calc(args.graph)


if __name__ == "__main__":
    args = parse_args()
    f = import_(args)
    n_triangles = calc(args, f)
    print("Number of triangles: ", n_triangles)  # noqa: T201
    assert n_triangles == 1612010  # noqa: S101
