from turtle import Turtle

MOVE_DISTANCE = 2

class Paddle(Turtle):

    def __init__(self, position=(0, 0)):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("paddle")
        self.setheading(90)
        self.goto(position)
        self.direction = "UP"

    def up(self):
        self.direction = "UP"

    def down(self):
        self.direction = "DOWN"

    def check_for_reverse(self):
        if self.ycor() > 300:
            self.direction = "DOWN"
        if self.ycor() < -300:
            self.direction = "UP"

    def travel(self):
        if self.direction == "UP":
            self.setheading(90)
            self.forward(MOVE_DISTANCE)
        elif self.direction == "DOWN":
            self.setheading(270)
            self.forward(MOVE_DISTANCE)
        self.check_for_reverse()

