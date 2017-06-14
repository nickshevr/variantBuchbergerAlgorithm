import random
from constants import *

class Vector:
    def __init__(self, size, shouldGenerate = False):
        self.size = size
        if shouldGenerate:
            self.vectorData = [random.randrange(elemMinValue, elemMaxValue) for y in range(size)]

    def __eq__(self, other):
        iseq = True
        for y in range(self.size):
            if self.vectorData[y] != other.vectorData[y]:
                iseq = False
                break
        return iseq

    def __gt__(self, other):
        isgt = False
        for y in range(self.size):
            if self.vectorData[y] > other.vectorData[y]:
                isgt = True
                break
        return isgt

    def __lt__(self, other):
        result = self.__gt__(other)
        if result is NotImplemented:
            return result
        return not result

    def __sub__(self, other):
        result = Vector(self.size, False)
        result.vectorData = []

        for i in range(self.size):
            result.vectorData.append(self.vectorData[i] - other.vectorData[i])
        return result

    def __neg__(self):
        result = Vector(self.size, False)
        result.vectorData = []

        for i in range(self.size):
            result.vectorData.append(-self.vectorData[i])
        return result

    @staticmethod
    def test(list):
        identityMatrix = Vector(len(list), False)
        identityMatrix.vectorData = list
        return identityMatrix

    @staticmethod
    def identity(size, position):
        identityVector = Vector(size, False)
        identityVector.vectorData = [1 if i == position else 0 for i in range(size)]
        return identityVector
