from src.extensions.vector_extensions import VectorExtensions
from src.matrix_operator import MatrixOperator
from src.types.axis import (
    AXIS,
    Axis2,
    Axis3,
)
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.types.line2 import Line2

if __name__ == '__main__':
    matrix_operator = MatrixOperator()

    v1 = Vector2(1, 2)
    l2 = Line2(1, -1, 2)
    res = VectorExtensions.get_perpendicular_distance_2d(v1, l2)
    print(res)

    print("Fin")
