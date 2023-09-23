import RPi.GPIO as GPIO
from time import sleep
from components.appConfig import Config
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class statusLED:
    def __init__(self):
        self.__config = Config()
        self.__sysReady = self.__config.GPIO_sysReady()
        self.__countStat = self.__config.GPIO_countStat()
        self.__dataUpload = self.__config.GPIO_dataUploadStat()
        GPIO.setup(self.__sysReady,GPIO.OUT)
        GPIO.setup(self.__countStat,GPIO.OUT)
        GPIO.setup(self.__dataUpload,GPIO.OUT)
        GPIO.output(self.__sysReady,False)
        GPIO.output(self.__countStat,False)
        GPIO.output(self.__dataUpload,False)

    def sysReady_Show(self,stat):
        GPIO.output(self.__sysReady,stat)

    def count_Show(self):
        for i in [0,2]:
            GPIO.output(self.__countStat,True)
            sleep(0.05)
            GPIO.output(self.__countStat,False)
            sleep(0.05)
    
    def dataUpload_Show(self):
        for i in [0,3]:
            GPIO.output(self.__dataUpload,True)
            sleep(0.05)
            GPIO.output(self.__dataUpload,False)
            sleep(0.05)

    def Error_Show(self):
        for i in [0,3]:
            GPIO.output(self.__sysReady,True)
            GPIO.output(self.__countStat,True)
            GPIO.output(self.__dataUplaod,True)
            sleep(0.05)
            GPIO.output(self.__sysReady,False)
            GPIO.output(self.__countStat,False)
            GPIO.output(self.__dataUplaod,False)
            sleep(0.05)
    
    def close(self):
        GPIO.output(self.__sysReady,False)
        GPIO.output(self.__countStat,False)       
        GPIO.output(self.__dataUpload,False)
        GPIO.cleanup()
        

