from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.speed_of_car = STARTING_MOVE_DISTANCE
        self.start()

    def speed_up(self):
        self.speed_of_car += MOVE_INCREMENT

    def start(self):
        self.goto(300, y= random.randint(-230,190))
        self.move_left()

    def move_left(self):
        self.forward(self.speed_of_car)
    

