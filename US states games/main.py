import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = turtle.textinput(title="Guess the State", prompt="What's another state's name?").title()
print(answer_state)

# if answer_state == "Texas":
#     t = turtle.Turtle()
#     t.hideturtle()
#     t.penup()
#     t.goto(100, -100)  # Coordinates for Texas on the map
#     t.write(answer_state)

data1 = pandas.read_csv("50_states.csv")
game_is_on = True
all_states = data1.state.to_list()    
guessed_states = []   
while len(guessed_states) < 50 and game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        mstate = data1[data1.state == answer_state]
        mstate_xcor = mstate.x.item()
        mstate_ycor = mstate.y.item()
        #print(int(mstate_xcor), int(mstate_ycor))
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(mstate_xcor), int(mstate_ycor))
        t.write(answer_state)     

#commented out code from development process to exit out of turtle window once user types "Exit"
#turtle.mainloop()

# mstate = data1[data1.state == answer_state]
# mstate_xcor = mstate.x
# mstate_ycor = mstate.y
# print(int(mstate_xcor), int(mstate_ycor))
# t = turtle.Turtle()
# t.hideturtle()
# t.penup()
# t.goto(int(mstate_xcor), int(mstate_ycor))
# t.write(answer_state)
# all_states = data1.state.to_list()
# #print(all_states)   
#screen.exitonclick()