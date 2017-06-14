import random
from constants import *

class Vector:
    def __init__(self, size, shouldGenerate):
        self.size = size
        if shouldGenerate:
            self.vectorData = [random.randrange(elemMinValue, elemMaxValue) for y in range(size)]

    def __gt__(self, other):
        isgt = False
        for y in range(self.size):
            if self.vectorData[y] > other.vectorData[y]:
                isgt = True
                break
        return isgt

    def __lt__(self, other):
        result = other.__gt__(self)
        if result is NotImplemented:
            return result
        return not result

    @staticmethod
    def identity(size, position):
        identityVector = Vector(size, False)
        identityVector.vectorData = [1 if i == position else 0 for i in range(size)]
        return identityVector
