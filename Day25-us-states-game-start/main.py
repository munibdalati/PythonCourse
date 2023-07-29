from turtle import Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
print(all_states)


correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What is the another state?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("not_guessed_states.csv")
        break
    if answer_state in all_states:
        correct_guesses.append(answer_state)
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(answer_state)
        print(correct_guesses)


screen.exitonclick()



