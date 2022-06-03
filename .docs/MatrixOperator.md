
# Matrix Operator

---

### Methods

#### 1. `apply_linear_transformation`
#### 2. `apply_translation`
#### 3. `apply_rotation`
#### 4. `apply_scale`

---

### `apply_linear_transformation`

**parameter_names : types**
- **vector** : `Vector2` or `Vector3`
- **transformation_axis** : `Axis2` or `Axis3`

**returns : types**
- **vector** : `Vector2` or `Vector3`

**Description** : Given `vector` and `transformation_axis`, applies linear transformation to given `vector`
using `transformation_axis` in 2D/3D space and returns a new vector.

**Example** : `transformed_vector = matrix_operator().apply_linear_transformation(vector, axis)`

---

### `apply_translation`

**parameter_names : types**
- **vector** : `Vector2` or `Vector3`
- **translation_vector** : `Vector2` or `Vector3`

**Description** : Given `vector` and `translation_vector`, applies translation to given `vector` using
`translation_vector` in 2D/3D space and returns a new vector.

**Example** : `translated_vector = matrix_operator().apply_translation(vector, vector)`

---

### `apply_rotation`

**parameter_names : types**
- **vector** : `Vector2` or `Vector3`
- **rotation_vector** : `int` or `float` or `Vector3`

**Description** : Given `vector` and `rotation_vector`, applies rotation to given `vector` using `rotation_vector`
in 2D/3D space and returns a new vector.

**Important notes;**
- Method expects `rotation_vector` or its properties(x, y, z) in **degrees**

**Example** : `rotated_vector = matrix_operator().apply_rotation(vector, angle)`

---

### `apply_scale`

**parameter_names : types**
- **vector** : `Vector2` or `Vector3`
- **scale_vector** : `Vector2` or `Vector3`

**Description** : Given `vector` and `scale_vector`, applies scale to given `vector` using `scale_vector`
in 2D/3D space and returns a new vector.

**Example** : `scaled_vector = matrix_operator().apply_scale(vector, vector)`