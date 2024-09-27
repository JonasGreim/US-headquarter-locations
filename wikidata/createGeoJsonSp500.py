import json


def convert_to_geojson_sp500(input_file, output_file):
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
                "market_cap": item["market_cap"],
                "year": item["year"],
                "qid": item["qid"],
                "wikiDataName": item["wikiDataName"]
            }
        }
        geojson["features"].append(feature)

    with open(output_file, 'w') as f:
        json.dump(geojson, f, indent=4)


# Example usage
convert_to_geojson_sp500('./sp500RankingWithCoordinates.json', './sp500Companies.geojson')