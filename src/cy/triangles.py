"""
Calculate triangles for network.

I.e.: use graph from https://snap.stanford.edu/data/ego-Facebook.html.
"""
from collections import defaultdict

import cython


def calc_triangles(graph: defaultdict[cython.int, list[cython.int]]) -> int:
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

    visited: list[cython.int] = []
    for node in graph:
        neighbors_visited: list[cython.int] = []
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
