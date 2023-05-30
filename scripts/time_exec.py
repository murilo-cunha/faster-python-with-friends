from pathlib import Path

# import pure_python.triangles as triangles  # python 3.9, 3.11, cython

import triangles  # mypyc
# import rust_python as triangles
import time

if __name__ == "__main__":
    fb_data = Path(__file__).parents[1] / "data" / "facebook_combined.txt"
    # triangles._about(fb_data)

    start = time.time()
    n_triangles = triangles.main(fb_data)
    stop = time.time()

    print("number of triangles: ", n_triangles)
    print(f"time: {stop - start:.2f}s")
    assert n_triangles == 1612010
