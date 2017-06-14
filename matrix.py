import random
from vector import *
from constants import *

class Matrix:
    def __init__(self, lines, columns, generate):
        self.columns = columns
        self.lines = lines
        if generate:
            self.matrixData = [ Vector(lines, True) for x in range(columns) ]

    @staticmethod
    def identity(size):
        identityMatrix = Matrix(size, size, False)
        identityMatrix.matrixData = [ Vector.identity(size, i) for i in range(size)]
        return identityMatrix

    @staticmethod
    def test():
        identityMatrix = Matrix(2, 3, False)
        identityMatrix.matrixData = [ Vector.test([2, 0, 2]), Vector.test([2, 1, 0])]
        print identityMatrix.matrixData[0].vectorData;
        print identityMatrix.matrixData[1].vectorData;
        return identityMatrix

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.columns != other.size:
                raise TypeError();

            result = Vector(self.columns)
            result.vectorData = [0 for i in range(self.columns)]

            for i in range(self.lines):
                for j in range(self.columns):
                    result.vectorData[i] += self.matrixData[i].vectorData[j] * other.vectorData[j]

        return result;