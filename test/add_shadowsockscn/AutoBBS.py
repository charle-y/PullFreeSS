# -*- coding: utf-8 -*-

import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, http.cookiejar, re, hashlib, time, json

class Utils:
    @staticmethod
    def getMD5Of(src):
        m = hashlib.md5()
        m.update(src)
        #print(m.hexdigest())
        return m.hexdigest()
    @staticmethod
    def getTime():
        return int(time.time())

class AutoBBS:
    __userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36'

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
        else :
            print('Login failed!')
            is_login = 0
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
            
    def reply(self, fid, tid, msg):
        headers = {'User-Agent': self.__userAgent}
        params = {'mod': 'post', 'action': 'reply',
                  'replysubmit': 'yes', 'infloat': 'yes',
                  'handlekey': 'fastpost', 'inajax': '1',
                  'fid': fid, 'tid': tid}
        url = self.domain.urlWithParams('forum.php', params)
        data = {'message': msg, 'posttime': Utils.getTime(),
                'usesig': '0', 'subject': '', 'formhash': self.__formhash}
        res = self.__post(url, headers, data)
        if res[3].find('成功') != -1:
            print('Reply OK!')
        else :
            print('Reply failed!')
    def new(self, fid, subject, message):
        headers = {'User-Agent': self.__userAgent}
        params = {'mod': 'post', 'action': 'newthread', 'topicsubmit': 'yes', 'fid': fid}
        url = self.domain.urlWithParams('forum.php', params)
        data = {'formhash': self.__formhash, 'posttime': Utils.getTime(),
                'wysiwyg': '1', 'typeid': '323', 'subject': subject,
                'message': message, 'allownoticeauthor': '0', 'usesig': '1'}
        res = self.__post(url, headers, data)
 
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
            ss+=servers[nl][0][:-1]+',"remarks" : "'+info_nodes[nl]+'"},\r\n'
        #print(ss)
        return ss
        
        
    
'''
from Domain import Domain
domain = Domain(hostname = 'bbs.uestc.edu.cn')
autobbs = AutoBBS(domain = domain, userName = '', passWord = '')
autobbs.login()
'''
