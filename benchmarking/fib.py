"""Do benchmark with multiple environments."""
import anyio

from benchmarking.common import Run, benchmark

runs = (
    Run(
        docker="python:3.10-slim-buster",
        setup=[],
        entrypoint=["python", "scripts/time_fib.py", "40", "-l", "py"],
        output_file="python310",
    ),
    Run(
        docker="python:3.11-slim-buster",
        setup=[],
        entrypoint=["python", "scripts/time_fib.py", "40", "-l", "py"],
        output_file="python311",
    ),
    Run(
        docker="pypy",
        setup=[],
        entrypoint=["python", "scripts/time_fib.py", "40", "-l", "py"],
        output_file="pypy",
    ),
    Run(
        docker="python:3.10-slim-buster",
        setup=["cythonize", "-i", "src/"],
        entrypoint=["python", "scripts/time_fib.py", "40", "-l", "cy"],
        output_file="cython",
    ),
    Run(
        docker="python:3.10-slim-buster+rust",
        setup=["cd", "src/rs", "&&", "maturin", "develop", "--release"],
        entrypoint=["python", "../../scripts/time_fib.py", "40", "-l", "rs"],
        output_file="rust",
    ),
    Run(
        docker="mojo",
        setup=[],
        entrypoint=["mojo", "src/mojo/low.🔥"],
        output_file="mojo",
    ),
)


async def main() -> None:
    """Benchmark using dagger pipelines."""
    for run in runs:
        benchmark(run)


anyio.run(main)
