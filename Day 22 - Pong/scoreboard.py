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
        self.goto(0, 270)
        self.player1_score = 0
        self.player2_score = 0
        self.refresh()

    def increase_player1_score(self):
        self.player1_score += 1
        self.refresh()

    def increase_player2_score(self):
        self.player2_score += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        if self.player1_score > self.player2_score:
            game_message = "Player 1 wins!"
        else:
            game_message = "Player 2 wins!"
        self.write(game_message, move=False, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        score_message = "Player 2:  " + str(self.player2_score) + "         " + "Player 1:  " + str(self.player1_score)
        self.write(score_message, move=False, align=ALIGNMENT, font=FONT)