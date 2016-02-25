#! /usr/bin/python3.5
import codecs, re
file = codecs.open('web.txt','r',"utf-8")
content = file.read()

keyStr = ["服务器地址:(.*)","端口:(.*)","密码:(.*)","加密方式:(.*)",\
          "状态:<.*>(.*)<.*>"]
b=[""]*5
for i in range(5):
    b[i]=re.findall(".*"+keyStr[i]+"</.*",content)
#b=re.findall(".*密码:(.*)</.*",content)
#print(content)
print(b,len(b))
#转置b
bb=[[r[col] for r in b] for col in range(len(b[0]))]
print(bb,len(bb))
SS='  {\r\n"server" : "%s",\r\n"server_port" : %s,\r\n"password" : "%s",\r\n"method" : "%s",\r\n"remarks" : "%s"}\r\n'
print(SS%tuple(bb[1]))
