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

G = [Vector.identity(variablesCount, i) for i in range(variablesCount)]
u = Vector(variablesCount, True)
A = Matrix(equationsCount, variablesCount, True)
b = Vector(equationsCount, True)

print "A: \n"

A.mprint()

print "B: \n"

print b.vectorData

print "U: \n"

print u.vectorData

print "\n"

print len(G)

def firstCheck(vectorOne, vectorTwo):
    return vectorOne > vectorTwo

def secondCheck(vectorOne, vectorTwo):
    return -u < vectorOne - vectorTwo < u

def thirdCheck(vectorOne, vectorTwo):
    return -b < A*(vectorOne - vectorTwo) < b

isLengthChanged = True

while isLengthChanged:
    startLength = len(G)
    for i in range(len(G)):
        for j in range(len(G)):
            if firstCheck(G[i], G[j]) & secondCheck(G[i], G[j]) & thirdCheck(G[i], G[j]):
                difference = G[i] - G[j]
                isUnique = True
                for k in G:
                    if (k == difference):
                        isUnique = False
                if (isUnique):
                    G.append(G[i] - G[j])

    endLength = len(G)
    isLengthChanged = endLength != startLength
    print endLength

for i in G:
    print i.vectorData

# print Vector.identity(equationsCount, 0).vectorData
#
# identityMatrix = Matrix.identity(equationsCount)
#
# print identityMatrix.matrixData[0].vectorData > identityMatrix.matrixData[1].vectorData

