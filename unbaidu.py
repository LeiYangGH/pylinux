#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
import requests
import json
import time
import subprocess
from datetime import datetime

open_url = r'http://zhidao.baidu.com/question/%s.html?entry=qb_ihome_tag' 

days = 10

def diff_days(date):
    if date.startswith(u'今天') or date.endswith(u'前'): 
        return 0
    last_date = datetime.strptime(date, '%Y-%m-%d %H:%M')
    return (datetime.now() - last_date).days

def urlopen(page=1):
    print(page)
    time.sleep(2)
    timestamp = int(round(time.time() * 1000))
    url = r'https://zhidao.baidu.com/ihome/api/myanswer'
    size = 100
    parms = {
    'pn' : (page - 1) * 100,
    'rn' : 100,
    't' : timestamp,
    'type' : 'default'
    }
    headers = {
    #'BAIDUID' : u'D32C35449574FFEFB6EDD158B2A6F14D:FG=1',
    'BDUSS' : r'JSLVNjQWtFMWd5Njh0Sm9ibkdSdUx6SXA4RlM2QU1zVEFER2xrMDJuc2pwV2hZSVFBQUFBJCQAAAAAAAAAAAEAAACnjSA20fS54rXEwNff49~jAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACMYQVgjGEFYSX'
    }
    try:
        r = requests.get(url, data=parms, cookies=headers)
        t = r.text
        #print(t)
        return t
    except Exception as e:
        print(e)

def urlcall(url):
    print(url)
    #if browser:
    #    subprocess.call([r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', url])
    #else:
    #    os.startfile(url)


def baidu_answer_nobest():
    #x = 1
    urls = []
    page = 1

    while True:
        sys.stdout.write('.')
        objs = json.loads(urlopen(page))
        if objs['errno'] == 1:
            print(objs['errmsg'])
            return urls

        items = objs['data']['question']['list']
        # display list
        for i in items:
            item_days = diff_days(i['createTime']) 
            #if x > 10: return urls
            print("d="+ str(item_days))
            if item_days > days: return urls

            if i['qStatus'] is 2 and i['isBest'] == '0':
                urls.append(open_url % i['qid'])
        #x = x + 1
        #page+=1
        page+=1

urls = baidu_answer_nobest()
sys.stdout.write('\n')

if input('Are you sure open %d urls? [Y/n] ' % len(urls)) == 'y':
    [urlcall(url) for url in urls]
    os.system('pause')
