from SPARQLWrapper import SPARQLWrapper, JSON
#  https://github.com/RDFLib/sparqlwrapper


def request_queryIndustry(qid):
    user_agent = 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql", agent=user_agent)
    sparql.setReturnFormat(JSON)

    sparql.setQuery(f"""
    SELECT ?company ?companyLabel ?industryLabel WHERE {{
      VALUES ?company {{ wd:{qid} }}
      ?company wdt:P452 ?industry.
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
    }}
    """)

    try:
        queryResult = sparql.queryAndConvert()
        return queryResult["results"]["bindings"][0]
    except Exception as e:
        print('industry not found', e)
