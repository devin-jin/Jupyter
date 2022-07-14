'''
import turtle as t
t.penup()
t.goto(-225,150)
t.pendown()

t.pensize(1)
  
#画长方形
t.color("red","red")
t.begin_fill()

t.forward(450)
t.right(90)
t.forward(300)
t.right(90)
t.forward(450)
t.right(90)
t.forward(300)
t.right(90)
t.end_fill()

#前往大五角星起始坐标
x=-145
y=85
t.penup()
t.goto(x,y)
t.pendown()
#画大五角星
t.color("yellow","yellow")
t.begin_fill()
for i in range(5):
    t.forward(30)
    t.right(144)
    t.forward(30)
    t.left(72)
t.end_fill()

r=9#小五角星边长
d=95#大五角星到小五角星距离
m=14#围绕角度

#到小五角星的起始位置
t.penup()
t.goto(x-12,y-14)
t.setheading(3*m)
t.forward(d)
t.pendown()

#画第一个小五角星
t.color("yellow","yellow")
t.begin_fill()
for i in range(5):
    t.forward(r)
    t.right(144)
    t.forward(r)
    t.left(72)
t.end_fill()
#画第二个小五角星
t.penup()
t.goto(x-12,y-14)
t.setheading(m)
t.forward(d)
t.pendown()

t.color("yellow","yellow")
t.begin_fill()
for i in range(5):
    t.forward(r)
    t.right(144)
    t.forward(r)
    t.left(72)
t.end_fill()
#画第三个小五角星
t.penup()
t.goto(x-12,y-14)
t.setheading(-m)
t.forward(d)
t.pendown()

t.color("yellow","yellow")
t.begin_fill()
for i in range(5):
    t.forward(r)
    t.right(144)
    t.forward(r)
    t.left(72)
t.end_fill()
#画第四个小五角星
t.penup()
t.goto(x-12,y-14)
t.setheading(-3*m)
t.forward(d)
t.pendown()

t.color("yellow","yellow")
t.begin_fill()
for i in range(5):
    t.forward(r)
    t.right(144)
    t.forward(r)
    t.left(72)
t.end_fill()
'''
import math
def isPerfectNum():
    n = int(input('input a number: '))
    k = int(math.sqrt(n))
    sum=0
    for i in range(1,k+1):
        if 0 == n%i:
            sum += n/i
            sum += i
    sum -= n 
    if n == sum:
        return 1
    else:
        return 0
def main():
    tag = isPerfectNum()
    if tag:
        print("This is perfect number")
    else:
        print("This isn't perfect number")
        
if __name__=='__main__':
    main()
 




