from turtle import Screen
from net import Net
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
new_net = Net()

# Prepare for paddles
screen.listen()
screen.register_shape("paddle", ((-4, -30),(-4, 30), (4, 30), (4, -30)))

# Create and move a paddle one
paddle1 = Paddle((380, 0))
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

# Create and move paddle two
# Create and move a paddle one
paddle2 = Paddle((-380, 0))
screen.onkey(paddle2.up, "q")
screen.onkey(paddle2.down, "a")

# Create the ball
ball = Ball()

# Keep score
new_scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.008)

    # Make the ball Move
    ball.travel()
    paddle1.travel()
    paddle2.travel()

    # Check for bounce on walls
    ball.try_bounce_top()
    ball.try_bounce_bottom()

    # check for bounce with paddle
    ball.try_paddle1_bounce(paddle1)
    ball.try_paddle2_bounce(paddle2)

    # check if ball out of bounds for scoring
    if ball.xcor() < -410:
        new_scoreboard.increase_player1_score()
        ball.hideturtle()
        ball = Ball()

    if ball.xcor() > 410:
        new_scoreboard.increase_player2_score()
        ball.hideturtle()
        ball = Ball()

    if new_scoreboard.player1_score > 5 or new_scoreboard.player2_score > 5:
        new_scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
