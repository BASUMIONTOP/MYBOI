
import turtle
from turtle import*
window = turtle.Screen()
window.tracer(False)
window.bgcolor("white")

pixel = Turtle()
pixel.speed(0) 


pixel_size = 20


def draw_pixel(x, y, color):
    pixel.penup()
    pixel.goto(x, y)
    pixel.pendown()
    pixel.begin_fill()
    pixel.color(color)
    for _ in range(4): 
        pixel.forward(pixel_size)
        pixel.left(90)
    pixel.end_fill()

image = [
    [1, 2, 2, 1, 1, 2, 2, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 1, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]

for y in range(len(image)):
    for x in range(len(image[y])):
        if image[y][x] == 1:
            draw_pixel(x * pixel_size - 100, 100 - y * pixel_size, "blue")  
        elif image[y][x] == 2:
            draw_pixel(x * pixel_size - 100, 100 - y * pixel_size, "black")  

pixel.hideturtle()
window.tracer(True)
turtle.exitonclick()
done()

