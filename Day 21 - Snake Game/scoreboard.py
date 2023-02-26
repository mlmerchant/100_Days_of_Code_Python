import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        Score_Message = "Score:  " + str(self.score)
        self.write(Score_Message, move=False, align=ALIGNMENT, font=FONT)