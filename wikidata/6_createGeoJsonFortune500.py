import json

# create a geojson file from Fortune 500 json data


def convert_to_geojson(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for item in data:
        coordinates = item["headquarterCoordinates"].replace("Point(", "").replace(")", "").split()
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(coordinates[0]), float(coordinates[1])]
            },
            "properties": {
                "rank": item["rank"],
                "company": item["company"],
                "revenues": item["revenues"],
                "profits": item["profits"],
                "year": item["year"],
                "qid": item["qid"],
                "wikiDataName": item["wikiDataName"],
                "industry": item["industry"]
            }
        }
        geojson["features"].append(feature)

    with open(output_file, 'w') as f:
        json.dump(geojson, f, indent=4)


convert_to_geojson('./data_fortune500/uniqueCompaniesWithQidsAndWithIndustrySector.json', './data_fortune500/x_sp500Companies.geojson')
