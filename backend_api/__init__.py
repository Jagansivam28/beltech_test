import csv
from collections import defaultdict

def make_json():
    csvFilePath = "Sub_Urban_Rail_Chennai.csv"
    # create a dictionary
    json_data = []
    stations = defaultdict(list)
    connection_line = defaultdict(list)
    stations_code = defaultdict(list)
    connection_line_dist = defaultdict(dict)


    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for i,row in enumerate(csvReader):
            json_data.append(row)
            row["Station"] = row["Station"].split("RS")[0].lower().strip()
            stations[row["Station"]].append(row)
            row["Station Code"] = row["Station Code"].lower()
            connection_line[row["Connection"]].append(row["Station Code"])
            connection_line_dist[row["Connection"]][row["Station Code"]] = row["Distance in Kms"]

    return json_data,stations,connection_line,stations_code,connection_line_dist


json_all_data,stations_wise,connection_line_wise,stations_code,connection_line_dist = make_json()
