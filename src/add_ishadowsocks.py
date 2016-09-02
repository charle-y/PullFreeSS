# -*- coding: utf-8 -*-
from GetPage import GetPage

class ishadowsocks:
    
    def __init__(self, SS):
        self.SS=SS
    def get(self):
        content = GetPage('http://www.ishadowsocks.com/').get().decode("utf8")
        Servers=""
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
                #print(A_pass)
                if j==2 and A_pass=="":
                    isOn=0
                elif j==4 and A_pass!="正常":
                    isOn=0
                tempServer+=self.SS[j]+A_pass
                if j==4:
                    tempServer+=self.SS[5]
            tempServer+=",\r\n"
            if isOn==1:
                    Servers+=tempServer
        return Servers
if __name__=="__main__":
    SS=['  {\r\n"server" : "','",\r\n"server_port" : ',',\r\n"password" : "','",\r\n"method" : "','",\r\n"remarks" : "','"}\r\n']
    happy = ishadowsocks(SS=SS)
    print(happy.get());

