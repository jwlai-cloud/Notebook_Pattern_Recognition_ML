import numpy as np
from prml.nn.function import Function


class Tanh(Function):

    def _forward(self, x):
        self.out = np.tanh(x)
        return self.out

    def _backward(self, delta, x):
        return delta * (1 - self.out ** 2)


def tanh(x):
    return Tanh().forward(x)
