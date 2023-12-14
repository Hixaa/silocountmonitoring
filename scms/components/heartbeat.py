import json
import requests
from components.appConfig import Config
from datetime import datetime
from time import sleep
import threading

class Heartbeat:
    def __init__(self):
        self.__config = Config()
        self.__urlHeartbit = self.__config.urlHeartbeat()
        self.__clientId = self.__config.clientId()
        self.__deviceId = self.__config.deviceId()
        self.__heartBeat_Interval = self.__config.heartbeatInterval()
        self.__aliveStatus = "Alive"
        self.__headers = {'Content-Type' : 'application/json'}
        self.__heartBeatThread = threading.Timer(self.__heartBeat_Interval,self.__sendBeat)
        self.__heartBeatThread.start()
        
    def __sendBeat(self):
        try:
            payload = json.dumps({"DateTime":str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),"ClientId":str(self.__clientId),"DeviceId":str(self.__deviceId),"AliveStatus":str(self.__aliveStatus)})
            #print("HeartBeat: Payload: ",payload)
            self.__resp = requests.request("POST", self.__urlHeartbit , headers = self.__headers, data = payload)
        
            # if self.__resp.status_code == 200:
            if(self.__resp.json().get("status") == "1"):    #CHANGED
                print("[+]","HeartBeat - Heartbeat sent successfully!")
            else:
                print("[-]","HeartBeat - Network issue!")
        except:
            print("[-]","Heart Beat: Internet Connectivity Failed!")
        self.__heartBeatThread.cancel()
        self.__heartBeatThread = threading.Timer(self.__heartBeat_Interval,self.__sendBeat)
        self.__heartBeatThread.start()



