import requests

url = "https://api.itbook.store/1.0/search/mongodb"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
