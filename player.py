STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
    def moveup(self):
        self.forward(MOVE_DISTANCE)

    def restart_postion(self):
        self.goto(STARTING_POSITION)
    def  game_over(self):
        self.write("GAME OVER",align="center",font=('Arial',8,'normal'))