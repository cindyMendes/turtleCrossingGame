import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    screen.onkey(player.move_up, "Up")

    # detects collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detects a successful crossing
    if player.is_at_finnish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()




screen.exitonclick()