#!/usr/bin/env python
# coding: UTF-8
class student:
    def __init__(x,name,age):
        
        x.name=name
        x.age=age
        x.setfixname()

    def greet(x):
        print('I am ' + x.name + ',I\'m '+str(x.age)+' years old')

    def setfixname(x):
        x.name = 'fixed name'

class manager(student):
    def manage(self,stu):
        print(self.name + ' manage ' + stu.name )
##    def __init__(x,name,age):
##        x.name=name
##        x.age=age

if __name__ == '__main__':  
    ly = student('leiyang',29)
    ly.greet()



    mgr = student('shawn',40)
    mgr.greet()
