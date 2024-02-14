import requests

BASE = "http://127.0.0.1:5000/"
data = [{"likes": 10, "name": "Tim", "views": 10000},
        {"likes": 10, "name": "How to make REST API", "views": 10000},
        {"likes": 10, "name": "Tim", "views": 10000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(response.json())

response = requests.patch(BASE + "video/2", {})
print(response.json())
