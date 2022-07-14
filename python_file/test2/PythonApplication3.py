import turtle as t
t.penup()
t.goto(-200,0)
t.pendown()
t.pensize(20)
t.right(50)

r=13

t.color("purple")
for i in range(25):
    t.left(4)
    t.forward(2)
for i in range(25):
    t.right(4)
    t.forward(2)

t.color("red")
for i in range(25):
    t.left(4)
    t.forward(2)
for i in range(25):
    t.right(4)
    t.forward(2)

t.color("yellow")
for i in range(25):
    t.left(4)
    t.forward(2)
for i in range(25):
    t.right(4)
    t.forward(2)  
    
t.color("pink")
for i in range(25):
    t.left(4)
    t.forward(2)
for i in range(25):
    t.right(4)
    t.forward(2)

t.color("blue")
for i in range(12):
    t.left(4)
    t.forward(2)
t.left(2)
t.forward(40)

t.color("green")
t.circle(15,180)
t.forward(20)