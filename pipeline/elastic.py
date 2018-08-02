from datetime import datetime
from elasticsearch import Elasticsearch
#es = Elasticsearch('our.es.server.name:9200')
es = Elasticsearch()

doc = {'term': 'test', 'usr': 108}
res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)

print(res['_source'])
