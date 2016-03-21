# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error, http.cookiejar, re, time, json

class AutoBBS:
    __userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36'
    left_dataVolume=''
    def __init__(self, domain, userName, passWord, proxyHandler = {}):
        self.domain = domain
        self.__userName = userName
        self.__passWord = passWord
        cj = http.cookiejar.CookieJar()
        self.__opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxyHandler),
                                             urllib.request.HTTPCookieProcessor(cj))
        
    def __get(self, url, headers):
        request = urllib.request.Request(url = url, headers = headers)
        res = self.__opener.open(request)
        return res.getcode(), res.info(), res.geturl(), res.read().decode("utf8")
    
    def __post(self, url, headers, data):
        data = urllib.parse.urlencode(data).encode(encoding="utf-8")
        request = urllib.request.Request(url = url, headers = headers, data = data)
        res = self.__opener.open(request)
        return res.getcode(), res.info(), res.geturl(), res.read()
    
    def login(self):
        headers = {'User-Agent': self.__userAgent}
        extUrl = '/auth/login'
        url = self.domain.fullUrl(extUrl=extUrl)
        #res11=res[3].decode("utf8")
        #print(res[3])
        data = {'email': self.__userName,
                'passwd': self.__passWord}
        #Utils.getMD5Of(self.__passWord)
        self.__post(url, headers, data)
        url = self.domain.urlWithParams('/user', {})
        res = self.__get(url, headers)
        #print(res[0])
        if res[3].find('节点列表') != -1:
            print('Login OK!')
            is_login = 1
            self.left_dataVolume = re.findall("剩余流量：(.*?)<",res[3])[0]
            last_time = re.findall("<p>上次签到时间：<code>(.*)?</code></p>",res[3])[0]
            ts = time.time()-time.mktime(time.strptime(last_time,'%Y-%m-%d %H:%M:%S'))
            #print(ts)
            need_time=(240-int(ts/60/6))/10
            if need_time<0:
                print("需要签到，距离上次签到",24-need_time,"小时")
                need_check = 1
            else:
                print("不需要签到，还有",need_time,"小时才可以签到")
                need_check = 0
        else :
            print('Login failed!')
            is_login = 0
            need_check = 0
        return is_login, need_check
        
    def checkin(self):
        headers = {'User-Agent': self.__userAgent}
        url = self.domain.urlWithParams('/user/checkin', {})
        data = {}
        #Utils.getMD5Of(self.__passWord)
        res=self.__post(url, headers, data)
        msg=res[3].decode('unicode-escape')
        #print(msg)
        msg1 = "".join(re.findall('"msg":"(.*)",',msg))
        if msg1.find("已经签到") != -1:
            print('已经签到过')
            return 0
        elif msg1.find("流量") != -1:
            print(msg1)
            return 1
        else:
            print("something is wrong",msg1)
            return 0
            
    def getAccount(self):
        headers = {'User-Agent': self.__userAgent}
        url = self.domain.urlWithParams('/user/node', {})
        #Utils.getMD5Of(self.__passWord)
        res = self.__get(url, headers)
        node_list=re.findall('<a   href="\.(.*?)">',res[3])
        info_nodes = re.findall(r'<i class="fa fa-angle-right"></i> (.*?)</li>',res[3])
        tt = len(node_list)
        servers=['']*tt
        ss=""
        for nl in range(tt):
            url = self.domain.urlWithParams('/user'+node_list[nl], {})
            res = self.__get(url, headers)
            servers[nl] = re.findall('{.*}',res[3])
            ss+=servers[nl][0][:-1]+',"remarks" : "'+info_nodes[nl]+self.left_dataVolume+'"},\r\n'
        #print(ss)
        return ss
