from turtle import Turtle

FONT=("courier", 25, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-380,220)
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level +=1
        self.update_scoreboard

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)    