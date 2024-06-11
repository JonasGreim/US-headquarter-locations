from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setReturnFormat(JSON)
# From https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#Cats
sparql.setQuery("""
SELECT ?company ?companyLabel ?headquartersLabel WHERE {
  VALUES ?company { wd:Q1454852 } ?company wdt:P159 ?headquarters.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
""")

try:
    queryResult = sparql.queryAndConvert()
    for r in queryResult["results"]["bindings"]:
        print(r['company']['value'])
        print(r['companyLabel']['value'])
        print(r['headquartersLabel']['value'])
except Exception as e:
    print(e)

# Example value of queryResult["results"]["bindings"]
# {'company': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q1454852'},
#  'companyLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Hormel'},
#  'headquartersLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Austin'}}
