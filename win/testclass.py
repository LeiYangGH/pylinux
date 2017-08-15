#!/usr/bin/env python
# coding: UTF-8
##from student.testclass import *
from student.testclass import student,manager

ly = student('leiyang',29)
ly.greet()

mgr = manager('shawn',40)
mgr.greet()
mgr.manage(ly)
