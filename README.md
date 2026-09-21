# common_math_sense

A simple, human-friendly mathematics library for Python.

Made for people who want to do **actual maths** in Python without having to fight with Python first.

## Features

* Basic mathematics
* Trigonometry
* Basic physics calculations
* Algebra and equation solving
* Human-friendly functions
* Common mathematical constants

## Installation

Clone the repository:

```bash
git clone https://github.com/dhhlk/common_math_sense.git
cd common_math_sense
py -m pip install .
```

SymPy is installed automatically as a dependency.

## Example

```python
from imports.genius import solve

solve("x + 13 = 13 + 2")
```

Output:

```text
x = [2]
```

It can also solve equations where the variable appears on both sides:

```python
solve("x + 4 = 2*x")
```

Output:

```text
x = [4]
```

## Why?

Python is great at programming, but sometimes you just want to write the maths you actually mean.

**common_math_sense** aims to make common mathematics easier and more human-friendly.

## Version

**v1.0.0** 🚀

First stable release.
