#!/usr/bin/env python
# coding: UTF-8
class student:
    def __init__(x,name,age):
        
        x.name=name
        x.age=age
        xyz = 5


    def __setattr__(self, attr, value):
        if attr == 'name':
            if len(value)>200:
                print('name > 200')
##            else:
##                object.__setattr__(self, attr, value)
        if attr == 'age':
            if value>100:
                print('age > 100')
##            else:
##                object.__setattr__(self, attr, value)
        self.__dict__[attr] = value
                

    def greet(x):
        print('I am ' + x.name + ',I\'m '+str(x.age)+' years old')

class manager(student):
    def manage(self,stu):
        print(self.name + ' manage ' + stu.name )

if __name__ == '__main__':  
    ly = student('leiyang',29)
    ly.greet()

    mgr = student('shawn',40)
    mgr.greet()

    print('xyz = %d' % (self.xyz))
