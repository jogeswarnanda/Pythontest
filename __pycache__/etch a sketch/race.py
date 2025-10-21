from turtle import Turtle, Screen
import random
#turtle_module.colormode(255)
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
screen.bgcolor("white")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


user_bet = screen.textinput(title="Make your bet",prompt="Which color turle will win the rase?")
print(f"You bet on {user_bet}")

pen = Turtle()
pen.hideturtle()
pen.penup()
pen.goto(x=-0, y=0)


is_race_on = False
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + (turtle * 40))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
                pen.write(f"You've won! The {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "normal"))
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                pen.write(f"You've lost! The {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "normal"))
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

  


screen.exitonclick()
