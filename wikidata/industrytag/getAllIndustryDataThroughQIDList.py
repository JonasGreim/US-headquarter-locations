import os
import pandas as pd
import re
from queryIndustry import request_queryIndustry

# 17 of 196 failed
# todo check created list

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "./../uniqueCompaniesWithQidsAndWithLocationData.json")

df = pd.read_json(file_path, orient='columns')
df['industry'] = None
allQids = df['qid']  # f.e. http://www.wikidata.org/entity/Q81965
filtered_qids_WithoutIndustry = df[df['industry'].isnull()]['qid']

print('total queries:  ', len(filtered_qids_WithoutIndustry))  # total queries:   196
# print(allCompanyQidWikidataLinks[0])
# qid = re.search(r'Q\d+', allCompanyQidWikidataLinks[0]).group()
# print(qid)


notFoundCountercounter = 0
for qidLink in filtered_qids_WithoutIndustry:
    if qidLink is None or qidLink == '':
        notFoundCountercounter += 1
        continue
    qid = re.search(r'Q\d+', qidLink).group()

    queryResponse = request_queryIndustry(qid)

    if queryResponse is None:
        notFoundCountercounter += 1
    else:
        companyName = queryResponse['companyLabel']['value']
        industry = queryResponse['industryLabel']['value']

        print(industry)
        if industry is not None:
            df.loc[df['qid'].str.strip() == qidLink, 'industry'] = industry


# updates json with query results
df.to_json('./uniqueCompaniesWithQidsAndWithIndustry.json', orient='records', indent=4)
print('total number of no company qids found:', notFoundCountercounter, ' of ', len(filtered_qids_WithoutIndustry))
