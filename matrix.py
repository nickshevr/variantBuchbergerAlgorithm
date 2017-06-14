import random
from vector import *
from constants import *

class Matrix:
    def __init__(self, lines, columns, generate):
        if generate:
            self.matrixData = [ Vector(lines, True) for x in range(columns) ]

    @staticmethod
    def identity(size):
        identityMatrix = Matrix(size, size, False)
        identityMatrix.matrixData = [ Vector.identity(size, i) for i in range(size)]
        return identityMatrix