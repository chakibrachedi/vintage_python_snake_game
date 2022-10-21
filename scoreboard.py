from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)