from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 350)
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 24, "bold"))
        self.hideturtle()

    def updateScoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", align="center",
                   font=("Arial", 24, "bold"))

    def gameOver(self):
        self.goto(-10, 0)
        self.write("GAME OVER",
                   font=("Arial", 24, "bold"))
