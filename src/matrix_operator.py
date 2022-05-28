from src.types.axis import (
    Axis2,
    Axis3,
)
from src.types.vector2 import Vector2
from src.types.vector3 import Vector3
from src.operations.transformation import TransformationOperator
from src.operations.translation import TranslationOperator
from src.operations.rotation import RotationOperator
from src.operations.scale import ScaleOperator


class MatrixOperator:
    def __init__(self):
        self.__transformation_operator = TransformationOperator()
        self.__translation_operator = TranslationOperator()
        self.__rotation_operator = RotationOperator()
        self.__scale_operator = ScaleOperator()

    # Applies 2D/3D linear transformation to a Vector2/Vector3
    def apply_linear_transformation(self, vector: Vector2 | Vector3, transformation_axis: Axis2 | Axis3) -> Vector2 | Vector3:
        if type(vector) == Vector2 and type(transformation_axis) == Axis2:
            return self.__transformation_operator.get_transformation_2d(vector, transformation_axis)
        elif type(vector) == Vector3 and type(transformation_axis) == Axis3:
            return self.__transformation_operator.get_transformation_3d(vector, transformation_axis)
        else:
            raise TypeError("Invalid argument types for method apply_transformation. Expected types: (Vector2 and "
                            "Axis2) or (Vector3 and Axis3)")

    # Applies 2D/3D translation to a Vector2/Vector3
    def apply_translation(self, vector: Vector2 | Vector3, translation_vector: Vector2 | Vector3) -> Vector2 | Vector3:
        if type(vector) == Vector2 and type(translation_vector) == Vector2:
            return self.__translation_operator.get_translation_2d(vector, translation_vector)
        elif type(vector) == Vector3 and type(translation_vector) == Vector3:
            return self.__translation_operator.get_translation_3d(vector, translation_vector)
        else:
            raise TypeError("Invalid argument types for method apply_translation. Expected types: (Vector2 and "
                            "Vector2) or (Vector3 and Vector3)")

    # Applies rotation to a Vector2/Vector3
    def apply_rotation(self, vector: Vector2 | Vector3, rotation_vector: int | float | Vector3) -> Vector2 | Vector3:
        if type(vector) == Vector2 and (type(rotation_vector) == int or type(rotation_vector) == float):
            return self.__rotation_operator.get_rotation_2d(vector, rotation_vector)
        elif type(vector) == Vector3 and type(rotation_vector) == Vector3:
            return self.__rotation_operator.get_rotation_3d(vector, rotation_vector)
        else:
            raise TypeError("Invalid argument types for method apply_rotation. Expected types: (Vector2 and "
                            "int/float) or (Vector3 and Vector3)")

    # Applies 2D/3D scale to a Vector2/Vector3
    def apply_scale(self, vector: Vector2 | Vector3, scale_vector: Vector2 | Vector3) -> Vector2 | Vector3:
        if type(vector) == Vector2 and type(scale_vector) == Vector2:
            return self.__scale_operator.get_scale_2d(vector, scale_vector)
        elif type(vector) == Vector3 and type(scale_vector) == Vector3:
            return self.__scale_operator.get_scale_3d(vector, scale_vector)
        else:
            raise TypeError("Invalid argument types for method apply_scale. Expected types: (Vector2 and "
                            "Vector2) or (Vector3 and Vector3)")