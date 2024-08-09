import os
import pandas as pd

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "items.json")

df = pd.read_json(file_path, orient='columns')
filtered_data = df.loc[df['rank'] <= 55]
uniqueCompanyNames = filtered_data['company'].unique()


df = pd.DataFrame({
    'companyName': uniqueCompanyNames,
    'searchQueryCompanyName': uniqueCompanyNames,
    'wikiDataName': '',
    'qid': ''
})

df.to_json('./uniqueCompaniesWithQids.json', orient='records', lines=False, indent=4)
