#! /usr/bin/python3.5
import codecs, re
file = codecs.open('web1.txt','r',"utf-8")
content = file.read()


'''
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
print(SS%tuple(bb))
'''
#https://sdjkx.me/2015/12/silicon-valley-ss%E5%AF%86%E7%A0%81%E5%B7%B2%E7%BB%8F%E6%9B%B4%E6%96%B0/

b=re.findall("<code>([\w\W]*)</code>",content)
Servers = "".join(b).replace("<br />","")
print(b)
