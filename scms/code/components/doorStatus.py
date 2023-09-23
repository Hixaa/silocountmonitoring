import RPi.GPIO as GPIO
import os
from components.appConfig import Config
from datetime import datetime
import json
import requests
GPIO.setmode(GPIO.BCM)

class Door:
    def __init__(self):
        self.__config = Config()
        self.__currDir = os.getcwd()
        self.__fileName = self.__currDir+'/doorStat.log'

        self.__clientId = self.__config.clientId()
        self.__deviceId = self.__config.deviceId()

        self.__doorSignal = self.__config.GPIO_doorChannel()

        self.__data = list() #Empty list as data
        self.__doorData = dict() #Empty dict as silo
        self.__newdoorState = False
        self.__param = ""

        self.__doorStatURL = self.__config.urlDoor()
        self.__headers = {'Content-Type':'application/json'}

        GPIO.setup(self.__doorSignal, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.__lastdoorState = GPIO.input(self.__doorSignal)
        GPIO.add_event_detect(self.__doorSignal, GPIO.BOTH, callback = lambda channel:self.__doorCallback(channel,self.__param), bouncetime = 1)
        
    def __doorOpen(self, param):
        self.__param = "Open"
        self.__doorData = {"DateTime":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"ClientId":str(self.__clientId),"DeviceId":str(self.__deviceId),"DoorDeviceStatus":self.__param}
        payload = json.dumps(self.__doorData)
        resp = requests.request("POST", self.__doorStatURL, headers = self.__headers, data=payload)
        if(resp.status_code == 200):
            print("[+] Door Status Uploaded - Open")
        else:
            print("[-] Door Upload Failed - Open")
        
        with open(self.__fileName, 'a+') as fileP:
            fileP.seek(os.SEEK_END)
            fileP.write(json.dumps(self.__doorData) + "\n")
            
    def __doorClose(self, param):
        self.__param = "Close"
        self.__doorData = {"DateTime":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"ClientId":str(self.__clientId),"DeviceId":str(self.__deviceId),"DoorDeviceStatus":self.__param}
        payload = json.dumps(self.__doorData)
        resp = requests.request("POST", self.__doorStatURL, headers = self.__headers, data=payload)
        if(resp.status_code == 200):
            print("[+] Door Status Uploaded - Close")
        else:
            print("[-] Door Upload Failed - Close")

        with open(self.__fileName, 'a+') as fileP:
            fileP.seek(os.SEEK_END)
            fileP.write(json.dumps(self.__doorData) + "\n")

    def __doorCallback(self, channel, param):
        self.__newdoorState = GPIO.input(self.__doorSignal)

        if self.__newdoorState != self.__lastdoorState:
            if self.__newdoorState == GPIO.HIGH:
                self.__doorOpen(self)
            else:
                self.__doorClose(self)
            self.__lastdoorState = self.__newdoorState

    def close(self):
        GPIO.cleanup()

