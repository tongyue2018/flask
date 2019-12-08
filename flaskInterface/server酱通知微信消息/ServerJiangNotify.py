

import requests

class ServerJiangNoify:
    def __init__(self,text,desp):
        self.__text = text
        self.__desp = desp
    def getText(self):
        return self.__text
    def getDesp(self):
        return self.__desp

    def sendMessage(self):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        }
        urlDict = {
            'serverJiang': 'https://sc.ftqq.com/SCU54661Tded2ef7767853b3d82a00ac637c4ef3f5d1d5363c48bf.send',
        }
        data = {
            "text": self.__text,
            "desp": self.__desp
        }
        sendMessageOBJ = requests.post(url=urlDict['serverJiang'], headers=headers, data=data)
        return sendMessageOBJ.json()
