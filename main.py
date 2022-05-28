from src.matrix_extensions import MatrixExtensions
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


if __name__ == '__main__':
    matrix_operator = MatrixExtensions()

    position = Vector2(3, 4)
    deg = 45
    result = matrix_operator.apply_rotation_2d(position, deg)

    print(result.x)
    print(result.y)

    print("Fin")
