from matrix import *
from vector import *
from constants import *
import timeit
from time import time


class buchBergerAlgorithm():
    def __init__(self, variablesCount, equationsCount):
        self.variablesCount = variablesCount
        self.equationsCount = equationsCount
        self.G = [Vector.identity(variablesCount, i) for i in range(variablesCount)]
        #self.u = Vector.test([1, 1, 1, 1, 1, 1, 1])
        self.c = Vector(variablesCount, True)
        self.u = Vector(variablesCount, True)
        self.A = Matrix(equationsCount, variablesCount, True)
        self.b = Vector(equationsCount, True)
        self.cacheSet = set()

    def firstCheck(self, vectorOne, vectorTwo):
        if vectorOne * self.c > vectorTwo * self.c:
            return True
        return vectorOne > vectorTwo

    def secondCheck(self, vectorOne, vectorTwo):
        return -self.u < vectorOne - vectorTwo < self.u

    def thirdCheck(self, vectorOne, vectorTwo):
        return -self.b < self.A * (vectorOne - vectorTwo) and self.A * (vectorOne - vectorTwo) < self.b

    def inputPrint(self):
        print "C: \n"

        print self.c.vectorData

        print "A: \n"

        self.A.mprint()

        print "B: \n"

        print self.b.vectorData

        print "U: \n"

        print self.u.vectorData

        print "\n"

    def solve(self):
        endLength = 0
        isLengthChanged = True
        t1 = time()
        #print len(self.G)
        while isLengthChanged and endLength < 2000:
            startLength = len(self.G)
            for i in range(len(self.G)):
                for j in range(len(self.G)):
                    trigger = str(i) + "-" + str(j) in self.cacheSet

                    if not trigger:
                        self.cacheSet.add(str(i) + "-" + str(j))
                        self.cacheSet.add(str(j) + "-" + str(i))

                    if i != j and not trigger and self.firstCheck(self.G[i], self.G[j]) and self.secondCheck(self.G[i], self.G[j]) and self.thirdCheck(
                            self.G[i], self.G[j]):
                        difference = self.G[i] - self.G[j]
                        isUnique = True
                        # print len(cacheSet)
                        # print "Checked", i, j
                        for k in self.G:
                            if (k == difference):
                                isUnique = False
                                break
                        if (isUnique):
                            self.G.append(self.G[i] - self.G[j])

            endLength = len(self.G)
            #print endLength
            isLengthChanged = endLength != startLength

        t2 = time()
        lastLength = endLength

        # for i in self.G:
        #     print i.vectorData

        #print "generation test field for %f seconds" % (t2 - t1)

        return {
            'time': t2-t1,
            'endLength': lastLength
        }



