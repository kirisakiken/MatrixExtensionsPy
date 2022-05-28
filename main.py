from src.extensions.vector_extensions import VectorExtensions
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

    v1 = Vector3(1, 11.2, 0)
    v2 = Vector3(2, -5, 0)
    res = VectorExtensions.get_cross_product(v1, v2)
    print(res)

    print("Fin")
