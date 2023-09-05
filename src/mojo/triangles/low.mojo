from python import Python


def load_graph(data):
    """Load undirected graph from CSV file with ` ` delimiter."""

    builtins = Python.import_module("builtins")
    csv = Python.import_module("csv")
    collections = Python.import_module("collections")

    nodes = collections.defaultdict(builtins.list)
    f = builtins.open("facebook_combined.txt")
    directed = csv.reader(f, " ")
    f.close()

    rev = builtins.list()
    for i in directed:
        rev.append([i[1], i[0]])
    undirected = directed + rev
    for n in undirected:
        nodes[builtins.int(n[0])].append(builtins.int(n[1]))
    return nodes


def calc_triangles():
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
    # Python.add_to_path("utils")
    # utils = Python.import_module("utils")
    # var graph = utils.graph()
    num_triangles = 0

    for node in graph.keys():
        neighbors_visited = []
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


def main():
    # graph = calc_triangles()
    load_graph("facebook_combined.txt")
