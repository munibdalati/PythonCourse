import random
from turtle import Screen
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")


t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]


for i in range(100):
    tim.pensize(10)
    tim.forward(20)
    tim.speed("fastest")
    tim.setheading(random.choice(directions))
    tim.color(random_color())


screen = Screen()
screen.exitonclick()