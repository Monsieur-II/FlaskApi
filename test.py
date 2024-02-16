import requests
import json

BASE = "http://127.0.0.1:5000/"
data = [{"likes": 10, "name": "Tim", "views": 10000},
        {"likes": 10, "name": "How to make REST API", "views": 10000},
        {"likes": 10, "name": "Tim", "views": 10000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(response.json())

data = {"likes": 99, "name": "Tim", "views": 10000}
json_data = json.dumps(data)
headers = {'Content-Type': 'application/json'}

response = requests.patch(BASE + "video/2", data=json_data, headers=headers)
print(response.json())
