# Faster Python with Friends

> Stronger with friends.

## Overview

In this project we investigate ways in which we can make a Python application faster. See below a comparison of different methods.

Note: values may change - local setup was experimental and unstable.

| method      | time - fibonacci | time - triangles | relative - fibonacci | relative - triangles | relative - average |
| ----------- | ---------------- | ---------------- | -------------------- | -------------------- | ------------------ |
| python 3.10 | 31.8979s         | 133.9575s        | 1                    | 1                    | 1                  |
| python 3.11 | 19.1536s         | 123.0167s        | 0.6005               | 0.9183               | 0.7594             |
| pypy3       | 5.9190s          | 5.9954s          | 0.1856               | 0.0448               | 0.1152             |
| cython      | 6.8486s          | 127.8094s        | 0.2147               | 0.9541               | 0.5844             |
| mypyc       | 1.6822s          | 117.1570s        | 0.0527               | 0.8746               | 0.4637             |
| pyo3        | 0.7056s          | 3.3887s          | **0.0221**           | **0.0253**           | **0.0237**         |
| mojo*       | ???              | ???              |                      |                      |                    |


## Setup

```bash
git clone ...
pdm install
```

> `pdm install --dev ./src/rs` or, in a virtual environment, `pip install ./src/rs`

For updates, uninstall and reinstall `./src/rs`.

Install pypy3.10 -> create venv mannually and run script manually

install dependencies with `pip install .`
## Python 3.9

```bash
source .venv/bin/activate
python -c "from pure_python.triangles import main; main()"
```

## Python 3.11

```bash
pdm venv create -n py311 python3.11
eval $(pdm venv activate py311)
python -c "from pure_python.triangles import main; main()"
```

## Cython

```bash
source .venv/bin/activate
cythonize --3str -i pure_python/triangles.py
python -c "from pure_python.triangles import main; main()"
rm pure_python/*.so pure_python/*.c # clean up
rm -rf pure_python/build  # clean up
```

## Mypyc

```bash
source .venv/bin/activate
mypyc pure_python/triangles.py
python -c "from triangles import main; main()"
rm *.so  # clean up
rm -rf build/  # clean up
```

## PyO3

```bash
source .venv/bin/activate
cd rust_python/
maturin develop --release
python -c "from rust_python.triangles import main; main();"
```

## Mojo 🔥

Mojo not open source yet (June, 2023).
Could not compare performance to regular Python - imports, different syntax, etc.
