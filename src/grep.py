#! /usr/bin/python3.5
#version 0.1
import codecs #, os, sys

from ishadowsocks import ishadowsocks

try:
  ori_file = codecs.open("gui-config.json", 'r',"utf-8")
  ori_txt=ori_file.read()
  ori_file.close()
  Dress1=ori_txt[ori_txt.find("],"):]
except:
  Dress1=""

Dresses = ['{\r\n"configs" : [\r\n','],\r\n"strategy" : null,\r\n"index" : 2,\r\n"global" : false,\r\n"enabled" : false,\
\r\n"shareOverLan" : false,\r\n"isDefault" : false,\r\n"localPort" : 8087,\r\n"pacUrl" : null,\r\n"useOnlinePac" : false,\
"availabilityStatistics" : false}\r\n']
SS=['  {\r\n"server" : "','",\r\n"server_port" : ',',\r\n"password" : "','",\r\n"method" : "','",\r\n"remarks" : "','"}\r\n']

happy = ishadowsocks(SS=SS)
Servers=happy.get()

OUTfile=Dresses[0]+Servers
if len(Dress1)<10:
  OUTfile+=Dresses[1]
else:
  OUTfile+=Dress1
print(OUTfile)

output_file = codecs.open("gui-config.json", 'w+',"utf-8")
output_file.write(OUTfile)
output_file.close()


