from turtle import Turtle
from random import choice


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)
        ball_heading = choice([45, 80, 100, 135, 260, 225, 280, 315])
        self.setheading(ball_heading)

    def travel(self):
        self.forward(3)

    def try_bounce_top(self):
        if self.ycor() > 300:
            if 0 < self.heading() < 90:
                # heading east
                new_heading = 360 - (self.heading())
                self.setheading(new_heading)
            else:
                # heading west
                new_heading = 270 - (self.heading() - 90)
                self.setheading(new_heading)

    def try_bounce_bottom(self):
        if self.ycor() < -300:
            if 180 < self.heading() < 270:
                # heading west
                new_heading = abs(270 - self.heading()) + 90
                self.setheading(new_heading)
            else:
                # heading east
                new_heading = (360 - self.heading())
                self.setheading(new_heading)

    def try_paddle1_bounce(self, paddle):
        if self.distance(paddle) < 20:
            new_direction = choice([100, 135, 260, 225])
            self.setheading(new_direction)

    def try_paddle2_bounce(self, paddle):
        if self.distance(paddle) < 20:
            new_direction = choice([45, 80, 280, 315])
            self.setheading(new_direction)



