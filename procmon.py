from shutil import copyfile
import os
import sys
import zipfile
import os.path
import shutil
import time
import datetime
import psutil

process_name = "gedit"


def waitdatprocessstart():
    print ''
    print 'wait for gedit  process to start'
    while(1):
        exist = 0


        for proc in psutil.process_iter(): 
            process = psutil.Process(proc.pid)
            pname = process.name()
            if pname == process_name:
            #print process_name
                exist = 1
        if exist == 1:
            print 'process started'
            print ''
            break
        else:
            sys.stdout.write('.')
            time.sleep(2)

def waitdatprocesssstop():
    print ''
    print 'wait for gedit  process to stop'
    while(1):
        exist = 0
        for proc in psutil.process_iter(): 
            process = psutil.Process(proc.pid)
            pname = process.name()
            if pname == process_name:
            #print process_name
                exist = 1
        if exist == 0:
            print 'process stopped'
            print ''
            break
        else:
            sys.stdout.write('.')
            time.sleep(2)




waitdatprocessstart()

waitdatprocesssstop()



print "pause..."
raw_input()
os._exit()









 
