from turtle import *

window = Screen()
window.bgcolor("pink")

tom = Turtle()
tom.speed(0)
tom.width(1)
tom.pu()
tom.goto(-300, -300)
tom.pd()
window.tracer(50)


def redsquare():
    tom.begin_fill()
    tom.fillcolor('red')  
    tom.color('red')
    for _ in range(4):
        tom.fd(25)
        tom.lt(90)
    tom.end_fill()
def whitesquare():
    tom.begin_fill()
    tom.color('white') 
    for i in range(4):
        tom.fd(25)
        tom.lt(90)
    tom.end_fill()

def bluesquare():
    tom.begin_fill()
    tom.color('#156fb6') 
    for i in range(4):
        tom.fd(25)
        tom.lt(90)
    tom.end_fill()

def skinsquare():
    tom.begin_fill()
    tom.color('#f8b133')  
    for i in range(4):
        tom.fd(25)
        tom.lt(90)
    tom.end_fill()

def blacksquare():
    tom.begin_fill()
    tom.color('black')
    for i in range(4):
        tom.fd(25)
        tom.lt(90)
    tom.end_fill()


for i in range(10):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.rt(90)
tom.fd(25)
tom.lt(90)

for i in range(9):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.lt(90)
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.lt(90)
tom.fd(25)

for i in range(3):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.back(50)
tom.rt(90)
for i in range(1):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.lt(90)
tom.fd(25)
for i in range(2):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.lt(90)
tom.fd(25)
tom.rt(90)
tom.back(25)
for i in range(2):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.back(100)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(4):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(4):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.lt(90)
tom.fd(25)
tom.rt(90)
tom.pu()
tom.back(450)
tom.pd()
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(4):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
whitesquare()
tom.pu()
tom.fd(25) 
tom.pd()
for i in range(2):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.back(375)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(4):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    redsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(4):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.back(250)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()

update()
done()
window.mainloop()