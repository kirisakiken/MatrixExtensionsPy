from src.matrix_operator import MatrixOperator
from src.types.axis import (
    AXIS,
    Axis2,
    Axis3,
)
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3

if __name__ == '__main__':
    matrix_operator = MatrixOperator()

    point = Vector3(5, 10, 1)
    tr = Vector3(2, 2, 4)
    result = matrix_operator.apply_scale(point, tr)

    print(result.x)
    print(result.y)
    print(result.z)

    print("Fin")
