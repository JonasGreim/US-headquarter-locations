# US headquarter locations
#### University Leipzig, SoSe 2024, Computational Spatial Humanities
#### Jiacheng Lang, Jonas Greim

### Task:
US headquarter locations of big companies (Fortune 500 / Big Stock market players?) for the last 100 years. 
Look into centers of industrial developmnt (Steel & Cars --> Silicon Valley?), track free market developments geographically


### Setup:
virtual python environment:
- python3 -m venv venv
- source venv/bin/activate

install packages:
- pip3 install scrapy
- pip3 install json

### Run scraper (scrapy):
The scraper only searches the existing annual SP500 and Fortune 500 rankings of the specified websites. There are no headquarters locations in the rankings.

go into the scrapy folder:

- cd topUsCompaniesLocationScraper

- Fortune500:
  - scrapy crawl us-companies -o fortune500.json

- S&P500:
  - scrapy crawl us-companies-sp500 

### apiWiki
First try to preserve the headquarters locations of the companies with the offical wikipedia api.

- pip3 install requests
- pip3 install json

run:
- python3 apiWiki.py

Problem: 
- You get the same data as you would scrape the wiki page (with the official api and also with python wikiapi wrapper)
- Html data is completely unstructured -> cannot scrape the data
- We also tried the new wikipedia geosearch api ([link](https://www.mediawiki.org/wiki/API:Geosearch#Example_1:_Obtain_coordinates))
  - But only a few wikipedia pages have coordinates 
