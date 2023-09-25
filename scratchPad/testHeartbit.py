import requests
import json
from datetime import datetime
import time
from time import sleep

url = "http://silo.growbean.in/example-api-device-status-heartbeat.php"

payload = json.dumps({
  "DateTime": "2023-09-07 01:10:10",
  "ClientId": "16",
  "DeviceId": "6",
  "AliveStatus": "Active"
})
headers = {
  'Content-Type': 'application/json'
}

while True:
    response = requests.request("POST", url, headers=headers, data=payload)
    #value = response["status"]
    #print(value)
    if response.status_code == 200:
        print("[+]",datetime.now().strftime("%Y-%m-%d %H:%M:%S")," Heartbit sent successfully!")
    else:
        print("[-]",datetime.now().strftime("%Y-%m-%d %H:%M:%S")," Error in sending heartbit!")
    time.sleep(30)

#print(response)
