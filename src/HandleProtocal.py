# -*- coding: utf-8 -*-
import re
from GetPage import GetPage
import json
from collections import OrderedDict

class ishadowsocks:
    url = 'http://isx.yt/';
    keyStr = ["IP Address:<.*?>(.*?)</","Port：(.*?)</","Password:<.*?>(.*?)</","Method:(.*?)</","IP Address:<span id=(.*?)>"]
    SS = ["server", "server_port", "password", "method", "remarks"]
    
    url_List = []
    keyStr_List = []
    SS_List= []
    config_len = -1
    '''
    
    '''
    def __init__(self):
        try: 
            self.readIni()
        except:
            self.creatIni()
    def get(self):
        ss = []
        for i in range(self.config_len):    
            self.url = self.url_List[i]
            self.keyStr = self.keyStr_List[i]
            self.SS = self.SS_List[i]
            ss.extend(self.htmlWork())
        #print(ss)
        return ss
    
    def htmlWork(self):
        Servers = [];
        content = GetPage(self.url).get().decode("utf8")
        b=[""]*5;
        serverValidFlag = True;
        for i in range(5):
            b[i]=re.findall(self.keyStr[i],content)
        for j in range(len(b[0])):
            server_dict = OrderedDict();
            serverValidFlag = True;
            for i in range(5):
                if (b[i][j] == ''):
                    serverValidFlag = False;
                server_dict[self.SS[i]] = b[i][j];
            #print(server_dict)
            if serverValidFlag:
                Servers.append(server_dict);
        #print(Servers)
        #b[4] = 'unknown'
        #print(Servers)
        #Servers = %tuple(b)+",\r\n"self.SS[i]
        return Servers
        
    def readIni(self):
        config_len = -1
        with open("re.ini", "r") as s:
            j = json.load(s)
            self.config_len = len(j["config"])
            #print(self.config_len)
            for i in range(self.config_len):
                self.url_List.append(j["config"][i]["url"])
                self.keyStr_List.append(j["config"][i]["keyStr"].split(';'))
                self.SS_List.append(j["config"][i]["SS"].split(';'))
                
    def creatIni(self):        
        jj = []
        j = {}
        j["url"] = self.url
        j["keyStr"] =";".join(self.keyStr)
        j["SS"] = ";".join(self.SS)
        jj.append(j)
        j1 = {}
        j1["config"] = jj
        with open("re.ini", "w") as s:
            json.dump( j1, s, indent = 2)
            
if __name__=="__main__":
    SS=["server", "server_port", "password", "method", "remarks", "auth", "timeout"]
    happy = ishadowsocks()
    with open("gui-config.json", "r") as s:
        j = json.load(s)
        j["configs"] = happy.get()
        with open("gui-config.json", "w") as n_c:
            try:
                json.dump(j, n_c, indent = 4, separators=(',', ': '))
                print("写入成功")
            except:
                print("写入失败")
    #print(happy.get());

