import os
import pandas as pd
from wikidata.helperFunctions.queryCompaniesQID import request_query_companies_qid

# looping through the unique companies and checking if they have a qid (wikidata page id) -> add qid if not present
# updates json with query results

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, './data_sp500/uniqueCompanies.json')

df = pd.read_json(file_path, orient='columns')
filtered_UniqueCompanyNames_WithoutQid = df[df['qid'] == '']['searchQueryCompanyName']

# 48  of  196 no result
print('total queries:  ', len(filtered_UniqueCompanyNames_WithoutQid))  # total queries:   196

notFoundCountercounter = 0
for search_uniqueCompanyName in filtered_UniqueCompanyNames_WithoutQid:
    queryResponse = request_query_companies_qid(search_uniqueCompanyName)
    if queryResponse is None:
        notFoundCountercounter += 1
    else:
        qid = queryResponse["item"]["value"]
        wikidata_company_name = queryResponse["itemLabel"]["value"]
        print(qid, wikidata_company_name)

        df.loc[df['searchQueryCompanyName'] == search_uniqueCompanyName, 'qid'] = qid
        df.loc[df['searchQueryCompanyName'] == search_uniqueCompanyName, 'wikiDataName'] = wikidata_company_name

df.to_json('./data_sp500/uniqueCompaniesWithQids.json', orient='records', indent=4)
print('total number of no company qids found:', notFoundCountercounter, ' of ', len(filtered_UniqueCompanyNames_WithoutQid))
