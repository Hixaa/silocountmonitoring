import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
import signal
GPIO.setmode(GPIO.BCM)



class CountMonitor:
    def __init__(self):
        self.__Channel= 4
        #Things to add in config file
        self.__clientId = 1
        self.__uid = 2
        self.__count= 0
        self.__data = list() #Empty list named as data
        GPIO.setup(self.__Channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.__newchannelState = False
        self.__lastchannelState = GPIO.input(self.__Channel)
        GPIO.add_event_detect(self.__Channel, GPIO.BOTH, callback=self.__countCallback, bouncetime= 1)

    def __Counting(self):
        self.__count += 1
        silo = {"DateTime":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"ClientId":str(self.__clientId),"UID":str(self.__uid),"Count":str(self.__count)}
        #silo = '{"DateTime":"%s","ClientId":"%d","UID":"%d","Count":"%d"}'%(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.__clientId,self.__uid,self.__count)
        #self.__data.append(silo)
        print("[+]",silo)

    def __countCallback(self, channel):
        self.__newchannelState = GPIO.input(self.__Channel)

        if self.__newchannelState != self.__lastchannelState:
            if self.__newchannelState == GPIO.HIGH:
                self.__Counting()
            self.__lastchannelState = self.__newchannelState

    def cleanup(self):
        GPIO.cleanup()

    def run(self):
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup()


if __name__ == "__main__":
    a = CountMonitor()
    a.run()

