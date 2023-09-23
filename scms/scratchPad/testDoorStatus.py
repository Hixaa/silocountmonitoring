import RPi.GPIO as GPIO
import os
import signal
from datetime import datetime
import time
from time import sleep
import json
GPIO.setmode(GPIO.BCM)

class testDoor:
    def __init__(self):
        self.__currDir = os.getcwd()
        self.__fileName = self.__currDir+'/doorlog.txt'
        self.__door = 4
        self.__clientId = 1
        self.__uid = 2
        self.__data = list() #Empty list as data
        self.__doorData = dict() #Empty dict as silo
        self.__newdoorState = False
        #self.__existingdata = ''
        #self.__combinedData = ''
        self.__param = '' 
        GPIO.setup(self.__door, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        #self.__prev_state = GPIO.input(self.__door)
        #self.__doorState = GPIO.input(self.__door)
        self.__lastdoorState = GPIO.input(self.__door)
        #self.__debounceTime = time.time()
        #self.__debounceDelay = 0.2
        GPIO.add_event_detect(self.__door, GPIO.BOTH, callback = lambda channel:self.__doorCallback(channel,self.__param), bouncetime = 50)
        #GPIO.remove_event_detect(self.__door)
        #GPIO.add_event_detect(self.__door, GPIO.FALLING, callback = lambda channel:self.__doorCallbackFalling(channel,fallingParam), bouncetime = 200)
        #GPIO.add_event_detect(self.__door, GPIO.FALLING, callback = self.__doorCallback, bouncetime = 200)
        
    def __doorOpen(self, param):
        self.__param = 1
        self.__doorData = {"DateTime":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"ClientID":str(self.__clientId),"UID":str(self.__uid),"Status":str(self.__param)}
        with open(self.__fileName, 'a+') as fileP:
            fileP.seek(os.SEEK_END)
            #self.__data.append(self.__silo) 
            fileP.write(json.dumps(self.__doorData) + "\n")
            print("[+]",self.__doorData)
            
    def __doorClose(self, param):
        self.__param = 0
        self.__doorData = {"DateTime":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"ClientID":str(self.__clientId),"UID":str(self.__uid),"Status":str(self.__param)}
        with open(self.__fileName, 'a+') as fileP:
            fileP.seek(os.SEEK_END)
            #self.__data.append(self.__silo) 
            fileP.write(json.dumps(self.__doorData) + "\n")
            print("[+]",self.__doorData)

    def __doorCallback(self, channel, param):
        self.__newdoorState = GPIO.input(self.__door)

        if self.__newdoorState != self.__lastdoorState:
            if self.__newdoorState == GPIO.HIGH:
                self.__doorOpen(self)
            else:
                self.__doorClose(self)
            self.__lastdoorState = self.__newdoorState
    
    def run(self):
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup()

    def cleanup(self):
        GPIO.cleanup()

           


if __name__ == "__main__":
    a = testDoor()
    a.run()
