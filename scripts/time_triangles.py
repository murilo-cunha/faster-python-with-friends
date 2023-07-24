"""Time the triangles calculation."""
import argparse
from pathlib import Path

from misc import timer
from py.triangles import load_and_calc


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("graph", type=Path)
    return parser.parse_args()


@timer
def calc(args: argparse.Namespace) -> int:
    """Calculate triangles for graph in file."""
    return load_and_calc(args.graph)


if __name__ == "__main__":
    args = parse_args()
    n_triangles = calc(args)
    print("Number of triangles: ", n_triangles)  # noqa: T201
    assert n_triangles == 1612010  # noqa: S101
