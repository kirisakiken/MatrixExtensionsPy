from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.operations.translation import TranslationOperator


class MatrixExtensions:
    def __init__(self):
        self.translation_operator = TranslationOperator()
        # self.rotation_operator = RotationOperator()
        # self.scale_operator = ScaleOperator()
        # self.transformation_operator = TransformationOperator()

    def apply_translation_2d(self, vector_2: Vector2, translation_vector: Vector2):
        return self.translation_operator.get_translation_2d(vector_2, translation_vector)