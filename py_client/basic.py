import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={'word':'Hello world'}) 
print(get_response.json())
