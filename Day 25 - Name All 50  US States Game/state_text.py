from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 6, 'normal')


class StateText(Turtle):

    def __init__(self, text, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x, y)
        self.write(text, move=False, align=ALIGNMENT, font=FONT)
