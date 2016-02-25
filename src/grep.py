#! /usr/bin/python3.5
#version 0.1
import codecs #, os, sys
import urllib.request
user_agent = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"'
}
req = urllib.request.Request('http://www.ishadowsocks.com/',headers=user_agent)
response = urllib.request.urlopen(req,timeout = 5)
the_page = response.read()
response.close()
#type = sys.getfilesystemencoding()
#转换成本地系统编码
#the_page = unicode(the_page, "gb2312").encode("utf8")
#print(the_page)
##print(the_page.decode("utf8"))#可以用的
content = the_page.decode("utf8")

try:
  ori_file = codecs.open("gui-config.json", 'r',"utf-8")
  ori_txt=ori_file.read()
  ori_file.close()
  Dress1=ori_txt[ori_txt.find("],"):]
  #bak_file = codecs.open("gui-config.json.bak", 'a+',"utf-8")
  #bak_file.write(ori_txt)
  #bak_file.close()
except:
  Dress1=""

Dresses = ['{\r\n"configs" : [\r\n','],\r\n"strategy" : null,\r\n"index" : 2,\r\n"global" : false,\r\n"enabled" : false,\
\r\n"shareOverLan" : false,\r\n"isDefault" : false,\r\n"localPort" : 8087,\r\n"pacUrl" : null,\r\n"useOnlinePac" : false,\
"availabilityStatistics" : false}\r\n']
SS=['  {\r\n"server" : "','",\r\n"server_port" : ',',\r\n"password" : "','",\r\n"method" : "','",\r\n"remarks" : "','"}\r\n']
OUTfile=Dresses[0]
#tempServer=""
#isOn=0

initA=0
strABC=[["A","","A","",""],["B","","B","",""],["C","","C","",""]]
strClass=["服务器地址:","端口:","密码:","加密方式:",'状态:<font color="green">']
for i in range(3):
  tempServer=""
  isOn=1
  for j in range(5):
    A1=strABC[i][j]+strClass[j] #设置关键字1
    A2='</'#设置关键字2
#print(len(A1))
    A_start=content.find(A1,initA)+len(A1)#找出关键字1的位置
    initA=A_start
    A_end =content.find(A2,A_start)#找出关键字2的位置(从字1后面开始查找)
    A_pass=content[A_start:A_end]#得到关键字1与关键字2之间的内容(即想要的数据)
    print(A_pass)
    if j==2 and A_pass=="":
      isOn=0
    elif j==4 and A_pass!="正常":
      isOn=0
    tempServer+=SS[j]+A_pass
    if j==4:
      tempServer+=SS[5]
  if i<2:
    tempServer+=","
  tempServer+="\r\n"
  if isOn==1:
    OUTfile+=tempServer
#print(len(Dress1))
if len(Dress1)<10:
  OUTfile+=Dresses[1]
else:
  OUTfile+=Dress1
print(OUTfile)
#try:
#  os.remove("../gui-config.json")
#finally:
output_file = codecs.open("gui-config.json", 'w+',"utf-8")
output_file.write(OUTfile)
output_file.close()


