
# Matrix Operations Library for Python

---

Library has basic `matrix` and `vector` operations available for 2D and 3D
spaces. To use the library in external projects. Either pull project files
into your repositroy, or reference it via `setup.py` or `requirements.txt`
file.

---

### Supported Types;
1. [x] `Vector2 -- [x, y]`
2. [x] `Vector3 -- [x, y, z]`
3. [x] `Vector4 -- [x, y, z, w]`
4. [x] `Quaternion -- [x, y, z, w]`
5. [x] `Line2 -- ax + by = c`
6. [x] `Line3 -- ax + by + cz = d`

### Supported Operations;
1. [x] `Linear Transformation in 2D/3D`
2. [x] `Translation in 2D/3D`
3. [x] `Rotation in 2D/3D`
4. [x] `Scale in 2D/3D`



## [Library Documentation](https://github.com/kirisakiken/matrix-operations-py/blob/master/.docs/MatrixOperator.md#matrix-operator)

---

### Usage

Import following files into your project,
- Use `MatrixOperator` for 2D/3D operations [src/matrix_operator.py](https://github.com/kirisakiken/matrix-operations-py/blob/master/src/matrix_operator.py)
- Use `VectorExtensions` for other vector operations [src/extensions/vector_extensions.py](https://github.com/kirisakiken/matrix-operations-py/blob/master/src/extensions/vector_extensions.py)

---

### Project Dependencies;
- numpy 1.22.4

---

## Contribution Guide

To become a contributor, please send your `github username` and name of this repository to `bezmican96@gmail.com`.

### Development Dependencies

- flake8 4.0.1
- pytest 7.1.2
- [+Project Dependencies](https://github.com/kirisakiken/matrix-operations-py#dependencies)

---

### 1. Setup Development environment

- Create venv/conda environment (recommended) ~ Python 3.8, 3.9, 3.10
- Activate venv/conda environment
- Install project/development dependencies by;
  1. `pip install -r requirements.txt`
  2. `pip install -r dev_requirements.txt`

### 2. Introducing code changes

- Create new branch using latest master
- Introduce your code . . .


### 3. Linting/Testing code changes

- Add unit tests for the code
- Lint your code with;
  1. `flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics`
  2. `flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics`
- Test your code by executing: `pytest`
- Test your code coverage by executing `pytest --cov=src/ --cov-fail-under=90 && rm .coverage`
- Commit and push changes


### 4. Open pull request

- Open pull request using your branch
- Target to master
- Add description explaining features/fixes that you've introduced.
- And good to go! ☺

---

### TODO
- add quaternion support in operations
- cd package release
