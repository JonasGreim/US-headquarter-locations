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
count = filtered_data['company'].unique()

print('total:  ', len(count))

counter = 0
for i in count:
    a = request_query_companies_qid(i)
    if a is None:
        counter = counter + 1

    print(a)
print('total number no company qids:', counter)
