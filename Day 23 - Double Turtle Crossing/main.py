from turtle import Screen
from car import Car
from player import Player
from scoreboard import Scoreboard
import time

# Player 1 presses "Up Arrow"
# Player 2 presses "Q"

INCREASE_FACTOR = .07
NUM_OF_CARS = 25
speed = 1
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
STARTING_Y = -280
HIT_BOX = 10
WINNING_SCORE = 5

# Create the Screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Double Turtle Crossing")
screen.tracer(0)

# Prepare for paddles
screen.listen()

# Create and move a player one
player1 = Player((200, STARTING_Y), "blue")
screen.onkey(player1.up, "Up")


# Create and move player two
player2 = Player((-200, STARTING_Y), "green")
screen.onkey(player2.up, "q")


# Create the cars
cars = []
for _ in range(NUM_OF_CARS):
    cars.append(Car())

# Keep score
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.008)

    for car in cars:
        # Make the cars move
        car.forward(speed)
        # Respawn cars off the screen
        if car.xcor() > (SCREEN_WIDTH / 2 + car.random_heading()) or car.xcor() < (SCREEN_WIDTH / -2 - car.random_offset):
            car.setheading(car.random_heading())
            car.goto(car.random_starting_position())

    # Check if player1 scored
    if player1.ycor() > SCREEN_HEIGHT / 2 - 10:
        scoreboard.increase_player1_score()
        player1.goto(200, STARTING_Y)
        speed = speed + speed * INCREASE_FACTOR

    # Check if player2 scored
    if player2.ycor() > SCREEN_HEIGHT / 2 - 10:
        scoreboard.increase_player2_score()
        player2.goto(-200, STARTING_Y)
        speed = speed + speed * .5

    # check if player hit
    for car in cars:
        if car.distance(player1) < HIT_BOX:
            player1.goto(200, STARTING_Y)
        if car.distance(player2) < HIT_BOX:
            player2.goto(-200, STARTING_Y)

    if scoreboard.player1_score == WINNING_SCORE or scoreboard.player2_score == WINNING_SCORE:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
