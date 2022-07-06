import turtle as t # turtle 기니까 t로 받는다는 의미

#1. 정사각형 그리기
for i in range(4):
    t.fd(100)
    t.left(90)
print(t.pos())

#2. 평행사변형 그리기
t.up()
t.goto(200,0)
t.down()
for i in range(2):
    t.fd(120)
    t.left(120)
    t.fd(100)
    t.left(60)

#3. 별 그리기
t.up()
t.goto(-200,0)
t.down()
for i in range(5):
    t.fd(110)
    t.left(360*2/5)

#4. 기하학적인 도형 그리기
t.up()
t.goto(0,300)
t.down()

t.color('red', 'yellow')
t.begin_fill()

while(True):
    t.forward(100)
    t.left(170)
    x,y=t.pos()
    if int(x) == 0 and int(y) == 300:
        break
t.end_fill()
t.done()
