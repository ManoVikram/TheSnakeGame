from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
food = Food()

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
        food.refresh()

screen.exitonclick()
