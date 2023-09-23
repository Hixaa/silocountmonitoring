import os
from datetime import datetime

class StoreJson:
    def __init__(self):
        self.__rootFolder = os.getcwd()
        self.__dataStorageFolder = self.__rootFolder+'/data_storage'
        self.__selectedFile = ''
        if(not os.path.exists(self.__dataStorageFolder)):
            os.makedirs(self.__dataStorageFolder)

    def __generateAndAppend(self,data):
        self.__FileName = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.__selectedFile = self.__FileName
        try:
            # FIXME: Change the .txt to .dat
            with open("%s/%s.txt"%(self.__dataStorageFolder,self.__FileName),'a+') as fp:
                print("[+] Generated File : %s"%(self.__FileName))
                fp.write(data+'\n')
        except FileNotFoundError:
            os.mkdir(self.__dataStorageFolder)
        
    def __checkLinesInFile(self,fileName):
        count=0
        with open("%s/%s"%(self.__dataStorageFolder,fileName),'r') as fp:
            for count, line in enumerate(fp):
                pass
        print("[+]  %d Lines are in %s File"%(count,fileName))
        return count
         
    def getJsonArray(self):
        jsonStr = ''
        with open("%s/%s"%(self.__dataStorageFolder,self.__selectedFile),'r') as fp:
            jsonArray = fp.readlines()
        
        return jsonArray

    def checkAvailable_Files(self, recent = True):
        #Check File inside folder
        file_avail = list()
        for file in os.listdir(self.__dataStorageFolder):
            # FIXME: Update the extension from .txt to .dat
            if file.endswith(".txt"):
                file_avail.append(file)
        file_avail.sort() #ascending sort
        # print("[+] Available Files: ",file_avail) 
       
        if(len(file_avail) > 0):
            if (recent):
                self.__selectedFile = file_avail[-1]
            else:
                self.__selectedFile = file_avail[0]
            print("[+] Current Selected Files: %s"%(self.__selectedFile))
            return True
        else:
            return False

    def truncateFile(self):
        print("[+] Stored File Will Truncate Here!")
        os.remove("%s/%s"%(self.__dataStorageFolder,self.__selectedFile))
        print("[+] Truncated: ","%s/%s"%(self.__dataStorageFolder,self.__selectedFile))

    def pushLocal(self,data):
        if(self.checkAvailable_Files()):
            if(self.__checkLinesInFile(self.__selectedFile) >= 99):
                self.__generateAndAppend(data)
                print('[+]                    GENERATING NEW FILE')
            else:
                with open("%s/%s"%(self.__dataStorageFolder,self.__selectedFile),'a') as fp:
                    fp.write(data +'\n')
                    print("[+] Appeneded data: %s in %s File!"%(data,self.__selectedFile))
        else:
            self.__generateAndAppend(data)
