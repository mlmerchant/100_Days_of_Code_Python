# Install TKinter for turtle to work
import turtle
import colorgram
from random import choice

screen = turtle.Screen()
screen.colormode(255)

rgb_colors = []
# place an image with the colors you want in the project folder
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

turtle = turtle.Turtle()

x = -275
y = -250
circle_size = 10
circle_spacing = 4

turtle.speed("fastest")
turtle.hideturtle()

while x < 275:
    while y < 250:
        color_choice = (255, 255, 255)
        # Eliminate the colors that blend into the background
        while color_choice[0] > 200 and color_choice[1] > 200 and color_choice[2] > 200:
            color_choice = choice(rgb_colors)
        turtle.color(color_choice)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(circle_size)
        turtle.end_fill()
        y = y + circle_size * circle_spacing
    y = -250
    x = x + circle_size * circle_spacing

screen.exitonclick()

