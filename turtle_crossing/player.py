from turtle import Turtle
start=(0,-280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(start)
        self.left(90)


    def move(self):
        self.forward(10)

    def goto_start(self):
        self.goto(start)
    
    def reached_finish(self):
        if self.ycor()>280:
            return True
        else:
            return False