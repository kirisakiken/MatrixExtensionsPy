from src.matrix_operator import MatrixOperator
from src.types.axis import Axis2
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


if __name__ == '__main__':
    matrix_operator = MatrixOperator()

    position = Vector2(2, 3)
    axis = Axis2(Vector2(1, 0.5), Vector2(-2, 1))
    result = matrix_operator.apply_transformation_2d(position, axis)

    print(result.x)
    print(result.y)

    print("Fin")
