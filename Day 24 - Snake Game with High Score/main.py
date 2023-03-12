from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

MAP_EDGE = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.25)
    snake.move()

    # detect collision with self
    if snake.is_collision():
        scoreboard.reset()
        snake.reset()

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # detect collision with wall
    if snake.head.xcor() > MAP_EDGE or snake.head.xcor() < -MAP_EDGE or snake.head.ycor() > MAP_EDGE or snake.head.ycor() < -MAP_EDGE:
        scoreboard.reset()
        snake.reset()


screen.exitonclick()
