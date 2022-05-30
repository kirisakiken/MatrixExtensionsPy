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

    v1 = Vector2(0, 0)
    v2 = Vector2(11, 11)
    res = VectorExtensions.get_lerp(v1, v2, 0.1, True)
    print(res.x)
    print(res.y)

    print("Fin")
