import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()


player = Player()
screen.onkey(fun=player.moveup,key="Up")
car_manager = CarManager()
car_manager.hideturtle()
scoreboard = Scoreboard()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.display()
    car_manager.create_cars()

    car_manager.move_car()

    for car in car_manager.cars:
        if player.distance(car)<15:
            scoreboard.gameover()
            game_is_on = False

        if player.ycor() >= 280:
            scoreboard.increase_level()
            car_manager.increase_speed()
            player.restart_postion()



screen.exitonclick()




