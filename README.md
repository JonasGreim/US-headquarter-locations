# US headquarter locations
#### University Leipzig, SoSe 2024, Computational Spatial Humanities
#### Jiacheng Lang, Jonas Greim

### Task:
US headquarter locations of big companies (Fortune 500 / Big Stock market players?) for the last 100 years. 
Look into centers of industrial developmnt (Steel & Cars --> Silicon Valley?), track free market developments geographically

scrape this website: https://money.cnn.com/magazines/fortune/fortune500_archive/full/1955/


### Setup:
virtual python environment:
- python3 -m venv venv
- source venv/bin/activate

install packages:
- pip3 install scrapy

### Run scraper:
go into the scraper folder:

store in json: 
- scrapy crawl us-companies -o items.json

store in csv:
- scrapy crawl us-companies -o items.csv
