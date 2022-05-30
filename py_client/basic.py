import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint,json={"query":"Hello World"}) # HTTP Request
print(get_response.text) # print raw text response 
print(get_response.status_code) # print status response 

