from turtle import Turtle
import random

move_distance=20
move_inc=10
colors=["red","blue","orange","purple","yellow","green"]


class Car(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.car_speed=move_distance
        

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance == 1:
            new_car=Turtle("square")
            new_car.penup()
            y_pos=random.randint(-250,250)
            new_car.goto(400, y_pos)
            new_car.color(random.choice(colors))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=move_inc
