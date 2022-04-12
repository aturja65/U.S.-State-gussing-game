import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("U.S. State guessing game")
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
entered_states = []
unanswered_states = []
while len(entered_states) < 50:
    answer = screen.textinput(title=f"{len(entered_states)}/50 correct guessed", prompt="Enter a state name").title()
    if answer == "Exit":
        for state in states:
            if state not in entered_states:
                unanswered_states.append(state)
        new = pandas.DataFrame(unanswered_states)
        new.to_csv("Unanswered states.csv")
        break
    if answer in states:
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(int(data[data.state == answer].x), int(data[data.state == answer].y))
        state.write(answer)
        entered_states.append(answer)
