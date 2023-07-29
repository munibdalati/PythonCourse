import turtle as t
from turtle import Screen

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

for i in range(4):
    tim.forward(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()