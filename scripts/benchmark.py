"""Execute a command."""
import sys

import anyio
import dagger


async def test() -> None:
    """Testing dagger pipelines."""
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        python = (
            client.container()
            # pull container
            .from_("python:3.11-slim-buster")
            .with_directory(
                ".",
                client.host().directory("."),
                include=["scripts/", "src/", "pyproject.toml"],
            )
            .with_exec(["pip", "install", "."])
            .with_exec(
                ["python", "scripts/time_fib.py", "40", "-l", "py", ">", "output.txt"]
            )
        )

        # execute
        await python.file("output.txt").export("output.txt")  # .stdout()


anyio.run(test)
