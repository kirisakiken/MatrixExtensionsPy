from src.matrix_extensions import MatrixExtensions
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3


if __name__ == '__main__':
    matrix_operator = MatrixExtensions()

    position = Vector2(3, 4)
    translation_vector = Vector2(1, 1)
    translation = matrix_operator.apply_translation_2d(position, translation_vector)

    print(translation.x)
    print(translation.y)

    print("Fin")

