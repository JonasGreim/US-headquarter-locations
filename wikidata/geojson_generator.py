import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import os
import json
from datetime import datetime

# 49 unique companies between 1990 - 2024
data_49 = {
    'Company Name': ['Exxon Mobil', 'IBM', 'Loews', 'Raytheon', 'Bristol-Myers Squibb', 'Merck', 
                     'Coca-Cola', 'Walmart', 'General Electric', 'Procter & Gamble', 'Verizon', 
                     'Johnson & Johnson', 'Eli Lilly', '3M', 'PepsiCo', 'Walt Disney', 'AT&T', 'AIG', 
                     'Boeing', 'DuPont', 'Pfizer', 'Microsoft', 'Altria Group', 'Home Depot', 'Intel', 
                     'Chevron', 'Bank of America', 'Cisco Systems', 'Berkshire Hathaway', 'Citigroup', 
                     'Oracle', 'Qualcomm', 'Paramount Global', 'Wells Fargo', 'JPMorgan Chase', 'UPS', 
                     'Alphabet', 'Amgen', 'Apple', 'Philip Morris Int.', 'Amazon', 'Meta/Facebook', 
                     'Visa', 'UnitedHealth', 'Mastercard', 'Tesla', 'NVIDIA', 'PayPal', 'Broadcom'],
    'Headquarters': ['Spring', 'Armonk', 'New York City', 'Waltham', 'New York City', 'Kenilworth', 
                     'Atlanta', 'Bentonville', 'Boston', 'Cincinnati', 'New York City', 
                     'New Brunswick', 'Indianapolis', 'Maplewood', 'Purchase', 'Burbank', 'Dallas', 
                     'New York City', 'Chicago', 'Wilmington', 'New York City', 'Redmond', 'Richmond', 
                     'Atlanta', 'Santa Clara', 'San Ramon', 'Charlotte', 'San Jose', 'Omaha', 'New York City', 
                     'Austin', 'San Diego', 'New York City', 'San Francisco', 'New York City', 'Atlanta', 
                     'Mountain View', 'Thousand Oaks', 'Cupertino', 'New York City', 'Seattle', 
                     'Menlo Park', 'Foster City', 'Minnetonka', 'Purchase', 'Palo Alto', 'Santa Clara', 
                     'San Jose', 'San Jose'],
    'Coordinates': ['30.31,-95.23', '41.12,-73.71', '40.71,-74.01', '42.38,-71.23', '40.71,-74.01', 
                    '40.68,-74.21', '33.75,-84.39', '36.37,-94.21', '42.36,-71.06', '39.1,-84.51', 
                    '40.71,-74.01', '40.49,-74.45', '39.77,-86.15', '44.95,-93.09', '41.04,-73.70', 
                    '34.15,-118.32', '32.78,-96.80', '40.71,-74.01', '41.88,-87.63', '39.74,-75.55', 
                    '40.71,-74.01', '47.67,-122.12', '37.54,-77.45', '33.75,-84.39', '37.38,-121.97', 
                    '37.78,-122.32', '35.23,-80.84', '37.33,-121.88', '41.26,-95.93', '40.71,-74.01', 
                    '30.27,-97.74', '32.82,-117.16', '40.71,-74.01', '37.77,-122.42', '40.71,-74.01', 
                    '33.75,-84.39', '37.42,-122.08', '34.18,-118.84', '37.33,-122.03', '40.71,-74.01', 
                    '47.61,-122.33', '37.45,-122.15', '37.56,-122.27', '44.95,-93.26', '41.04,-73.70', 
                    '37.44,-122.14', '37.36,-121.98', '37.33,-122.03', '37.33,-122.03']
}

# create dataFrame
df_49 = pd.DataFrame(data_49)

# companies lists
data_1990 = {
    'Company Name': ['Exxon Mobil', 'IBM', 'Loews', 'Raytheon', 'Bristol-Myers Squibb', 'Merck', 
                     'Coca-Cola', 'Walmart', 'General Electric', 'Procter & Gamble', 'Verizon', 
                     'Johnson & Johnson', 'Eli Lilly', '3M', 'PepsiCo', 'Walt Disney', 'AT&T', 'AIG', 
                     'Boeing', 'DuPont']
}

data_1994 = {
    'Company Name':[
        "Exxon Mobil",
        "Coca-Cola",
        "Walmart",
        "Raytheon",
        "Merck",
        "Procter & Gamble",
        "General Electric",
        "PepsiCo",
        "IBM",
        "Johnson & Johnson",
        "Bristol-Myers Squibb",
        "Chevron",
        "Loews",
        "Intel",
        "AIG",
        "Verizon",
        "Microsoft",
        "Walt Disney",
        "3M",
        "Pfizer"
    ]
}

data_1999 = {
    'Company Name':[
        "Microsoft",
        "General Electric",
        "Intel",
        "Walmart",
        "Exxon Mobil",
        "Coca-Cola",
        "IBM",
        "Merck",
        "Pfizer",
        "Cisco Systems",
        "Bristol-Myers Squibb",
        "Procter & Gamble",
        "Citigroup",
        "Johnson & Johnson",
        "Bank of America",
        "Eli Lilly",
        "Berkshire Hathaway",
        "AIG",
        "Home Depot",
        "AT&T"
    ]
}

