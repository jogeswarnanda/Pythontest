import random
import turtle as t
from turtle import Screen

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

timmy = t.Turtle()
timmy.speed("fastest")

def draw_spiral_graph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)

draw_spiral_graph(2)  
screen = t.Screen()
screen.exitonclick()


