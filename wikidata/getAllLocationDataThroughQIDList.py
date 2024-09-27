import os
import pandas as pd
import re
from queryHeadquarters import request_queryHeadquarters

# 56 of 196 failed

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "uniqueCompaniesWithQidsAndWithLocationData.json")

df = pd.read_json(file_path, orient='columns')
allQids = df['qid']  # f.e. http://www.wikidata.org/entity/Q81965
if 'headquarterCoordinates' not in df.columns:
    df['headquarterCoordinates'] = None
filtered_qids_WithoutLocation = df[df['headquarterCoordinates'].isnull()]['qid']

print('total queries:  ', len(filtered_qids_WithoutLocation))  # total queries:   196
# print(allCompanyQidWikidataLinks[0])
# qid = re.search(r'Q\d+', allCompanyQidWikidataLinks[0]).group()
# print(qid)


notFoundCountercounter = 0
for qidLink in filtered_qids_WithoutLocation:
    if qidLink is None or qidLink == '':
        notFoundCountercounter += 1
        continue
    qid = re.search(r'Q\d+', qidLink).group()

    queryResponse = request_queryHeadquarters(qid)

    if queryResponse is None:
        notFoundCountercounter += 1
    else:
        companyName = queryResponse['companyLabel']['value']
        headquarterLocationName = queryResponse['headquartersLabel']['value']
        headquarterCoordinates = queryResponse['coordinateLocation']['value']

        print(headquarterCoordinates)
        if headquarterCoordinates is not None:
            df.loc[df['qid'].str.strip() == qidLink, 'headquarterCoordinates'] = headquarterCoordinates


# updates json with query results
df.to_json('./uniqueCompaniesWithQidsAndWithLocationData.json', orient='records', indent=4)
print('total number of no company qids found:', notFoundCountercounter, ' of ', len(filtered_qids_WithoutLocation))
