import os
import pandas as pd

# create a json file with unique companies

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "./data_sp500/dataset_sp500.json")

df = pd.read_json(file_path, orient='columns')
filtered_data = df.loc[df['rank'] <= 55]
uniqueCompanyNames = filtered_data['company'].unique()


df = pd.DataFrame({
    'companyName': uniqueCompanyNames,
    'searchQueryCompanyName': uniqueCompanyNames,
    'wikiDataName': '',
    'qid': ''
})

df.to_json('./data_sp500/uniqueCompanies.json', orient='records', lines=False, indent=4)
