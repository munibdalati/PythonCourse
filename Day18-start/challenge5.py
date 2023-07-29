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


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.speed("fastest")


draw_spirograph(20)




screen = Screen()
screen.exitonclick()

