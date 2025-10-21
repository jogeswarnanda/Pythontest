from turtle import Turtle, Screen
import random
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")    

class Score(Turtle):
    """A class to manage the scoreboard in the Pong game."""

    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(-100, 200)
        self.write(self.lscore, align=ALIGNMENT, font=(FONT))
        self.goto(100, 200) 
        self.write(self.rscore, align=ALIGNMENT, font=(FONT))
        self.update_scoreboard()
    def l_point(self):
        self.lscore += 1
        self.update_scoreboard()
    def r_point(self):
        self.rscore += 1
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align=ALIGNMENT, font=(FONT))
        self.goto(100, 200) 
        self.write(self.rscore, align=ALIGNMENT, font=(FONT))
        
   
