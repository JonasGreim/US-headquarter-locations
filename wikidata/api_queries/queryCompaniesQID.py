from SPARQLWrapper import SPARQLWrapper, JSON
#  https://github.com/RDFLib/sparqlwrapper

# SPARQLWrapper Docs
# https://sparqlwrapper.readthedocs.io/en/latest/main.html
# https://foundation.wikimedia.org/wiki/Policy:User-Agent_policy

# idea: make query better (-> maybe add country USA, or one more company labels)

def request_query_companies_qid(company_name):
    user_agent = 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql", agent=user_agent)
    sparql.setReturnFormat(JSON)

    search_string = company_name

    #  found 40/50 companies
    sparql.setQuery(f"""
    SELECT DISTINCT ?item ?itemLabel
    WHERE {{
      ?item ?label "{search_string}"@en.
      ?article schema:about ?item.
      ?article schema:inLanguage "en".
      ?article schema:isPartOf <https://en.wikipedia.org/>.

      SERVICE wikibase:label {{
        bd:serviceParam wikibase:language "en".
      }}
    }}
    """)

    # old query with tags
    # sparql.setQuery(f"""
    # SELECT DISTINCT ?item ?itemLabel
    # WHERE {{
    #   ?item rdfs:label "{search_string}"@en .
    #   ?item wdt:P31/wdt:P279* ?type .
    #   VALUES ?type {{ wd:Q783794 wd:Q4830453 }}
    #   SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
    #   }}
    # """)
    # Q783794 (company) or Q4830453 (business)
    # wdt:P31/wdt:P279* = instance of (P31) a company or an instance of a subclass (P279*) of a company

    try:
        queryResult = sparql.queryAndConvert()
        firstBestResult = queryResult["results"]["bindings"][0]
        return firstBestResult
    except Exception as e:
        print('No Results found with company name:  ', company_name)

    # Example value of queryResult["results"]["bindings"]
    # {'item': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q54173'}, 'itemLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'General Electric'}}
    # {'item': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q3088656'}, 'itemLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Mobil'}}