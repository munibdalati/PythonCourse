import random
from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
all_turtles = []
is_race_on = False

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    i += i
    new_turtle.goto(x=-230, y=y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"you've won, the winner is {wining_color}")
                break
            else:
                print(f"you've lost, the winner is {wining_color}")
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)


screen.exitonclick()
