from turtle import Turtle, Screen
import random
tim = Turtle()
#turtle_module.colormode(255)

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)

screen = Screen()
screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.onkey(change_color, "x")
screen.exitonclick()
