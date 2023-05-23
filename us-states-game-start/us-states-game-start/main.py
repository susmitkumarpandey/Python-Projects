import turtle, pandas

screen=turtle.Screen()
screen.title("U.S. States Game")
image="us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states=pandas.read_csv("us-states-game-start/50_states.csv")
correct_guesses=[]
tr=turtle.Turtle()
tr.penup()

game_on=True
while game_on:
    answer_state=screen.textinput(title="Guess the state", prompt="what's another state name")
    if answer_state==states.state:
        tr.goto(states.x,states.y)
        tr.write(answer_state)
        correct_guesses.append(answer_state)
    else:
        game_on=False


turtle.mainloop()