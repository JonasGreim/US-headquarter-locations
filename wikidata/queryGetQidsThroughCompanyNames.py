import os
import pandas as pd
from queryCompaniesQID import request_query_companies_qid

# looping through the companies and checking if they have a qid

current_dir = os.path.dirname(__file__)
# parent_dir_path = os.path.join(current_dir, ".")
file_path = os.path.join(current_dir, "uniqueCompaniesWithQids.json")

df = pd.read_json(file_path, orient='columns')
filtered_UniqueCompanyNames_WithoutQid = df[df['qid'] == '']['searchQueryCompanyName']

# 48  of  196 no result
print('total queries:  ', len(filtered_UniqueCompanyNames_WithoutQid))  # total queries:   196

counter = 0
for search_uniqueCompanyName in filtered_UniqueCompanyNames_WithoutQid:
    queryResponse = request_query_companies_qid(search_uniqueCompanyName)
    if queryResponse is None:
        counter += 1
    else:
        qid = queryResponse["item"]["value"]
        wikidata_company_name = queryResponse["itemLabel"]["value"]
        print(qid, wikidata_company_name)

        df.loc[df['searchQueryCompanyName'] == search_uniqueCompanyName, 'qid'] = qid
        df.loc[df['searchQueryCompanyName'] == search_uniqueCompanyName, 'wikiDataName'] = wikidata_company_name


# updates json with query results
df.to_json('./uniqueCompaniesWithQids.json', orient='records', indent=4)
print('total number of no company qids found:', counter, ' of ', len(filtered_UniqueCompanyNames_WithoutQid))


# 5 companies are missing -> no wikidata or wikipedia entry ??
# search again -> positios manually

# TODO search headquarter location data


# I need 2 lists: (curate company names)

# input: unique names list (csv, json)  (input list)
# output: unique names + qid (if found)

# depends how much company fails -> compute on their own again
# -> need name changes/translation table


# item top 100 from 1958-2005
# take top 55




# create csv, json with pandas -> insert manually qids
# take top 60