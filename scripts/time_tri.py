"""Time the triangles calculation."""
import argparse
import sys
from collections.abc import Callable
from pathlib import Path
from textwrap import dedent

from py.timing import timer
from py.triangles import Graph, load_graph


def import_(args: argparse.Namespace) -> Callable[[Path], int]:
    """Dynamically import the module."""
    if args.lib == "py":
        from py.triangles import calc_triangles as f
    elif args.lib == "cy":
        from cy.triangles import calc_triangles as f
    elif args.lib == "rs":
        import rs  # https://github.com/PyO3/pyo3/issues/759

        f = rs.triangles.calc_triangles
    return f  # noqa: RET504


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("graph", type=Path)
    parser.add_argument("-l", "--lib", choices=["py", "cy", "rs"], required=True)
    parser.add_argument("-s", "--silent", action="store_true")
    return parser.parse_args()


@timer
def calc(graph: Graph, calc_triangles: Callable[[Graph], int]) -> int:
    """Calculate triangles for graph in file."""
    return calc_triangles(graph)


if __name__ == "__main__":
    args = parse_args()
    f = import_(args)
    nodes = load_graph(args.graph)
    num_triangles, time = calc(nodes, f)
    if not args.silent:
        print(  # noqa: T201
            dedent(
                f"""\
                version: {sys.version}
                `triangles` took {time:0.4f} seconds
                {num_triangles=}""",
            ),
        )
    else:
        print(f"{time:0.4f}")  # noqa: T201
