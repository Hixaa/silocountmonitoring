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
        self.__count = 0
        #self.__stateChange = False
        self.__data = list() #Empty list named as data
        self.__prevState = GPIO.input(self.__Channel)
        GPIO.setup(self.__Channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def run(self):
        try:
            while True:
                #GPIO.wait_for_edge(self.__Channel,GPIO.RISING)
                #self.__Channel.wait_for_press()
                #self.__Channel.wait_for_release()
                #GPIO.wait_for_edge(self.__Channel,GPIO.RISING)
                #GPIO.wait_for_edge(self.__Channel,GPIO.FALLING)

                self.__currState = GPIO.input(self.__Channel)
                #if(self.__prev_state != self.__curr_state):
                 #   self.__stateChange = True
                  #  self.__prev_state = self.__curr_state

                #if(self.__stateChange == True and self.__curr_state == True):
                if(self.__prevState == LOW and self.__currState == HIGH)
                    sleep(0.5) #debounce
                    self.__count += 1
                    silo = {"DateTime":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"ClientId":str(self.__clientId),"UID":str(self.__uid),"Count":str(self.__count)}
                    #silo = '{"DateTime":"%s","ClientId":"%d","UID":"%d","Count":"%d"}'%(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.__clientId,self.__uid,self.__count)
                    #self.__data.append(silo)
                    print("[+]",silo)
                    #self.__stateChange = False

        except KeyboardInterrupt:
            GPIO.cleanup()


if __name__ == "__main__":
    a = CountMonitor()
    a.run()

