from turtle import Turtle

FONT  = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(-250,260)
        self.score = 1
        self.level()

    def level(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def level_up(self):
        self.score += 1
        self.level()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)