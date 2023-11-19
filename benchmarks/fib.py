"""Benchmark fibonacci calculation using Dagger."""
import sys

import anyio
import dagger


async def main() -> None:
    """Do benchmark."""
    interpreters = ["3.10", "3.11"]
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        # Could also local with
        #  `build = client.host().directory(".").docker_build("Dockerfile")`
        for interpreter in interpreters:
            benchmark = (
                client.container()
                .from_(f"python:{interpreter}-slim-bookworm")
                .with_directory(
                    "/app/src",
                    client.host().directory("src"),
                )
                .with_directory(
                    "/app/scripts",
                    client.host().directory("scripts"),
                )
                .with_file("/app/pyproject.toml", client.host().file("pyproject.toml"))
                .with_workdir("app")
                # .with_exec(["pyenv", "install", interpreter])
                # .with_exec(["pyenv", "global", interpreter])
                .with_exec(["pip", "install", "."])
                .with_exec(
                    [
                        "/bin/sh",
                        "-c",
                        f"python scripts/time_fib.py 10 -l py > {interpreter}.py.log",
                    ]
                )
            )
            await benchmark.file(f"{interpreter}.py.log").export(
                f"{interpreter}.py.log"
            )


anyio.run(main)
