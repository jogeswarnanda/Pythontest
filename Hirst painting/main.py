import turtle as turtle_module
import random
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(240, 239, 238), (242, 117, 31), (240, 79, 94), (240, 95, 34), (154, 113, 8), (128, 215, 206), (212, 153, 163), (150, 186, 224), (167, 45, 137), (51, 91, 86), (85, 183, 4), (29, 37, 42), (132, 218, 221), (249, 207, 0), (240, 231, 235), (227, 237, 233), (211, 130, 19), (246, 208, 47), (134, 188, 147), (229, 168, 179), (88, 96, 101), (241, 171, 154), (164, 190, 224), (44, 78, 73), (33, 43, 42), (61, 63, 68), (116, 94, 6), (112, 134, 137), (47, 72, 73)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for i in range(1, number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()




