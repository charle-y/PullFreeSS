# -*- coding: utf-8 -*-
import urllib.request

class GetPage:
    
    def __init__(self, url):
        self.url=url
    def get(self):
        
        user_agent = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
        }
        
        req = urllib.request.Request(self.url,headers=user_agent)
        response = urllib.request.urlopen(req,timeout = 5)
        the_page = response.read()
        response.close()
        
        return the_page


