# importing the requests library
import requests
import json
# defining the api-endpoint 
API_ENDPOINT = "http://localhost:5000/predict"

with open("testreq.json", 'r') as j:
    data = j.read()
data = eval(data)
r = requests.get(url = "http://localhost:5000/health")
print(r.json())
r = requests.post(url = API_ENDPOINT, json = data)
print(r.json())