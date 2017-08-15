#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
import urllib.request as urllib2
from urllib import request, parse
#import urllib2
import json
import time
#import ConfigParser
import subprocess
import http.cookiejar
from datetime import datetime


timestamp = int(round(time.time() * 1000))
url = 'https://zhidao.baidu.com/ihome/api/myanswer'
parms = {
'pn' : 10,
'rn' : 10,
't' : timestamp,
'type' : 'default'
}
querystring = parse.urlencode(parms)
headers = {
'BAIDUID' : r'D32C35449574FFEFB6EDD158B2A6F14D:FG=1',
'BDUSS' : r'FrSGN4eWJEU21LWWVneWxhMHVNMzlzdC1sNGFyYldjdlhQWlhDWXEwOG1NelJZSVFBQUFBJCQAAAAAAAAAAAEAAACnjSA20fS54rXEwNff49~jAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACamDFgmpgxYMz',
#'BIDUPSID' : r'F5A8CF3A7BEA8E8E94D32CE2D999087A',
#'__cfduid':r'd8a8d603056330597710bc2a34f23feb71472292117',
}
req = urllib2.Request(url, headers=headers)
u = urllib2.urlopen(req)
resp = u.read()
print(resp)


