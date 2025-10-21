from turtle import Turtle
import random
import time


class Paddle(Turtle):
    """A class to represent the Paddle in the Pong game."""
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5,outline=None)
        self.speed("fastest")
        self.goto(position)
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)