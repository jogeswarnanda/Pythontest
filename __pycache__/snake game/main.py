from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

#for position in starting_positions:
#    new_segment = Turtle("square")
##    new_segment.color("white")
 #   new_segment.penup()
 #   new_segment.goto(position)
 #   segments.append(new_segment)

snake = Snake()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
#    for seg_num in range(len(segments) - 1, 0, -1):
##        new_x = segments[seg_num - 1].xcor()
#        new_y = segments[seg_num - 1].ycor()
#        segments[seg_num].goto(new_x, new_y)
#    segments[0].forward(20)
#    segments[0].left(90)
    
screen.exitonclick()