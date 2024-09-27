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
- pip3 install -r requirements.tx

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

run:
- python3 apiWiki.py

Problem: 
- You get the same data as you would scrape the wiki page (with the official api and also with python wikiapi wrapper)
- Html data is completely unstructured -> cannot scrape the data
- We also tried the new wikipedia geosearch api ([link](https://www.mediawiki.org/wiki/API:Geosearch#Example_1:_Obtain_coordinates))
  - But only a few wikipedia pages have coordinates 


### wikidata
- Try to get the headquarters locations of the companies with the wikidata api.

- create a unique company list from the ranking (initUniqueComaniesJson.py) -> map later location to json
- dataCompanyName, searchCompanyName, wikidataCompanyName, qid -> compare and correct manually

- First have to get the wikidata page qid (id) of the company -> text search with unique company names of ranking
- get qid -> if no qid found -> manually change company name (5/49)
- getAllQidsThroughCompanyNameList.py -> extract unique names of ranking -> text search -> first result: add qid + wikidata name to json
- (didn't work with tag filtering -> incmplete data) -> only text search in wikidata title and synonyms
- compare -> search name and wikidata name manually -> correct -> if not change the company name in the json 

- then retrieve the wikidata page with the qid (getAllLocationDataThroughQIDList.py) 
- try to get the headquarters location of the company -> no coordinates found -> change name -> run qid search again
- -> trail and error -> 15  of  49 failed


getAllIndustryDataThroughQIDList.py
-> run industry sector search -> 1  of  49 failed -> ask chatgpt to our 10 sectors

convert to geojson





wikidata websearch is different then the api search (worse)
difficult names -> bad search (alphabet, apple) -> data also not right company names


TODO:
- read me hübsch machen
- Alles ordnen, strukturieren -> folder data, foder helper methods folder
- alle files nochmal durchgehen, kommentare, input output fixen (wikidata)
- anzahl von fails von fortune500 notieren
- venv löschen
- frontend übertragen -> anpassungen machen



