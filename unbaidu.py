#!/usr/bin/env python
# coding:utf-8
import os
import sys
import requests
import json
import time
import subprocess
from datetime import datetime

open_url = r'http://zhidao.baidu.com/question/%s.html?entry=qb_ihome_tag' 

days = int(input('days?')) 
print(days)

def diff_days(date):
    if date.startswith('今天') or date.endswith('前'): 
        return 0
    last_date = datetime.strptime(date, '%Y-%m-%d')
    return (datetime.now() - last_date).days

def urlopen(page):
    print('\npage=' + str(page))
    timestamp = int(round(time.time() * 1000))
    url = r'https://zhidao.baidu.com/ihome/api/myanswer'
    size = 50 
    parms = {
    'pn' : (page - 1) * size,
    'rn' : size,
    't' : timestamp,
    'type' : 'default'
    }
    headers = {
    'BAIDUID' : u'D32C35449574FFEFB6EDD158B2A6F14D:FG=1',
    'BDUSS' : r'JSLVNjQWtFMWd5Njh0Sm9ibkdSdUx6SXA4RlM2QU1zVEFER2xrMDJuc2pwV2hZSVFBQUFBJCQAAAAAAAAAAAEAAACnjSA20fS54rXEwNff49~jAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACMYQVgjGEFYSX'
    }
    try:
        r = requests.get(url, params=parms, cookies=headers)
        return r.json()
    except Exception as e:
        print(e)


def urlcall(url):
    subprocess.call([r'google-chrome', url])

bestids = []

def baidu_answer_nobest():
    urls = []
    page = 1

    while True:
        sys.stdout.write('.')
        objs = urlopen(page)
        time.sleep(2)
        if objs['errno'] == 1:
            print(objs['errmsg'])
            return urls

        items = objs['data']['question']['list']
        for i in items:
            item_days = diff_days(i['finishTime'])
            if item_days > int(days):
                return urls

            if i['qStatus'] is 2:
                print(i['title']+"\n\n")
                if i['isBest'] == '0' and i['isRecommended'] != 1:
                    urls.append(open_url % i['qid'])
                    print('------------------------------')
                elif i['isBest'] == '1':
                   bestids.append(i['qid']) 

        page+=1

urls = baidu_answer_nobest()
sys.stdout.write('\n')

with open('bestids.txt', 'a') as bestf:
    for id in bestids:
        bestf.write(id+"\r\n")

if len(urls) < 10:
    [urlcall(url) for url in urls]
else:
    [urlcall(url) for url in urls[0:9]]
