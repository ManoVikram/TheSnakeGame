from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        super().__init__()
        self.turtles = []
        self.createSnake()
        self.head = self.turtles[0]

    def createSnake(self):
        for postion in STARTING_POSITIONS:
            turtle = Turtle("square")
            # turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(postion)
            self.turtles.append(turtle)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            newX = self.turtles[i - 1].xcor()
            newY = self.turtles[i - 1].ycor()
            self.turtles[i].goto(newX, newY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == UP or self.head.heading() == DOWN:
            return
        self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP or self.head.heading() == DOWN:
            return
        self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == LEFT or self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT or self.head.heading() == RIGHT:
            return
        self.head.setheading(RIGHT)
