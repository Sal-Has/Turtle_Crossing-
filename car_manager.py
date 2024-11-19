COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
XVALUE = 300

from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self) :
        super().__init__()
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_choice=random.randint(1,6)
        if random_choice == 1:
            new_turtle = Turtle("square")
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.seth(180)
            new_turtle.turtlesize(1,2)
            new_turtle.color(random.choice(COLORS))
            new_turtle.goto(300,random.randint(-250,250))
            self.cars.append(new_turtle)


    def move_car(self):
        for i in self.cars:
            i.showturtle()
            i.forward(self.move_speed)
    def increase_speed(self):
        self.move_speed +=MOVE_INCREMENT
