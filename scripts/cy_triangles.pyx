"""Calculate triangles for network in https://snap.stanford.edu/data/ego-Facebook.html."""
from collections import defaultdict

import csv
import os
from pathlib import Path
from typing import Dict, List, Optional

Graph = Dict[str, List[str]]


def load_graph(p: Optional[Path] = None) -> Graph:
    """Load undirected graph from CSV file with ` ` delimiter."""
    data = p or Path(os.environ["FB_DATA"])
    nodes = defaultdict(list)
    with data.open() as f:
        directed = list(csv.reader(f, delimiter=" "))

    undirected = directed + [[b, a] for [a, b] in directed]
    for node_id, neighbor in undirected:
        nodes[node_id].append(neighbor)
    return nodes


def calc_triangles(graph: Graph) -> int:
    """
    Calculate number of triangles.

    0. Track nodes visited and number of triangles
    1. For each node:
        a. Track neighbors visited
        b. Get it's neighbors
        c. If the neighbor node has not been visited, check it's neighbors
         ("far neighbor")
        d. If the "far neighbor" has not been visited (either nodes or neighbors), check
         that the current node is in the "far neighbor's" neighbors and increment
         triangle count if present
        e. Add neighbor node to neighbors visited
    2. Add node to nodes visited
    """
    num_triangles: int = 0

    visited: List[str] = []
    for node in graph.keys():
        neighbors_visited: List[str] = []
        for neighbor in graph[node]:
            if neighbor not in visited:
                for far_neighbor in graph[neighbor]:
                    if (
                        far_neighbor not in neighbors_visited
                        and far_neighbor not in visited
                        and node in graph[far_neighbor]
                    ):
                        num_triangles += 1
            neighbors_visited.append(neighbor)
        visited.append(node)
    return num_triangles


def main(data: Optional[Path] = None) -> int:
    """Calculate triangles for graph in file."""

    nodes = load_graph(data)
    return calc_triangles(nodes)

def _about(p: Path) -> None:
    """Information about the graph."""
    with p.open() as f:
        edges = list(csv.reader(f, delimiter=" "))
    nodes = {}
    for e in edges:
        nodes |= set(e)

    print("number of nodes:", len(nodes))
    print("number of edges:", len(edges))

if __name__ == "__main__":
    fb_data = Path(__file__).parents[1] / "data" / "facebook_combined.txt"
    _about(fb_data)
    
    n_triangles = main(fb_data)
    print("number of triangles:", n_triangles)
    assert n_triangles == 1612010
