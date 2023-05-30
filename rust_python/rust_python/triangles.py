"""Python entrypoint for timing execution."""
from pathlib import Path
import time
from rust_python.rust_python import load_and_calc


def main():
    fb_data = Path(__file__).parents[2] / "data" / "facebook_combined.txt"

    start = time.time()
    n_triangles = load_and_calc(str(fb_data))
    stop = time.time()

    print("number of triangles: ", n_triangles)
    print(f"time: {stop - start:.2f}s")
    assert n_triangles == 1612010
