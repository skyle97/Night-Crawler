from elasticsearch import Elasticsearch

elastic = Elasticsearch([{'host': 'localhost', 'port': 9200}])
