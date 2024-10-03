import pandas as pd

# Map the unique companies data to the SP500 companies ranking data

unique_companies = pd.read_json('./data_sp500/uniqueCompaniesWithQidsLocationAndWithOurIndustrySectors.json')
items = pd.read_json('./data_sp500/dataset_sp500.json')

# Filter items to include only the top 55 based on rank
items['rank'] = items['rank'].astype(int)
top_items = items[items['rank'] <= 55]

# Merge the filtered items with the unique companies data on companyName and company
merged_items = top_items.merge(unique_companies, left_on='company', right_on='companyName', how='left')

# Select columns
merged_items = merged_items[['rank', 'company', 'market_cap', 'year', 'headquarterCoordinates', 'qid', 'wikiDataName', 'industry']]

merged_items.to_json('./data_sp500/x_rankingWithCoordinates.json', orient='records', indent=4)
