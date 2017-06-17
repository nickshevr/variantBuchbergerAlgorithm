from buchberger import *
from elasticsearch import Elasticsearch

lowerTime = 200
maxTime = 0
averageTime = 0

es = Elasticsearch()

for variablesCount in range(3, 15):
    for i in range(100):
        solver = buchBergerAlgorithm(variablesCount, variablesCount-2)
        result = solver.solve()
        doc = {
            'time': result.get('time'),
            'endLength': result.get('endLength'),
            'equationsCount': variablesCount - 2,
            'variablesCount': variablesCount
        }

        print doc

        es.index(index="bounded-algorithm-1", doc_type='result', body=doc)
