from turtle import Turtle
import random
import time


class Food(Turtle):
    """A class to represent the food in the Snake game."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        """Relocate the food to a new random position."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)