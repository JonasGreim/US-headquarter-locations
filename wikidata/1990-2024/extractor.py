from bs4 import BeautifulSoup
import json

# Function to parse and extract company names by year
def extract_companies_by_year(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    data = {}

    # Find all divs with the specific class
    divs = soup.find_all('div', class_='w3-container w3-border tab')
    for div in divs:
        year_id = div.get('id')
        if year_id and year_id.endswith('y'):
            year = year_id[:-1]
            companies = []

            # Extract company names within this div
            for company_div in div.find_all('div'):
                company_span = company_div.find('span')
                if company_span:
                    company_name = company_div.contents[-1].strip()
                    companies.append(company_name)

            data[year] = companies

    return data

# Load the HTML content from the provided file
file_path = 'parsed_content_after1990.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Extract companies by year
companies_by_year = extract_companies_by_year(html_content)

# Save the extracted data to a text file
output_file_path = 'companies_by_year.json'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(companies_by_year, output_file, indent=4)

print(f"Extracted company names have been written to {output_file_path}")