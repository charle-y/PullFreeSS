import codecs, re
file = codecs.open('web.txt','r',"utf-8")
content = file.read()
from add_ishadowsocks import ishadowsocks
from add_hishadowsocks import hishadowsocks
from add_vultr import vultr
from GetPage import GetPage
SS=['  {\r\n"server" : "','",\r\n"server_port" : ',',\r\n"password" : "','",\r\n"method" : "','",\r\n"remarks" : "','"}\r\n']


happy = ishadowsocks(SS=SS)
happy1 = hishadowsocks(SS=SS)
happy2 = vultr(SS=SS)
print(happy2.get())

