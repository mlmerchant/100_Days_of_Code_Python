import turtle
from random import choice

# set up the screen
wn = turtle.Screen()
spacing = 50

# Pick a winner
guess = wn.textinput("Place your bet.", "Enter the color of the winning turtle.").lower()

# create racers
racers = []
colors = ["red", "orange", 'yellow', "green", "blue", "indigo", "violet"]
for color in colors:
    racer = turtle.Turtle(shape="turtle")
    racer.color(color)
    racer.penup()
    racers.append(racer)

# set races at start
height = wn.window_height()
width = wn.window_width()

x = ((width / 2) - 10) * -1
y = 0

for racer in racers:
    racer.goto(x, y)
    if y == 0:
        y += spacing
    elif y > 0:
        y *= -1
    else:
        y = (y * -1) + spacing

# turtle race
racing = True
while racing:
    racer = choice(racers)
    racer.forward(10)
    if racer.xcor() > (width / 2):
        racing = False
    winner = (racer.color())[0]

# declare a winner
if guess == winner:
    print(f"You are correct, the {winner} turtle won!")
else:
    print(f"You lose, the {winner} turtle won!")

# keep the window open
wn.mainloop()