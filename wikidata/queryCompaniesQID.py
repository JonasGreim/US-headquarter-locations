from SPARQLWrapper import SPARQLWrapper, JSON
#  https://github.com/RDFLib/sparqlwrapper

# TODO make query better (-> maybe add country USA, or more company labels)


def request_query_companies_qid(company_name):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setReturnFormat(JSON)

    search_string = company_name
    # old simple query without labels
    # sparql.setQuery(f"""
    # SELECT DISTINCT ?item
    # WHERE {{
    #   ?item rdfs:label "{search_string}"@en .
    # }}
    # """)

    sparql.setQuery(f"""
    SELECT DISTINCT ?item ?itemLabel
    WHERE {{
      ?item rdfs:label "{search_string}"@en .
      ?item wdt:P31/wdt:P279* ?type .
      VALUES ?type {{ wd:Q783794 wd:Q4830453 }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
      }}
    """)
    # Q783794 (company) or Q4830453 (business)
    # wdt:P31/wdt:P279* = instance of (P31) a company or an instance of a subclass (P279*) of a company

    try:
        queryResult = sparql.queryAndConvert()
        return queryResult["results"]["bindings"][0]
    except Exception as e:
        print(e)

    # Example value of queryResult["results"]["bindings"]
    # {'item': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q154950'}}
    # {'item': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q224038'}}
    # {'item': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q460703'}}

