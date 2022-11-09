import numpy as np


from benchopt import BaseObjective


class Objective(BaseObjective):

    name = "Affine"

    parameters = {
        'with_exp': [True, False]
    }

    def __init__(self, with_exp):
        self.with_exp = with_exp

    def set_data(self, a, b):
        self.a, self.b = a, b

    def compute(self, x):
        if self.with_exp:
            return np.exp(self.b + self.a * x)
        else:
            return self.b + self.a * x

    def to_dict(self):
        return dict(a=self.a, b=self.b)
