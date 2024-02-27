import numpy as np
import math

class Integral:
    def __init__(self, function, start, end):
        self.function = function
        self.start = start
        self.end = end

class Sym(Integral):
    def Calc(self, n=100):
        h = (self.end - self.start) / n
        result = self.function(self.start) + self.function(self.end)

        for i in range(1, n):
            x_i = self.start + i * h
            result += 4 * self.function(x_i) if i % 2 == 1 else 2 * self.function(x_i)

        return h * result / 3

class Trap(Integral):
    def Calc(self):
        total = 0
        array = np.linspace(self.start, self.end, num=10**6)
        for i in array:
            total += 2 * self.function(i)   # 2 * sin(i)
        result = (array[1] - array[0]) * (total - self.function(array[0])
                                          - self.function(array[-1])) / 2
        return result

def func(x):
    return math.cos(x)


if __name__ == '__main__':
    object_sym = Sym(func, 0, math.pi/2)
    result_sym = object_sym.Calc()

    object_trap = Trap(func, 0, math.pi/2)
    result_trap = object_trap.Calc()

    print("Simpson's method:", result_sym)
    print("Trapezoid method:", result_trap)
