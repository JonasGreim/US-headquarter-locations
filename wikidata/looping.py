import os
import pandas as pd
from queryCompaniesQID import request_query_companies_qid
import json

# looping through the companies and checking if they have a qid

current_dir = os.path.dirname(__file__)
# parent_dir_path = os.path.join(current_dir, ".")
file_path = os.path.join(current_dir, "temp.json")

df = pd.read_json(file_path, orient='columns')
filtered_data = df.loc[df['rank'] <= 50]
uniqueCompanyNames = filtered_data['company'].unique()

print('total queries:  ', len(uniqueCompanyNames))


# print(request_query_companies_qid('Exxon Mobil'))

counter = 0
for i in uniqueCompanyNames:
    queryResponse = request_query_companies_qid(i)
    if queryResponse is None:
        counter = counter + 1
    else:
        qid = queryResponse["item"]["value"]
        wikidata_company_name = queryResponse["itemLabel"]["value"]
        print(qid, wikidata_company_name)
        # print(queryResponse)
print('total number of no company qids found:', counter, ' of ', len(uniqueCompanyNames))


# TODO create csv, json with pandas -> insert manually qids
# TODO take top 60