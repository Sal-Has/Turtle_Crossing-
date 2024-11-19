FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()

    def increase_level(self):
        self.level+=1
        self.clear()
        self.display()
    def display(self):
        self.goto(-250, 240)
        self.write(f"Level:{self.level}",align="left",font=FONT)
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over.",move=False,align="center",font=FONT)
