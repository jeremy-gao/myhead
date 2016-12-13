#!/usr/bin/env python
#-*-coding:utf-8-*-
from urllib2 import urlopen
import demjson, commands, pycurl


class Elastic(object):
    def __init__(self):
        self.url = []
    def health(self,url):
        resp = urlopen(url)
        content = resp.read()
        data = demjson.decode(content, encoding="utf-8")
        return data
    def nodelist(self,url):
        resp = urlopen(url)    
        content = resp.read().split('\n')
        return content
    def allocation(self,url):
        resp = urlopen(url)
        content = resp.read().split('\n')
        return content
    def indexsize(self,url,cmd):
        systemcmd = url + cmd
        status,output = commands.getstatusoutput(systemcmd)
        return status,output
    def allindex(self,url):
        resp = urlopen(url)
        content = resp.read().split('\n')
        return content
    def indextypes(self,url):
        resp = urlopen(url)
        content = resp.read()
        return content
        
    def delindex(self,url):
        c = pycurl.Curl()
        c.setopt(pycurl.CUSTOMREQUEST, 'DELETE')
        c.setopt(pycurl.URL, url)
        c.perform()
        content = c.getinfo(pycurl.HTTP_CODE)
        c.close()
        return  content
        

        
