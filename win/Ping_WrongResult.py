from pywinauto import application
from shutil import copyfile
import os
import sys
import zipfile
import os.path
import shutil
import time
import datetime
import globalvalues
import psutil
import re
import subprocess

def pingip(ip):
##    if os.system("ping " + ip) == 0:
##        print  "can ping " + ip
##    else :
##        print "--- cannot ping " + ip
    if os.system("ping -n 1 "+ip).find("TTL=")>-1 :
        print "can ping "+ip
    else :
        print "--- can not ping"+ip
  

#pingip('www.baidu.com')
pingip('www.sina.com.cn')

 
