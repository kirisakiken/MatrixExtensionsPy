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
from src.types.line3 import Line3

if __name__ == '__main__':
    matrix_operator = MatrixOperator()

    v1 = Vector3(1, 2, 0)
    l2 = Line3(1, -1, 2)
    res = VectorExtensions.get_perpendicular_distance(v1, l2)
    print(res)

    print("Fin")
