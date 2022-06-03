import numpy as np

from src.types.axis import (
    Axis2,
    Axis3,
)


class AxisExtensions:
    def __init__(self):
        pass

    @staticmethod
    def axis2_to_matrix_2x2(axis_2: Axis2):
        return np.array([[axis_2.x_axis.x, axis_2.y_axis.x],
                         [axis_2.x_axis.y, axis_2.y_axis.y]])

    @staticmethod
    def axis3_to_matrix_3x3(axis_3: Axis3):
        return np.array([[axis_3.x_axis.x, axis_3.y_axis.x, axis_3.z_axis.x],
                         [axis_3.x_axis.y, axis_3.y_axis.y, axis_3.z_axis.y],
                         [axis_3.x_axis.z, axis_3.y_axis.z, axis_3.z_axis.z]])
