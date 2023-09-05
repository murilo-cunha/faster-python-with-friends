# from String import String
from python import Python


def add_to_graph(graph, org, dst):
    if org in graph.keys():
        current_dst = graph[org]
        current_dst.append(dst)
        graph[org] = current_dst

class Foo:
    def __init__(self, x):
        self.x = x


def main():
    pathlib = Python.import_module("pathlib")
    csv = Python.import_module("csv")

    txt = pathlib.Path("data/facebook_combined.txt").read_text()
    let s: String = txt.to_string()
    graph = Python.dict()

    org = String("")
    for i in range(len(s)):
        char = s[i]

        if char != "\n":
            if char != " ":
                if org == "":
                    org = char
                else:
                    dst = char
        else:
            org = ""
            add_to_graph(graph, org, dst)
    print(len(s))
