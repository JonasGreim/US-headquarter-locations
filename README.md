# Company Headquarters in the USA
The objective of this university project is to demonstrate how the US industry has changed over time, as represented by the major corporate headquarters included in the SP500 or Fortune 500 indices.
The geographical distribution of these headquarters and their respective industry sectors are presented on a map where users can select different years and choose between two indexes.


## Data
This repository is the data scraping and processing part of the project. 

- The historical company rankings (SP500 and Fortune 500) over many years are scraped from websites.
- The headquarters locations are then retrieved from the Wikidata API. 
- The data is then processed and converted into a GeoJSON format for the map.

## Visualisation
The visualization/mapping of the headquarters locations data can be found in [this repository](https://github.com/JonasGreim/leaflet-map-project).

The final visualization result can be found as website [here](https://jonasgreim.github.io/leaflet-map-project/).

## Getting Started:
To get a local copy up and running, follow these simple steps.
### Installation
1. Set up a virtual python environment (Python version >= 3.10):
```bash
python3 -m venv venv
source venv/bin/activate
```
2. Install the required packages:
```bash
- pip3 install -r requirements.tx
```

### Run scraper (scrapy):
**Info:** The scraper only searches the existing annual SP500 and Fortune 500 rankings of the specified websites. There are no headquarters locations in the rankings.

go into the scrapy folder:

```bash
cd topUsCompaniesLocationScraper
```

Fortune500:
```bash 
scrapy crawl us-companies -o fortune500.json
```

SP500:
```bash
scrapy crawl us-companies-sp500 
```

### Official Wikipedia API
First we tried to preserve the headquarters locations of the companies with the official Wikipedia API.

Problem: 
- You get the same data as you would scrape the wiki page (same thing with python wiki api wrappers)
- The HTML structure of Wikipedia company articles is inconsistent -> cannot scrape the data (f.e. the fact table)
- We also tried the new Wikipedia Geosearch API ([link](https://www.mediawiki.org/wiki/API:Geosearch#Example_1:_Obtain_coordinates))
  - But only a few wikipedia pages have coordinates 

run:
```bash 
cd apiWiki
python3 apiWiki.py
```

### Wikidata API

To access the headquarters location data of the companies, we used the Wikidata API.

Explain the data processing


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

- map unique companies to ranking (mapUniqueCompaniesToRanking.py)
- converte to geojson (createGeoJson.py)





wikidata websearch is different then the api search (worse)
difficult names -> bad search (alphabet, apple) -> data also not right company names
tried also with completly chatgpt -> wrong coordinates


TODO:
- read me hübsch machen
- Alles ordnen, strukturieren -> folder data, foder helper methods folder
- alle files nochmal durchgehen, kommentare, input output fixen (wikidata)
- anzahl von fails von fortune500 notieren
- venv löschen
- topUsCompaniesLocationScraper umbenennen -> scraped keine location nur company rankings



### Credits 
- Jiacheng Lang & Jonas Greim
- The university course "Computational Spatial Humanities," taught by Dr. Thomas Efer at the University of Leipzig