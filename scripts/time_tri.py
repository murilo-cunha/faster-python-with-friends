"""Time the triangles calculation."""
import argparse
from collections.abc import Callable
from pathlib import Path

from py.timing import timer
from py.triangles import Graph, load_graph


def import_(args: argparse.Namespace) -> Callable[[Path], int]:
    """Dynamically import the module."""
    if args.lib == "py":
        from py.triangles import calc_triangles as f
    elif args.lib == "cy":
        from cy.triangles import calc_triangles as f
    elif args.lib == "rs":
        from rs.triangles import calc_triangles as f
    return f


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("graph", type=Path)
    parser.add_argument("-l", "--lib", choices=["py", "cy", "rs"], required=True)
    return parser.parse_args()


@timer
def calc(graph: Graph, calc_triangles: Callable[[Graph], int]) -> int:
    """Calculate triangles for graph in file."""
    return calc_triangles(graph)


if __name__ == "__main__":
    args = parse_args()
    f = import_(args)
    nodes = load_graph(args.graph)
    num_triangles = calc(nodes, f)
    print(f"{num_triangles=}")  # noqa: T201
