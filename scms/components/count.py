import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from datetime import datetime
from time import sleep
from components.appConfig import Config
from components.statusLeds import statusLED
from components.cloudService import CloudService

class Count:
    def __init__(self):
        self.__config = Config()
        self.__ledStat = statusLED()
        self.__cloud = CloudService()
        
        print("Godown Stat: ",self.__config.isGodown())

        if(self.__config.isGodown()):
            self.__Channel = self.__config.GPIO_GodownChannel()
        else:
            self.__Channel = self.__config.GPIO_SiloChannel()
        print("Channel: ",self.__Channel)

        self.__count = self.__config.count()
        self.__ClientId = self.__config.clientId()
        self.__deviceId = self.__config.deviceId()

        self.__lastChannelState = False
        self.__data = list()
        self.__params = dict()

        GPIO.setup(self.__Channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.__Channel, GPIO.BOTH, callback = self.__CountCallback, bouncetime = 1)

    def __counting(self):
        self.__count += 1
        self.__params = {"DateTime":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"ClientId":str(self.__ClientId),"DeviceId":str(self.__deviceId),"Count":str(self.__count),"Param1":"0","Param2":"0","Param3":"0"}
        #print("[+]",self.__params)

        self.__config.setCount(self.__count)
        self.__ledStat.count_Show()
        self.__data.append(self.__params)

    def __CountCallback(self, channel):
        self.__newChannelState = GPIO.input(self.__Channel)
        if self.__newChannelState != self.__lastChannelState:
            if self.__newChannelState == GPIO.HIGH:
                self.__counting()
            self.__lastChannelState = self.__newChannelState

    def countSync(self):
        while True:
            if(len(self.__data) > 0):
                d = self.__data.pop(0)
                print("[+] Syncing!!!---> Started")
                self.__cloud.pushCount(d)
            sleep(0.1)
    
    def close(self):
        GPIO.cleanup()
        





