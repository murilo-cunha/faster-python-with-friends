"""Python entrypoint for timing execution."""
import os
import time
from rust_python.rust_python import load_and_calc


def main():
    start = time.time()
    n_triangles = load_and_calc(os.environ["FB_DATA"])
    stop = time.time()

    print("number of triangles: ", n_triangles)
    print(f"time: {stop - start:.2f}s")
    assert n_triangles == 1612010
