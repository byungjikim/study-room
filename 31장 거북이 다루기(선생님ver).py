from turtle import *
from random import randint
import time

speed(10)
up()
goto(-140,140)

for i in range(16):
    write(i, align='center')
    right(90)
    fd(10)
    down()
    fd(150)
    up()
    bk(160)
    left(90)
    fd(20)

finish_line = xcor() -20

turtle_color = ['red','blue','green','gold']
turtle_list = []

for i in range(len(turtle_color)):
    t= Turtle() #새 거북이 선수 생성
    t.color(turtle_color[i])
    t.shape('turtle')
    t.up()
    t.goto(-160, 140-30*(i+1))
    t.down()
    turtle_list.append(t)
def start():
    while(True):
        for t in turtle_list:
            dist = randint(1,5)
            t.fd(dist)
            if t.xcor() >= finish_line:
                return t
t= start()
for i in range(1,10):
    t.shapesize(i,i)
    time.sleep(0.3)

for i in range(36*3):
    t.right(10)

goto(0,0)
color1 = str(t.color()[0])
write("Congraturation "+color1,align = 'center')
