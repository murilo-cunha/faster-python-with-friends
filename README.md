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
| pyo3        | 0.7056s          | 3.3887s          | 0.0221               | **0.0253**           | **0.0237**         |
| mojo*       | 0.3658           | ???              | **0.0061**           |                      |                    |

*mojo compute is different due to different setup
## Setup

Make sure you have Python 3.10 and 3.11 and Pypy3 installed. You can use [pyenv](https://github.com/pyenv/pyenv) for managing versions. Also make sure to have [Rust installed](https://www.rust-lang.org/tools/install) for PyO3 experiment.


### Get the code

```bash
git clone git@github.com:murilo-cunha/faster-python-with-friends.git
cd faster-python-with-friends
```

### Create and install dependencies for each environment

#### Python 3.10

```bash
python3.10 -m venv .venv
source .venv/bin/activate  # or `.venv/Scripts/activate` on Windows
pip install .
```

#### Python 3.11

```bash
python3.11 -m venv .venv-3.11
source .venv-3.11/bin/activate  # or `.venv-3.11/Scripts/activate` on Windows
pip install .
```

#### Pypy

```bash
pypy3 -m venv .venv-pypy
source .venv-pypy/bin/activate  # or `.venv-pypy/Scripts/activate` on Windows
pip install .
```

#### Mojo

Install Mojo on Modular's their [official website](https://www.modular.com/mojo).

## Experiments

Follow the snippets below for each experiment. Some experiments produce artifacts - make sure to delete them before running the next experiment.

### Python 3.10

```bash
source .venv/bin/activate  # or `.venv/Scripts/activate` on Windows
python scripts/time_fib.py 40 --lib py  # fibonacci
python scripts/time_tri.py data/facebook_combined.txt --lib py  # triangles
```

### Python 3.11

```bash
source .venv-3.11/bin/activate  # or `.venv-3.11/Scripts/activate` on Windows
python scripts/time_fib.py 40 --lib py  # fibonacci
python scripts/time_tri.py data/facebook_combined.txt --lib py  # triangles
```

### Cython

```bash
source .venv/bin/activate  # or `.venv/Scripts/activate` on Windows
cythonize -i src/cy  # build extensions
python scripts/time_fib.py 40 --lib cy  # fibonacci
python scripts/time_tri.py data/facebook_combined.txt --lib cy  # triangles
```

### Mypyc

```bash
source .venv/bin/activate  # or `.venv/Scripts/activate` on Windows
mypyc src/py  # build extensions
python scripts/time_fib.py 40 --lib py  # fibonacci
python scripts/time_tri.py data/facebook_combined.txt --lib py  # triangles
```

### Pypy

```bash
source .venv-pypy/bin/activate  # or `.venv-pypy/Scripts/activate` on Windows
python scripts/time_fib.py 40 --lib py  # fibonacci
python scripts/time_tri.py data/facebook_combined.txt --lib py  # triangles
```

### PyO3 (bindings to Rust)

```bash
source .venv/bin/activate  # or `.venv/Scripts/activate` on Windows
cd src/rs/
maturin develop --release  # build package
python ../../scripts/time_fib.py 40 --lib rs  # fibonacci
python ../../scripts/time_tri.py data/facebook_combined.txt --lib rs  # triangles
```

### Mojo 🔥

```bash
mojo src/mojo/fibonacci/low.🔥
```
