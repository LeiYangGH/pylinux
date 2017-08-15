#!/usr/bin/env python
# coding: UTF-8
class student:
    def __init__(x,name,age):
        
        x.name=name
        x.age=age

    #why error if add this method
    def __setattr__(self, attr, value):
        if attr == '3name1':
            if len(value)>200:
                print('name > 200')

    def greet(x):
        print('I am ' + x.name + ',I\'m '+str(x.age)+' years old')

    def setfixname(x):
        x.name = 'fixed name'


class manager(student):
    def manage(self,stu):
        print(self.name + ' manage ' + stu.name )

if __name__ == '__main__':  
    ly = student('leiyang',29)
    ly.greet()

    mgr = student('shawn',40)
    mgr.greet()
