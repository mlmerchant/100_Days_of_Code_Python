from turtle import Turtle

MOVE_DISTANCE = 5

class Player(Turtle):

    def __init__(self, position=(0, 0), color="black"):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("turtle")
        self.setheading(90)
        self.goto(position)

    def up(self):
        self.forward(MOVE_DISTANCE)