data_2004 = {
    'Company Name':[
        "Microsoft",
        "Exxon Mobil",
        "Pfizer",
        "Citigroup",
        "General Electric",
        "Walmart",
        "Intel",
        "Cisco Systems",
        "Johnson & Johnson",
        "IBM",
        "AIG",
        "Berkshire Hathaway",
        "Procter & Gamble",
        "Coca-Cola",
        "Bank of America",
        "Wells Fargo",
        "Paramount Global",
        "Merck",
        "Chevron",
        "Verizon"
    ]
}

data_2009 = {
    'Company Name':[
        "Exxon Mobil",
        "Walmart",
        "Procter & Gamble",
        "Microsoft",
        "Johnson & Johnson",
        "Berkshire Hathaway",
        "Chevron",
        "AT&T",
        "General Electric",
        "JPMorgan Chase",
        "Pfizer",
        "IBM",
        "Coca-Cola",
        "Wells Fargo",
        "Alphabet",
        "Cisco Systems",
        "Verizon",
        "Oracle",
        "Philip Morris Int.",
        "PepsiCo"
    ]
}

data_2014 = {
    'Company Name':[
        "Apple",
        "Exxon Mobil",
        "Alphabet",
        "Microsoft",
        "Berkshire Hathaway",
        "Johnson & Johnson",
        "Walmart",
        "Chevron",
        "Wells Fargo",
        "Procter & Gamble",
        "General Electric",
        "JPMorgan Chase",
        "IBM",
        "Pfizer",
        "Amazon",
        "Coca-Cola",
        "Oracle",
        "Bank of America",
        "Citigroup",
        "Verizon"
    ]
}

data_2019 = {
    'Company Name':[
        "Microsoft",
        "Apple",
        "Amazon",
        "Alphabet",
        "Berkshire Hathaway",
        "Meta/Facebook",
        "Johnson & Johnson",
        "JPMorgan Chase",
        "Visa",
        "Exxon Mobil",
        "Walmart",
        "UnitedHealth",
        "Bank of America",
        "Pfizer",
        "Verizon",
        "Procter & Gamble",
        "Intel",
        "Wells Fargo",
        "Chevron",
        "Coca-Cola"
    ]
}

data_2024 = {
    'Company Name': [
        "Apple",
        "Microsoft",
        "Alphabet",
        "Amazon",
        "NVIDIA",
        "Meta/Facebook",
        "Tesla",
        "Berkshire Hathaway",
        "Eli Lilly",
        "Visa",
        "Broadcom",
        "JPMorgan Chase",
        "UnitedHealth",
        "Walmart",
        "Exxon Mobil",
        "Mastercard",
        "Johnson & Johnson",
        "Procter & Gamble",
        "Home Depot"
    ]
}

def left_join(data_year, df_independent):
    df_year = pd.DataFrame(data_year)
    df_merged = pd.merge(df_year, df_independent, on='Company Name', how='left')
    #print(df_merged)
    return df_merged

def geoJsonTransformer (dataframe, timestamp):

    dataframe[['Latitude', 'Longitude']] = dataframe['Coordinates'].str.split(',', expand=True).astype(float)

    timestamp_str = timestamp.strftime('%Y-%m-%d')

    dataframe['Time'] = timestamp_str

    gdf = gpd.GeoDataFrame(dataframe, geometry=gpd.points_from_xy(dataframe.Longitude, dataframe.Latitude))

    geojson_data = json.loads(gdf.to_json())

    # for feature, time in zip(geojson_data['features'], df['Time']):
    #     feature['properties']['time'] = time.strftime('%Y-%m-%d')

    # for feature in geojson_data['features']:
    #     feature['properties']['time'] = timestamp_str
    
    return geojson_data

def write_json_file(path, geojson_data):

    file_path = path

    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
            existing_data['features'].extend(geojson_data['features'])
    else:
        existing_data = geojson_data

    with open(file_path, 'w') as f:
        json.dump(existing_data, f)


dataframe_1990 = left_join(data_1990, df_49)
dataframe_1994 = left_join(data_1994, df_49)
dataframe_1999 = left_join(data_1999, df_49)
dataframe_2004 = left_join(data_2004, df_49)
dataframe_2009 = left_join(data_2009, df_49)
dataframe_2014 = left_join(data_2014, df_49)
dataframe_2019 = left_join(data_2019, df_49)
dataframe_2024 = left_join(data_2024, df_49)

geojson_1990 = geoJsonTransformer(dataframe_1990, datetime(1990, 1, 1))
geojson_1994 = geoJsonTransformer(dataframe_1994, datetime(1994, 1, 1))
geojson_1999 = geoJsonTransformer(dataframe_1999, datetime(1999, 1, 1))
geojson_2004 = geoJsonTransformer(dataframe_2004, datetime(2004, 1, 1))
geojson_2009 = geoJsonTransformer(dataframe_2009, datetime(2009, 1, 1))
geojson_2014 = geoJsonTransformer(dataframe_2014, datetime(2014, 1, 1))
geojson_2019 = geoJsonTransformer(dataframe_2019, datetime(2019, 1, 1))
geojson_2024 = geoJsonTransformer(dataframe_2024, datetime(2024, 1, 1))


write_json_file('company_after1990.geojson', geojson_1990)
write_json_file('company_after1990.geojson', geojson_1994)
write_json_file('company_after1990.geojson', geojson_1999)
write_json_file('company_after1990.geojson', geojson_2004)
write_json_file('company_after1990.geojson', geojson_2009)
write_json_file('company_after1990.geojson', geojson_2014)
write_json_file('company_after1990.geojson', geojson_2019)
write_json_file('company_after1990.geojson', geojson_2024)
