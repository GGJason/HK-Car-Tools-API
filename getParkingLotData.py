# Get data from HK open data
# https://data.gov.hk/tc-data/dataset/hk-dpo-datagovhk1-carpark-info-vacancy/resource/f4c792c6-071c-4a64-888b-afeea33d5ad7

import json
import os
import requests

with open("config.json") as config_file:
    config = json.load(config_file)

data_folder = config.get("data_folder", "data")
api = config["api"]
output = config["output"]

os.makedirs(data_folder, exist_ok=True)

x = requests.get(api["basic_info"])
print(x.status_code)
jsonObj = json.loads(x.text.encode('utf8')[3:].decode('utf8'))

with open(os.path.join(data_folder, output["parking_lot"]), "w") as file:
    json.dump(jsonObj["car_park"], file)

y = requests.get(api["vacancy"])
jsonObj = json.loads(y.text)

with open(os.path.join(data_folder, output["realtime"]), "w") as f:
    json.dump(jsonObj["results"], f)

print("Get data successfully.")