import numpy as np
import math


class Integral:
    def __init__(self, function, start, end):
        self.function = function
        self.start = start
        self.end = end

    def calc(self, n):
        pass


class Sym(Integral):
    def calc(self, n):
        h = (self.end - self.start) / n
        result = self.function(self.start) + self.function(self.end)

        for i in range(1, n):
            x_i = self.start + i * h
            result += 4 * self.function(x_i) if i % 2 == 1 else 2 * self.function(x_i)

        return h * result / 3


class Trap(Integral):
    def calc(self, n):
        total = 0
        array = np.linspace(self.start, self.end, n)
        for i in array:
            total += 2 * self.function(i)  # 2 * sin(i)
        result = (array[1] - array[0]) * (total - self.function(array[0])
                                          - self.function(array[-1])) / 2
        return result


def func(x):
    return math.cos(x)


if __name__ == '__main__':

    result_sym = Sym(func, 0, math.pi / 2).calc(100)
    result_trap = Trap(func, 0, math.pi / 2).calc(100)

    print("Simpson's method:", result_sym)
    print("Trapezoid method:", result_trap)
