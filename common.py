from buchberger import *

lowerTime = 200
maxTime = 0
averageTime = 0

for i in range(10):
    solver = buchBergerAlgorithm(7, 2)
    solver.inputPrint()
    time = solver.solve()

    averageTime += time

    if time < lowerTime :
        lowerTime = time

    if time > maxTime :
        maxTime = time


print 'LowestTime:', lowerTime
print 'MaxTime:', maxTime
print 'averageTime:', averageTime/100