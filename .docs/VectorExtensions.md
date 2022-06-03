
# Vector Extensions

---

### Methods

#### 1. `get_dot_product`
#### 2. `get_cross_product`
#### 3. `get_distance`
#### 4. `get_lerp`
#### 5. `get_perpendicular_distance`

---

### `get_dot_product`

**parameter_names : types**
- **a** : `Vector2` or `Vector3`
- **b** : `Vector2` or `Vector3`

**returns : types**
- **value** : `float`

**Description** : Calculates and returns **dot product** of given vectors `a` and `b`.

**Example** : `dot = VectorExtensions.get_dot_product(vector, vector)`

---

### `get_cross_product`

**parameter_names : types**
- **a** : `Vector2` or `Vector3`
- **b** : `Vector2` or `Vector3`

**returns : types**
- **value** : `float`

**Description** : Calculates and returns **cross product** of given vectors `a` and `b`.

**Example** : `dot = VectorExtensions.get_cross_product(vector, vector)`

---

### `get_distance`

**parameter_names : types**
- **a** : `Vector2` or `Vector3`
- **b** : `Vector2` or `Vector3`

**returns : types**
- **value** : `float`

**Description** : Calculates and returns **distance** between vector `a` and vector `b`.

**Example** : `dot = VectorExtensions.get_distance(vector, vector)`

---

### `get_lerp`

**parameter_names : types**
- **a** : `Vector2` or `Vector3`
- **b** : `Vector2` or `Vector3`
- **t** : `float`
- **unclamped** : `bool` , _default_ : False

**returns : types**
- **vector** : `Vector2` or `Vector3`

**Description** : Calculates and returns lerp value with given `t` between vector `a` and vector `b`.

**Important notes;**
- parameter `unclamped` is `False` by default. For unclamped lerp results, set parameter `unclamped` as `True`

**Examples** ;
- `lerp_clamped = VectorExtensions.get_lerp(vector, vector, t)`
- `lerp_unclamped = VectorExtensions.get_lerp(vector, vector, t, True)`

---

### `get_perpendicular_distance`

**parameter_names : types**
- **vector** : `Vector2` or `Vector3`
- **line** : `Line2` or `Line3`

**returns : types**
- **value** : `float`

**Description** : Calculates and returns **perpendicular distance** between `vector` and `line`.

**Important notes;**
- Parameter `line` represents `ax + by + c` or `ax + by + cz + d`. And line can be declared as `Line2(a, b, c)`
or `Line3(a, b, c, d)`

**Example** : `dot = VectorExtensions.get_distance(vector, vector)`

---
