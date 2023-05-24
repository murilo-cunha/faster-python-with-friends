"""Calculate triangles for network in https://snap.stanford.edu/data/ego-Facebook.html."""
from __future__ import annotations
from collections import defaultdict

import csv
from pathlib import Path

Graph = dict[str, list[str]]


def load_graph(p: Path) -> Graph:
    """Load undirected graph from CSV file with ` ` delimiter."""
    nodes = defaultdict(list)
    with p.open() as f:
        directed = list(csv.reader(f, delimiter=" "))

    undirected = directed + [[b, a] for [a, b] in directed]
    for node_id, neighbor in undirected:
        nodes[node_id].append(neighbor)
        
    print("number of nodes:", len(nodes))
    print("number of edges:", len(directed))
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
    
    visited: list[str] = []
    for node in graph.keys():
        neighbors_visited: list[str] = []
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


if __name__ == "__main__":
    fb_data = Path(__file__).parents[1] / "data" / "facebook_combined.txt"
    nodes = load_graph(fb_data)
    n_triangles = calc_triangles(nodes)
    
    print("number of triangles:", n_triangles)
    assert n_triangles == 1612010
