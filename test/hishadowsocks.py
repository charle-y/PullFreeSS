# -*- coding: utf-8 -*-
import re
from GetPage import GetPage

class hishadowsocks:
    
    def __init__(self, SS):
        self.SS='  {\r\n"server" : "%s",\r\n"server_port" : %s,\r\n"password" : "%s",\r\n"method" : "%s",\r\n"remarks" : "%s"}\r\n'

    def get(self):
        content = GetPage('http://www.hishadowsocks.com/').get().decode("utf8")
        keyStr = ["服务器地址:(.*?)","端口:(.*?)","密码:(.*?)","加密方式:(.*?)",\
          "状态:<.*>(.*?)<.*>"]
        b=[""]*5
        for i in range(4):
            b[i]="".join(re.findall(".*"+keyStr[i]+"</.*",content))
        b[4] = 'unknown'
        #print(b)
        Servers = self.SS%tuple(b)
        return Servers


