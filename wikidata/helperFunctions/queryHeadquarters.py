from SPARQLWrapper import SPARQLWrapper, JSON
#  https://github.com/RDFLib/sparqlwrapper

# TODO insert companies in query -> loop it

def request_queryHeadquarters(qid):
    user_agent = 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql", agent=user_agent)
    sparql.setReturnFormat(JSON)

    sparql.setQuery(f"""
    SELECT ?company ?companyLabel ?headquartersLabel ?coordinateLocation WHERE {{
      VALUES ?company {{ wd:{qid} }}
      ?company wdt:P159 ?headquarters.
      ?headquarters wdt:P625 ?coordinateLocation.
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
    }}
    """)

    try:
        queryResult = sparql.queryAndConvert()
        return queryResult["results"]["bindings"][0]
    except Exception as e:
        print('headquarter not found', e)

# result example:
# Apple
# Cupertino
# Point(-122.041944444 37.3175)
