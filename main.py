from src.matrix_operator import MatrixOperator
from src.types.axis import (
    Axis2,
    Axis3,
)
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


if __name__ == '__main__':
    matrix_operator = MatrixOperator()

    position = Vector3(2, 3, 1)
    axis = Axis3(Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1))
    result = matrix_operator.apply_transformation_3d(position, axis)

    print(result.x)
    print(result.y)
    print(result.z)

    print("Fin")
