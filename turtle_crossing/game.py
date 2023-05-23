from turtle import Turtle, Screen
import time
from player import Player
from car import Car
from scoreboard import ScoreBoard

score=ScoreBoard()
screen=Screen()
screen.title("The Turtle Crossing Game")
screen.setup(800,600)
screen.tracer(0)

car=Car()
tim=Player()
screen.listen()
screen.onkeypress(tim.move,"Up")



game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
   
    car.create_car()
    car.move_car()

    score.update_scoreboard()

    for a_car in car.all_cars:
        if a_car.distance(tim)<20:
            game_on=False
            score.game_over()


    if tim.reached_finish():
        tim.goto_start()
        car.level_up()
        score.level_up()
    

screen.exitonclick()