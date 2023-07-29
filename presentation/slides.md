---
theme: meetup
lineNumbers: false
themeConfig:
  title: Faster Python with Friends
  github: github.com/murilo-cunha
  twitter: _murilocunha
info: >
  ## Faster Python with Friends


  Python's flexible and intuitive syntax enables developers to quickly build
  applications. But on the other hand, it may be slow during runtime. Luckily,
  there are different ways we can speed up a Python program. In this talk, we'll
  explore different alternatives to make Python programs faster.
drawings:
  persist: false
title: Faster Python with Friends
hideInToc: true
layout: intro
---

# Faster Python with Friends

Stronger with friends 💪


---
layout: presenter
photo: /images/pic-blur.png
hideInToc: True
---

# About me

---

# Today

<Toc/>

---
layout: twocols
---

# Is Python slow?

- Add perf chart
- add funnny meme
- mention 3.11+nogil efforts


---

# Do we care?

::left::

- Mention ML annd python


- Is Python slow?
- Do we care?

<br/>



<img src="/images/slack.png" class="shadow-lg rounded-lg" />


::right::

<Tweet id="1677648534563086338" scale=0.8 />


---

# Experiment

- mention caution - benchmarks are always wrong

- fibbonacci + approach
- triannglee + approach
- show project structure

---

# Cython

- https://cython.readthedocs.io/en/latest/src/tutorial/pure.html?highlight=526#managing-the-global-interpreter-lock
- https://cython.readthedocs.io/en/latest/src/tutorial/pure.html?highlight=526#augmenting-pxd
- https://www.infoworld.com/article/3702888/cython-30-the-next-generation-of-python-at-the-speed-of-c.html
- https://cython.readthedocs.io/en/latest/src/quickstart/cythonize.html
- Cython 3.0
- Aims to be a Superset of Python
- `cdef`, `cimport`, ...

- show typing differences
- show snippet of project sstructure after cythonize
  - mention that if .so is available, it will be used

- demo:
  - cy without cythonize is the same as python performance
  - cythonize py + run py
  - cythonize cy + run cy
- could not run with cythonn outside type hintts

---

# Pypy

- https://pypy.org/performance.html

```bash
Building wheels for collected packages: numpy, py
  Building wheel for numpy (pyproject.toml) ... -
```

---
# Approaches...

---

# Bindings

- PyO3
- PyBind

---

# Final thoughts

- Python for most stuff, optimize for worst
- This is already the reality - add examples
- We are stronger with friends


<img src = "https://media4.giphy.com/media/Fzb4nqyfrTA66u2HOD/giphy.gif" class="h-56"/>


---
layout: qrcode
url: https://2023.pycon.pt
---

# Code and slides

<br/>
