from turtle import Turtle
import turtle
import pandas

screen = turtle.Screen()
screen.title("Middle East Countries game")
image = "middle_east_blank.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("countries.csv")
all_countries = data["country"].to_list()
print(all_countries)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


correct_guesses = []
while len(correct_guesses) < 15:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/15 Countries Correct",
                                    prompt="What is the another country?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_countries:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("not_guessed_countries.csv")
        break
    if answer_state in all_countries:
        correct_guesses.append(answer_state)
        state_data = data[data.country == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(answer_state)
        print(correct_guesses)

screen.exitonclick()



