import http.client

conn = http.client.HTTPSConnection("viacep.com.br")
payload = ''
headers = {}
conn.request("GET", "/ws/13058574/json", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))