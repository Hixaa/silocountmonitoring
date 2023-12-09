import configparser
import os
from pathlib import Path

class Config:
    def __init__(self):
        self.__folder = os.getcwd()
        self.__configPath = self.__folder + '/config_scms.ini'
        self.__countConfigPath = self.__folder + '/count.ini'
        if not os.path.exists(self.__countConfigPath):
            config = configparser.ConfigParser()
            config['COUNT'] = {'signalCount':'0'}
            with open(self.__countConfigPath,'w') as configfile:
                config.write(configfile)


###################**Count Update and Read**#########################
    def count(self):
        parser = configparser.ConfigParser()
        parser.read(self.__countConfigPath)
        return int(parser.get('COUNT','signalCount'))

    def setCount(self,count):
        parser = configparser.ConfigParser()
        parser.read(self.__countConfigPath)
        count_config = parser['COUNT']
        count_config['signalCount'] = str(count)
        with open(self.__countConfigPath,'w') as configfile:
            parser.write(configfile)
#####################################################################

################***GPIO for Giving Status***#########################
    
    def GPIO_sysReady(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('Status_GPIO','sysReady'))

    def GPIO_countStat(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('Status_GPIO','count'))

    def GPIO_dataUploadStat(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('Status_GPIO','dataUpload'))

################***GPIO for Input***################################
    
    def GPIO_GodownChannel(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('Input_GPIO','Godown_Channel'))

    def GPIO_doorChannel(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('Input_GPIO','doorChannel'))

    def GPIO_SiloChannel(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('Input_GPIO','Silo_Channel'))
####################################################################

    '''def channel_2(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('GPIO','channel_2')

    def channel_3(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('GPIO','channel_3')

    def channel_4(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('GPIO','channel_4')'''

##############***Cloud Service Fetch Gatway URL***#################
    
    def url(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('CloudService','url')

    def urlCount(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('CloudService','urlCount')

    def urlDoor(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('CloudService','urlDoor')

    def urlHeartbeat(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('CloudService','urlHeartbeat')

##################################################################

##############**********Application Specific*********#############

    def clientId(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('App','clientId')

    def deviceId(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('App','deviceId')

    def isGodown(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return bool(parser.getboolean('App','Godown'))

##################################################################

    def DS_maxLimit(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return parser.get('JSON_Storage','max_limit')

    def heartbeatInterval(self):
        parser = configparser.ConfigParser()
        parser.read(self.__configPath)
        return int(parser.get('Heartbeat_Interval','heartbeatInterval'))















