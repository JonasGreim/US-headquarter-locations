import requests
import json

# TODO checkout https://www.mediawiki.org/wiki/API:Geosearch#Example_1:_Obtain_coordinates
# https://www.mediawiki.org/wiki/Special:ApiSandbox

# search -> scrape -> city -> geosearch -> coordinates
# search -> scrape -> geosearch (with python wrapper)

# api explained
# https://github.com/mudroljub/wikipedia-api-docs

## search
# gsrsearch = intitle:belgrade(word "belgrade" is in title)
# gsrsearch = prefix:belgrade(article's title starts with the word "belgrade")

searchTerm = "\"apple inc\""
searchTerm2 = "apple|inc"
searchTerm3 = "apple_company."
seachUrl = "https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=" + searchTerm + "&exintro=&prop=extracts|pageimages&format=json"

# use titel from search result -> spaces = _
contentUrl = "https://en.wikipedia.org/w/api.php?action=query&titles=Apple_Inc.&prop=extracts|pageimages|info&pithumbsize=400&inprop=url&redirects=&format=json&origin=*"


response = requests.get(seachUrl)
response = json.loads(response.text)
print(json.dumps(response, indent=4))

# check if python wiki wrapper -> geoSearch cities directly
# extract cities -> wiki geosearch -> geo information
