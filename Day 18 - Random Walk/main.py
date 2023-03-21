from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
tim = Turtle()
tim.pensize(15)
tim.speed("fastest")
screen.colormode(255)

def return_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(1000):
    tim.seth(choice([0, 90, 180, 270]))
    tim.color(return_random_color())
    tim.forward(30)

screen.exitonclick()
