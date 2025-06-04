from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("red")
        self.goto(0, 270)
        self.hideturtle()
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
             # self.content
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open ("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)