from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.operations.translation import TranslationOperator
from src.operations.rotation import RotationOperator
from src.operations.scale import ScaleOperator


class MatrixExtensions:
    def __init__(self):
        self.translation_operator = TranslationOperator()
        self.rotation_operator = RotationOperator()
        self.scale_operator = ScaleOperator()
        # self.transformation_operator = TransformationOperator()

    def apply_translation_2d(self, vector_2: Vector2, translation_vector: Vector2):
        return self.translation_operator.get_translation_2d(vector_2, translation_vector)

    def apply_rotation_2d(self, vector_2: Vector2, degree: float):
        return self.rotation_operator.get_rotation_2d(vector_2, degree)

    def apply_scale_2d(self, vector_2: Vector2, scale_vector: Vector2):
        return self.scale_operator.get_scale_2d(vector_2, scale_vector)
