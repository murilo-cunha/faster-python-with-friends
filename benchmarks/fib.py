"""Benchmark fibonacci calculation using Dagger."""
import sys
from datetime import datetime, timezone
from pathlib import Path

import anyio
import dagger

CURR_DIR = Path(__file__).parent
SCRIPT = "python scripts/time_fib.py 40 --lib {lib} > {output_file}"


def _run_script(
    container: dagger.Container,
    sh: str,
    *,
    use_cache: bool = True,
) -> dagger.Container:
    """Run benchmark on Python module."""
    if not use_cache:
        container = container.with_env_variable(
            "CACHEBUSTER",
            str(datetime.now(tz=timezone.utc)),
        )
    return container.with_exec(["/bin/sh", "-c", sh])


def _cython(
    container: dagger.Container,
    output_file: str = "output.log",
    *,
    use_cache: bool = True,
) -> dagger.Container:
    """Run benchmark on Cython module."""
    return _run_script(
        container.with_exec(["cythonize", "-i", "src/cy"]),
        sh=SCRIPT.format(lib="cy", output_file=output_file),
        use_cache=use_cache,
    )


def _mypyc(
    container: dagger.Container,
    output_file: str = "output.log",
    *,
    use_cache: bool = True,
) -> dagger.Container:
    """Run benchmark on Mypyc module."""
    return _run_script(
        container.with_exec(["mypyc", "src/py"]),
        sh=SCRIPT.format(lib="py", output_file=output_file),
        use_cache=use_cache,
    )


def _python(
    container: dagger.Container,
    output_file: str = "output.log",
    *,
    use_cache: bool = True,
) -> dagger.Container:
    """Run benchmark on Python module."""
    return _run_script(
        container,
        sh=SCRIPT.format(lib="py", output_file=output_file),
        use_cache=use_cache,
    )


async def main() -> None:
    """Do benchmark."""
    alternatives = {
        "python:3.10-bookworm": [_python, _mypyc, _cython],
        "python:3.11-bookworm": [_python],
        "pypy:3.10-bookworm": [_python],
    }
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        # Could also local with
        #  `build = client.host().directory(".").docker_build("Dockerfile")`
        for container in alternatives:
            for benchmark_fn in alternatives[container]:
                setup = (
                    client.container()
                    .from_(container)
                    .with_env_variable("DEBIAN_FRONTEND", "noninteractive")
                    .with_directory(
                        "/app/src",
                        client.host().directory("src"),
                    )
                    .with_directory(
                        "/app/scripts",
                        client.host().directory("scripts"),
                    )
                    .with_file(
                        "/app/pyproject.toml", client.host().file("pyproject.toml")
                    )
                    .with_workdir("app")
                    .with_exec(["pip", "install", "."])
                )

                await benchmark_fn(
                    setup,
                    f"{benchmark_fn.__name__}.log",
                    use_cache=False,
                ).file(f"{benchmark_fn.__name__}.log").export(
                    str(CURR_DIR / f"{container + benchmark_fn.__name__}.log"),
                )
    CURR_DIR.glob("*.log")


anyio.run(main)
