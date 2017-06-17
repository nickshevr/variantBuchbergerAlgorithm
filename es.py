from buchberger import *
from elasticsearch import Elasticsearch

lowerTime = 200
maxTime = 0
averageTime = 0

es = Elasticsearch([{'host': 'swarm.smartycrm.com', 'port': '80'}])

settings = {
 "mappings" : {
    "result": {
        "properties" : {
            "time" : {"type": "float" },
            "vectorNorm" : {"type": "float" },
            "endLength" : {"type": "integer" },
            "equationsCount" : { "type" : "integer" },
            "variablesCount" : { "type" : "integer" }
        }
    }
}
}
if not es.indices.exists('bounded_3'):
    es.indices.create(index='bounded_3', ignore=400, body=settings)

for variablesCount in range(3, 15):
    for i in range(5):
        solver = buchBergerAlgorithm(variablesCount, variablesCount-2)
        result = solver.solve()
        doc = {
            'time': result.get('time'),
            'endLength': result.get('endLength'),
            'equationsCount': variablesCount - 2,
            'variablesCount': variablesCount,
            'vectorNorm': result.get('vectorU')
        }

        print doc

        es.index(index="bounded_3", doc_type='result', body=doc)
