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
def darkbluesquare():
    tom.begin_fill()
    tom.color('#074e8e') 
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
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(150)
tom.rt(90)
tom.fd(25)
tom.lt(90)
tom.fd(25)
tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(125)
tom.rt(90)
tom.back(50)
tom.rt(90)
tom.fd(150)
tom.lt(90)
tom.fd(25)
tom.lt(90)
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(75)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()

tom.pu()
tom.fd(50)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(11*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.fd(50)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(4):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(13*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.fd(50)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()

tom.pu()
tom.fd(25)
for i in range(5):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(18*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.fd(50)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(17*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(16*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.fd(25)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(15*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(8):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.fd(50)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(19*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(6):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(7):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.fd(25)
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(16*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(4):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(13*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(7):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(19*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(6):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(4):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()

for i in range(3):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()

tom.back(19*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(9):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()

for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(17*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(8):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(16*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(7):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    whitesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(15*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(12):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(16*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(4):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(4):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(5):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(15*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(2):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(3):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(5):
    bluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(1):
    darkbluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
tom.pu()
tom.back(13*25)
tom.rt(90)
tom.fd(25)
tom.lt(90)
for i in range(3):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    skinsquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(6):
    blacksquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
for i in range(2):
    darkbluesquare()
    tom.pu()
    tom.fd(25) 
    tom.pd()
















update()
done()
window.mainloop()