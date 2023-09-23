import sys 
import threading 
from time import sleep
from components.statusLeds import statusLED
from components.cloudService import CloudService
from components.count import Count
from components.heartbeat import Heartbeat
from components.doorStatus import Door

class App:
    def __init__(self):
        self.__ledStat = statusLED()
        self.__count = Count() #This Initialization starts the callback of Count Process. Detection of Interrupt and call the function
        self.__cloudService = CloudService()
        self.__door = Door()
        self.__heartBeat = Heartbeat()
        self.__ledStat.sysReady_Show(True)

    def run(self):
        try:
            siloCountSync_Thread =  threading.Thread(target = self.__count.countSync)
            autoSync_Thread = threading.Thread(target = self.__cloudService.autoSync)
            siloCountSync_Thread.start()
            autoSync_Thread.start()
            siloCountSync_Thread.join()
            autoSync_Thread.start()
        except:
            self.close()
    
    def close(self):
        self.__count.close()
        self.__ledStat.close()
        self.__door.close()
        sys.exit()
        


    
