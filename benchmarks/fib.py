"""Benchmark fibonacci calculation using Dagger."""
import sys

import anyio
import dagger


async def main() -> None:
    """Do benchmark."""
    interpreter = "3.10"
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        build = client.host().directory(".").docker_build()
        benchmark = (
            build.with_directory(
                "/app/src",
                client.host().directory("src"),
            )
            .with_directory(
                "/app/scripts",
                client.host().directory("scripts"),
            )
            .with_file("/app/pyproject.toml", client.host().file("pyproject.toml"))
            .with_workdir("app")
            .with_exec(["pyenv", "install", interpreter])
            .with_exec(["pyenv", "global", interpreter])
            .with_exec(["pyenv", "exec", "pip", "install", "."])
            .with_exec(
                ["pyenv", "exec", "python", "scripts/time_fib.py", "40", "-l", "py"]
            )
        )
        await benchmark


anyio.run(main)
