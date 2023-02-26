from turtle import Turtle
from random import randint

FOOD_BOX = 260

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        random_x = randint(-FOOD_BOX, FOOD_BOX)
        random_y = randint(-FOOD_BOX, FOOD_BOX)
        self.goto(random_x, random_y)

