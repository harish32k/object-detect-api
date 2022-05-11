# importing the requests library
import requests
# defining the api-endpoint 
API_ENDPOINT = "http://0.0.0.0:5000/predict"

with open("testreq.json", 'r') as j:
    data = j.read()
data = eval(data)
r = requests.post(url = API_ENDPOINT, data = data)
print(r)