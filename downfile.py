#!usr/bin/env python
#coding:utf-8
import os
from os import walk
from os import listdir
from os.path import isfile, join
import urllib.request
import shutil
print('os.getcwd():' + os.getcwd())
######################################
url = r'http://localhost/hello'

file_name = r'down/hello'

# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
######################################

print("downloaded\n")
