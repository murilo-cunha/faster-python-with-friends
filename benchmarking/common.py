"""Common utilities for creating benchmarks."""
import sys
from dataclasses import dataclass

import dagger


@dataclass
class Run:
    """A run within the benchmark."""

    docker: str
    setup: list[str]
    entrypoint: list[str]
    output_file: str | None = None


async def benchmark(run: Run) -> None:
    """Do benchmark for a single run."""
    output = run.output_file or run.docker
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        python = (
            client.container()
            .from_(run.docker)
            .with_directory(
                ".",
                client.host().directory("."),
                include=["scripts/", "src/", "pyproject.toml"],
            )
            .with_exec(
                ["pip", "install", "."] + (["&&", *run.setup] if run.setup else []),
            )
            .with_mounted_temp("/tmp/benchmarks")  # noqa: S108
            .with_exec([*run.entrypoint, ">", output])
        )
        await python.file(output).export(f"/tmp/benchmarks/{output}")  # noqa: S108
