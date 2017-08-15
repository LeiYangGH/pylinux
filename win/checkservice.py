from pywinauto import application
import re
import win32serviceutil
print "start"

 
status = win32serviceutil.QueryServiceStatus('MSSQLSERVER')

scvType, svcState, svcControls, err, svcErr, svcCP, svcWH = status
print svcState
#4 running
#1 stop
print "end"
    


