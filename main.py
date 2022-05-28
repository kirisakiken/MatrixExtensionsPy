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

    point = Vector3(2, 3, 4)
    rot = Vector3(30, 45, 75)
    result = matrix_operator.apply_rotation_3d(point, rot)

    print(result.x)
    print(result.y)
    print(result.z)

    print("Fin")
