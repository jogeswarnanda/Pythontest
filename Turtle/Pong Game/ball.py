from turtle import Turtle
import random
import time


class Ball(Turtle):
   """A class to represent the Ball in the Pong game."""
   def __init__(self,position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        #self.shapesize(stretch_len=1, stretch_wid=1,outline=None)
        self.speed("fastest")
        self.goto(position)
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

   def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

   def bounce_y(self):
        self.ymove = self.ymove * -1
        self.move_speed *= 0.9
   def bounce_x(self):
        self.xmove = self.xmove * -1
        self.move_speed *= 0.9
   def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.xmove *= -1