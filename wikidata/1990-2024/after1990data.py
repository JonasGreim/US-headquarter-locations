import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://www.finhacker.cz/top-20-sp-500-companies-by-market-cap"

# Send a GET request to the webpage
response = requests.get(url)
encoding = response.apparent_encoding
response.encoding = encoding
bd_soup = BeautifulSoup(response.text,"lxml")
pretty_html = bd_soup.prettify()

with open('parsed_content_after1990.txt', 'w', encoding='utf-8') as file:
    file.write(pretty_html)

print("HTML content has been written to parsed_content.txt")