from turtle import Turtle, Screen
import time

screen = Screen()

screen.setup(width=750, height=750)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

turtles = []
initialPositions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for i in range(3):
    turtle = Turtle("square")
    # turtle.shape("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(initialPositions[i])
    turtles.append(turtle)

isPlaying = True

while isPlaying:
    screen.update()
    time.sleep(0.1)
    for i in range(len(turtles) - 1, 0, -1):
        newX = turtles[i - 1].xcor()
        newY = turtles[i - 1].ycor()
        turtles[i].goto(newX, newY)
    turtles[0].forward(20)

screen.exitonclick()
