from elasticsearch import Elasticsearch
from datetime import date, timedelta

d = date.today() - timedelta(days=1)
yesterday = d.strftime('%Y.%m.%d')

es = Elasticsearch(
    ['localhost'],
    http_auth=('username', 'password'),
    scheme="https",
    port=64298,
    maxsize=1000
)

es.indices.refresh(index="_all")
#res = es.search(index="_all", body={
res = es.search(index="logstash-" + yesterday, body={
  "query": {
    "bool": {
      "must": [
        {
          "query_string": {
            "query": "_exists_:username.keyword",
            "analyze_wildcard": 'true',
            "default_field": "*"
          }
        }
      ],
      "filter": [],
      "should": [],
      "must_not": []
    }
  }
}, size=10000)

#print("Got %d Hits:" % res['hits']['total'])

for hit in res['hits']['hits']:
    try:
        print("%(username)s: %(password)s" % hit["_source"])
    except KeyError:
        print("%(username)s: " % hit["_source"])
