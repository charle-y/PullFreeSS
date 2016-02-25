import codecs, re
file = codecs.open('web.txt','r',"utf-8")
content = file.read()
from ishadowsocks import ishadowsocks
from GetPage import GetPage
SS=['  {\r\n"server" : "','",\r\n"server_port" : ',',\r\n"password" : "','",\r\n"method" : "','",\r\n"remarks" : "','"}\r\n']
url='http://www.ishadowsocks.com/'

happy = ishadowsocks(the_page=GetPage(url).get(),SS=SS)
print(happy.get())
