import requests, json

url_name = 'http://httpbin.org/post'
data = {"Name": "John"}
data_json = json.dumps(data)
headers = {'Content-Type': 'application/json'}
response = requests.post(url_name, data=data_json, headers=headers)
print(response)
