import numpy as np

from src.types.axis import Axis2


class AxisExtensions:
    def __init__(self):
        pass

    @staticmethod
    def axis2_to_matrix_2x2(axis_2: Axis2):
        return np.array([[axis_2.x_axis.x, axis_2.y_axis.x],
                         [axis_2.x_axis.y, axis_2.y_axis.y]])

