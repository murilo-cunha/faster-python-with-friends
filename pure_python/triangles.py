"""Calculate triangles for network in https://snap.stanford.edu/data/ego-Facebook.html."""
from collections import defaultdict

import csv
import os
from pathlib import Path
import time
from typing import List, Optional, Set
from typing import DefaultDict

NeighborNodes = List[int]
Graph = DefaultDict[int, NeighborNodes]


def load_graph(p: Optional[Path] = None) -> Graph:
    """Load undirected graph from CSV file with ` ` delimiter."""
    data = p or Path(os.environ["FB_DATA"])
    nodes: Graph = defaultdict(list)
    with data.open() as f:
        directed = list(csv.reader(f, delimiter=" "))

    undirected = directed + [[b, a] for [a, b] in directed]
    for node_id, neighbor in undirected:
        nodes[int(node_id)].append(int(neighbor))
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

    visited: NeighborNodes = []
    for node in graph.keys():
        neighbors_visited: NeighborNodes = []
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


def load_and_calc(data: Optional[Path] = None) -> int:
    """Calculate triangles for graph in file."""

    nodes = load_graph(data)
    return calc_triangles(nodes)


def _about(p: Path) -> None:
    """Information about the graph."""
    with p.open() as f:
        edges = list(csv.reader(f, delimiter=" "))
    nodes: Set[str] = set()
    for e in edges:
        nodes |= set(e)

    print("number of nodes:", len(nodes))
    print("number of edges:", len(edges))


def main():
    start = time.time()
    n_triangles = load_and_calc()
    stop = time.time()

    print("number of triangles: ", n_triangles)
    print(f"time: {stop - start:.2f}s")
    assert n_triangles == 1612010
