from matrix import *
from vector import *
from constants import *



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

G = [Vector.identity(equationsCount, i) for i in range(variablesCount)]
u = Vector(equationsCount, True)
A = Matrix(variablesCount, equationsCount, True)
b = Vector(equationsCount, True)

print A.matrixData

startLength = len(G)
lengthDifference = 1

def firstCheck(vectorOne, vectorTwo):
    return vectorOne > vectorTwo

def secondCheck(vectorOne, vectorTwo):
    return -u < vectorOne - vectorTwo < u

def thirdCheck(vectorOne, vectorTwo):
    return -b < A*(vectorOne - vectorTwo) < b

while lengthDifference != 0:
    print lengthDifference
    for i in range(len(G)):
        for j in range(len(G)):
            if i !=j & firstCheck(G[i], G[j]) & secondCheck(G[i], G[j]) & thirdCheck(G[i], G[j]):
                G.append(G[i] - G[j])

    endLength = len(G)
    lengthDifference = endLength - startLength
    startLength = endLength


# print Vector.identity(equationsCount, 0).vectorData
#
# identityMatrix = Matrix.identity(equationsCount)
#
# print identityMatrix.matrixData[0].vectorData > identityMatrix.matrixData[1].vectorData

