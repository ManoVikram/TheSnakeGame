from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highScoreData.txt") as file:
            self.highScore = int(file.read())
            # print(self.highScore)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 350)
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        # print(self.highScore)
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.highScore}", align="center",
                   font=("Arial", 24, "bold"))

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highScoreData.txt", mode="w") as fileWrite:
                fileWrite.write(f"{self.highScore}")
        self.score = 0
        self.updateScoreboard()

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    # def gameOver(self):
    #     self.goto(-10, 0)
    #     self.write("GAME OVER",
    #                font=("Arial", 24, "bold"))
