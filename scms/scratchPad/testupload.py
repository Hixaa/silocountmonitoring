import requests
import json

url = 'https://silo.growbean.in/example-api-insert-device-bulk-count.php'

data = ['{"DateTime":"2023-08-09 12:52:37","ClientId":"2","DeviceId":"2","Count":"200"}','{"DateTime":"2023-08-09 12:52:37","ClientId":"2","DeviceId":"2","Count":"200"}']

jsonObj = json.dumps(data)

x= requests.post(url, json = data)

print(jsonObj)
print(x)
