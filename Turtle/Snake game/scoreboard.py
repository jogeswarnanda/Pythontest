from turtle import Turtle, Screen
import random
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")    

class Score(Turtle):
    """A class to manage the scoreboard in the Snake game."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT))
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=(FONT))

    def reset(self):
        self.score = 0
        self.update_scoreboard()
