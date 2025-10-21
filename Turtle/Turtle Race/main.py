from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()   
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Guess the Winner", prompt="Which turtle will win the race? Enter a color: ")
#print(f"You bet on: {user_bet}")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
all_turtles = []

 
for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")      
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-70 + turtle_index * 30)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

pen = Turtle()

while is_race_on:
    
    for turtle in all_turtles:     
        random_distance = random.randint(0, 10)      
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
                pen.write(f"You win! The {winning_color} turtle is the winner!", align="center", font=("Courier", 20, "bold"))

            else:
                print(f"You lose! The {winning_color} turtle is the winner!")
                pen.write(f"You Loose! The {winning_color} turtle is the winner!", align="center", font=("Courier", 20, "bold"))

            
            is_race_on = False                   
        

screen.exitonclick()