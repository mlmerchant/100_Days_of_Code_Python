from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
SAVE_FILE = "high_score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open(SAVE_FILE) as file:
            self.high_score = int(file.read())
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(SAVE_FILE, mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        score_message = "Score: " + str(self.score) + "   " + "High Score: " + str(self.high_score)
        self.write(score_message, move=False, align=ALIGNMENT, font=FONT)
