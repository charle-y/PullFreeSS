#! /usr/bin/python3.5
#version 0.1
import codecs #, os, sys

from add_ishadowsocks import ishadowsocks
from add_hishadowsocks import hishadowsocks
from add_vultr import vultr
from add_shadowsockscn import add_shadowsockscn

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

Servers=""
try:
  happy = ishadowsocks(SS=SS)
  Servers+=happy.get()
except:
  print("ishadowsocks is down!")

try:
  happy = hishadowsocks(SS=SS)
  Servers+=happy.get()
except:
  print("hishadowsocks is down!")

try:
  happy = vultr(SS=SS)
  Servers+=happy.get()
except:
  print("vultr is down!")
  
try:
  happy = add_shadowsockscn.shadowsockscn(SS=SS)
  Servers+=happy.get()
except:
  print("shadowsockscn is down!")

OUTfile=Dresses[0]+Servers
if len(Dress1)<10:
  OUTfile+=Dresses[1]
else:
  OUTfile+=Dress1
print(OUTfile)

output_file = codecs.open("gui-config.json", 'w+',"utf-8")
output_file.write(OUTfile)
output_file.close()


