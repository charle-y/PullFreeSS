import codecs, re
file = codecs.open('web.txt','r',"utf-8")
content = file.read()
from ishadowsocks import ishadowsocks
from hishadowsocks import hishadowsocks
from GetPage import GetPage
SS=['  {\r\n"server" : "','",\r\n"server_port" : ',',\r\n"password" : "','",\r\n"method" : "','",\r\n"remarks" : "','"}\r\n']


happy = ishadowsocks(SS=SS)
happy1 = hishadowsocks(SS=SS)
print(happy1.get())
