from matrix import *
from vector import *
from constants import *


# A = Matrix(variablesCount, equationsCount, True)
# b = Vector(equationsCount)
# u = Vector(equationsCount)
#
# G = Matrix.identity(variablesCount)
#
# print G.matrixData
#
# print b.vectorData
# print u.vectorData
#
# print b > u
# print b < u

print Vector.identity(equationsCount, 0).vectorData

identityMatrix = Matrix.identity(equationsCount)

print identityMatrix.matrixData[0].vectorData > identityMatrix.matrixData[1].vectorData

