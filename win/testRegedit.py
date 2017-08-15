from _winreg import *
aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)


key = OpenKey(aReg,r"SOFTWARE\Microsoft\Microsoft SQL Server\120")
try:
    i=0
    while 1:
        name,value,type = EnumValue(key,i)
        print repr(name),value,type
        i+=1
except WindowsError:
    print      
