# Get data from HK open data
# https://data.gov.hk/tc-data/dataset/hk-dpo-datagovhk1-carpark-info-vacancy/resource/f4c792c6-071c-4a64-888b-afeea33d5ad7

import requests
import json

with open("config.json") as config_file:
    config = json.load(config_file)

api = config["api"]
output = config["output"]

x = requests.get(api["basic_info"])
print(x.status_code)
jsonObj = json.loads(x.text.encode('utf8')[3:].decode('utf8'))

with open(output["parking_lot"], "w") as file:
    json.dump(jsonObj["car_park"], file)

y = requests.get(api["vacancy"])
jsonObj = json.loads(y.text)

with open(output["realtime"], "w") as f:
    json.dump(jsonObj["results"], f)

print("Get data successfully.")