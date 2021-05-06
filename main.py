from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
cars = []
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "w")

loop = 0
game_is_on = True
while game_is_on:
    loop += 1
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 200:
        player.get_in_position()
        scoreboard.level_up()
        for car in cars:
            car.speed_up()

    if loop % 6 == 0 and len(cars) < 16:
        car = CarManager()
        cars.append(car)
    
    for car in cars:
        car.move_left()
        if car.xcor() < -300:
            car.start()
    
    for car in cars:
        if car.distance(player.pos()) < 20:
            game_is_on = False
            scoreboard.game_over()

        
    


screen.exitonclick()