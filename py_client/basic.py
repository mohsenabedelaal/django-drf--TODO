import requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint,json={"query":"Hello World"}) # HTTP Request
print(get_response.json()) # print raw text response 

