import json
import numpy as np
from queryCompaniesQID import request_query_companies_qid
from queryHeadquarters import queryHeadquarters

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def extract_unique_companies(data, start_year, end_year):
    years = np.arange(start_year, end_year + 1)
    string_years = [str(year) for year in years]
    unique_companies = set()
    for year in string_years:
        for company in data[year]:
            unique_companies.add(company)
    return list(unique_companies)

def fetch_company_qids(companies):
    results = []
    counter = 0
    for company in companies:
        a = request_query_companies_qid(company)
        if a is None:
            counter += 1
            continue
        name = a['itemLabel']['value']
        qid = a['item']['value'].split('/')[-1]
        results.append({'Name': name, 'QID': qid})
    return results, counter

def main():
    data = load_data('companies_by_year.json')
    unique_companies = extract_unique_companies(data, 1990, 2024)
    
    results, counter = fetch_company_qids(unique_companies)
    print('Total number of companies without QIDs:', counter)
    print(results)
    #[{'Name': 'Verizon', 'QID': 'Q919641'}, {'Name': 'Broadcom', 'QID': 'Q555925'}, {'Name': 'Coca-Cola', 'QID': 'Q121337069'}, {'Name': 'IBM', 'QID': 'Q30289967'}, {'Name': 'Boeing', 'QID': 'Q66'}, {'Name': 'Berkshire Hathaway', 'QID': 'Q121307826'}, {'Name': 'Eli Lilly', 'QID': 'Q43896148'}, {'Name': 'Apple', 'QID': 'Q312'}, {'Name': 'AT&T', 'QID': 'Q35476'}, {'Name': 'Citigroup', 'QID': 'Q219508'}, {'Name': 'PepsiCo', 'QID': 'Q334800'}, {'Name': 'Wells Fargo', 'QID': 'Q744149'}, {'Name': 'Mastercard', 'QID': 'Q489921'}, {'Name': 'Procter & Gamble', 'QID': 'Q212405'}, {'Name': 'DuPont', 'QID': 'Q221062'}, {'Name': 'Amazon', 'QID': 'Q456085'}, {'Name': 'Pfizer', 'QID': 'Q206921'}, {'Name': 'Amgen', 'QID': 'Q470517'}, {'Name': '3M', 'QID': 'Q159433'}, {'Name': 'Bank of America', 'QID': 'Q487907'}, {'Name': 'Tesla', 'QID': 'Q1548225'}, {'Name': 'Qualcomm', 'QID': 'Q544847'}, {'Name': 'Walmart', 'QID': 'Q483551'}, {'Name': 'Johnson & Johnson', 'QID': 'Q102543513'}, {'Name': 'Paramount Global', 'QID': 'Q76846862'}, {'Name': 'JPMorgan Chase', 'QID': 'Q192314'}, {'Name': 'Merck', 'QID': 'Q30269113'}, {'Name': 'Oracle', 'QID': 'Q30292006'}, {'Name': 'General Electric', 'QID': 'Q54173'}, {'Name': 'Microsoft', 'QID': 'Q2283'}, {'Name': 'Intel', 'QID': 'Q121270883'}, {'Name': 'Bristol-Myers Squibb', 'QID': 'Q266423'}, {'Name': 'PayPal', 'QID': 'Q483959'}]
    
    qid_list = [result['QID'] for result in results]
    print(qid_list)
    #['Q919641', 'Q555925', 'Q121337069', 'Q30289967', 'Q66', 'Q121307826', 'Q43896148', 'Q312', 'Q35476', 'Q219508', 'Q334800', 'Q744149', 'Q489921', 'Q212405', 'Q221062', 'Q456085', 'Q206921', 'Q470517', 'Q159433', 'Q487907', 'Q1548225', 'Q544847', 'Q483551', 'Q102543513', 'Q76846862', 'Q192314', 'Q30269113', 'Q30292006', 'Q54173', 'Q2283', 'Q121270883', 'Q266423', 'Q483959']

    for qid in qid_list:
        queryHeadquarters(qid)

if __name__ == "__main__":
    main()