#!/usr/bin/env python
# coding: UTF-8
##from student.testclass import *
from student.testclass import student,manager
##class student:
##    def __init__(x,name,age):
##        x.name=name
##        x.age=age
##
##    def greet(x):
##        print('I am ' + x.name + ',I\'m '+str(x.age)+' years old')
##
##class manager(student):
##    def __init__(x,name,age):
##        x.name=name
##        x.age=age

ly = student('leiyang',29)
ly.greet()

mgr = manager('shawn',40)
mgr.greet()
mgr.manage(ly)
