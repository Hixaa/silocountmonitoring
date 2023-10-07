import requests
import json
from requests.structures import CaseInsensitiveDict
from collections import namedtuple
from components.appConfig import Config
from components.storejson import StoreJson
from components.statusLeds import statusLED
import subprocess
from time import sleep
import threading


class CloudService:
    def __init__(self):
        self.__config = Config()
        self.__url = self.__config.url()
        self.__countURL = self.__config.urlCount()
        self.__headers = {'Content-Type':'application/json'}
        self.__storeData = StoreJson()
        self.__ledStat = statusLED()

    def __UserData(self,userData):
        return namedtuple('X', userData.keys())(*userData.values())

    def __dataFormat(self,data):
        return {"DateTime":data.DateTime,"ClientId":data.ClientId,"DeviceId":data.DeviceId,"Count":data.Count,"Param1":data.Param1,"Param2":data.Param2,"Param3":data.Param3}
        
    def pushCount(self,data):
        try:
            json_data_list = [data]    
            payload = json.dumps(json_data_list)
            print("\t\t ENTRY: ", payload)
            resp = requests.request("POST", self.__countURL, headers=self.__headers, data=payload) 
        
            if(resp.status_code == 200):
                print("[+] Successfully Added Data!")
                self.__ledStat.dataUpload_Show()
            else:
                raise Exception("Server Issue")

        except:
            self.__storeData.pushLocal(json.dumps(data))
            print("[+] Added Data Locally!!")
            print("[!] Error in Data Push. Network Issue!")

    def autoSync(self):
        while True:
            if(self.__storeData.checkAvailable_Files(recent = False) and self.__ping_server()):
                try:
                    json_data_list=[]
                    data = self.__storeData.getJsonArray()
                    for line in data:
                        d = json.loads(line.strip(),object_hook=self.__UserData)
                        json_data_list.append(self.__dataFormat(d))               
                    #print(json_data_list)

                    payload = json.dumps(json_data_list)
                    resp = requests.request("POST", self.__countURL, headers=self.__headers, data=payload)

                    # print("[+] Payload: ", payload)
                    # print("[+] Status Code: ", resp.status_code)
                    if(resp.status_code == 200):
                        print("[+] Successfully Added Data!")
                        self.__ledStat.dataUpload_Show()
                        self.__storeData.truncateFile()
                    else:
                        print("[!] AutoSync: Not Successfully Added Data! Server Issue !")
                except:
                    print("[!] AutoSync: Network Issue!")
            sleep(1)


    def __ping_server(self):
        cmd = ['ping','-c','1',self.__url]
        return subprocess.call(cmd,stdout = subprocess.DEVNULL,stderr = subprocess.STDOUT) == 0
