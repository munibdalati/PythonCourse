import random
from turtle import Screen
import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

num_sides = 3
for i in range(10):
    for i in range(num_sides):
        tim.forward(125)
        tim.right(360 / num_sides)
    num_sides += 1
    tim.pencolor(random.choice(colours))

screen = Screen()
screen.exitonclick()
