import time
import turtle

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.bgcolor("white")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 295 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        scoreboard.update_scoreboard()
    # Detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
