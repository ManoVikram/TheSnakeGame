from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

isPlaying = True
while isPlaying:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.increaseScore()
        snake.extendSnake()
        food.refresh()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 350 or snake.head.ycor() < -380:
        scoreboard.reset()
        snake.reset()

    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
