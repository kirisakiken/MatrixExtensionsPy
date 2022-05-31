
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
3. [ ] `Vector4 -- [x, y, z, w]`
4. [ ] `Quaternion -- [x, y, z, w]`
5. [x] `Line2 -- ax + by = c`
6. [x] `Line3 -- ax + by + cz = d`

### Supported Operations;
1. [x] `Linear Transformation in 2D/3D`
2. [x] `Translation in 2D/3D`
3. [x] `Rotation in 2D/3D`
4. [x] `Scale in 2D/3D`

---

### Usage
- Use `MatrixOperator` for 2D/3D operations [src/matrix_operator.py](https://github.com/kirisakiken/matrix-operations-py/blob/master/src/matrix_operator.py)
- Use `VectorExtensions` for other vector operations [src/extensions/vector_extensions.py](https://github.com/kirisakiken/matrix-operations-py/blob/master/src/extensions/vector_extensions.py)

---

### Dependencies;
- numpy 1.22.4

---

### TODO:
- add unit tests
- add ci/cd
- add docker
- add documentation
