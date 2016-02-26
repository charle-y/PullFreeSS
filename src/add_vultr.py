# -*- coding: utf-8 -*-
import re
from GetPage import GetPage

class vultr:
    
    def __init__(self, SS):
        self.SS='  {\r\n"server" : "%s",\r\n"server_port" : %s,\r\n"password" : "%s",\r\n"method" : "%s",\r\n"remarks" : "%s"}\r\n'

    def get(self):
        content = GetPage('https://sdjkx.me/2015/12/silicon-valley-ss%E5%AF%86%E7%A0%81%E5%B7%B2%E7%BB%8F%E6%9B%B4%E6%96%B0/').get().decode("utf8")
        b=re.findall("<code>([\w\W]*)</code>",content)
        Servers = "".join(b).replace("<br />","")+",\r\n"
        return Servers


