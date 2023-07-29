
from turtle import Screen
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()
