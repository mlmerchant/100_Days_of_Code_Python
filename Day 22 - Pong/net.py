from turtle import Turtle


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, -306)
        self.setheading(90)
        for x in range(0, 625, 9):
            if x % 2 == 0:
                self.pendown()
            else:
                self.penup()
            self.forward(9)
