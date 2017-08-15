#!/usr/bin/env python
# coding: UTF-8
#a = None or 5
a = 100*23
print(a)

import turtle
for i in range(1):
    def paint(ang,r,ang2):
        turtle.penup()
        turtle.setheading(ang)
        turtle.pendown()
        turtle.circle(r,ang2)
        turtle.speed(9)
        turtle.color("white")
        turtle.pensize(7)
        turtle.penup()
        turtle.goto(50,-50)
        turtle.pendown()
        turtle.dot(200,"pink")
        turtle.pendown()
        turtle.goto(50,86.6)
    ang=-150
    r=300
    ang2=46
    for j in range(3):
        paint(ang,r,ang2)
        ang2-=25
        paint(ang+ang2+25,r,-ang2)
        ang2+=25
        ang+=66
        r=r*0.9
turtle.done()



