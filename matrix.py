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

    def __mul__(self, other):
        if isinstance(other, Vector):
            result = Vector(other.size)
            result.vectorData = [ 0 for i in range(other.size)]
            # for j in range(self.columns):
            #     for i in range(self.lines):
            #         result.vectorData[j] += self.matrixData[j].vectorData[i] * other.vectorData[j]
            for i in range(self.columns):
                for j in range(self.lines):
                    result.vectorData[i] += self.matrixData[j].vectorData[i] * other.vectorData[j]

        return result