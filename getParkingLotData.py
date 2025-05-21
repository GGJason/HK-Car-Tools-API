# Get data from HK open data
# https://data.gov.hk/tc-data/dataset/hk-dpo-datagovhk1-carpark-info-vacancy/resource/f4c792c6-071c-4a64-888b-afeea33d5ad7

import requests
import json

x = requests.get('https://resource.data.one.gov.hk/td/carpark/basic_info_all.json')
print(x.status_code)
jsonObj = json.loads(x.text.encode('utf8')[3:].decode('utf8'))

with open("data/parkingLot.json", "w") as file:
    json.dump( jsonObj["car_park"],file)


y = requests.get('https://api.data.gov.hk/v1/carpark-info-vacancy?data=vacancy&lang=zh_TW')
jsonObj = json.loads(y.text)

with open("data/realtime.json", "w") as f:
    json.dump( jsonObj["results"],f)

print("Get data successfully.")