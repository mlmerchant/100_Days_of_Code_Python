from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
tim = Turtle()
tim.pensize(2)
tim.speed("fastest")
screen.colormode(255)


def return_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


angle = 11
turns = int(360/angle)

for _ in range(turns):
    tim.color(return_random_color())
    tim.circle(100)
    tim.right(angle)

screen.exitonclick()
