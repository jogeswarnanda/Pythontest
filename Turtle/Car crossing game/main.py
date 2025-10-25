import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
            print("Game Over")

    # Detect successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        score.increase_level()
        print("Level Up!")
    
screen.exitonclick()
