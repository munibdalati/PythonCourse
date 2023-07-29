# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as t
from turtle import Screen
from turtle import Screen
t.colormode(255)
color_list = [(188, 19, 46), (244, 233, 64), (252, 232, 237), (217, 239, 245), (195, 76, 34), (218, 66, 106), (13, 143, 89), (18, 125, 173), (196, 176, 17), (108, 182, 209), (12, 167, 214), (208, 154, 91), (238, 232, 3), (25, 40, 75), (36, 43, 111), (78, 175, 96), (181, 44, 65), (217, 67, 47), (217, 129, 153), (125, 185, 120), (238, 161, 180), (7, 61, 38), (147, 209, 220), (8, 91, 52), (5, 86, 109), (160, 30, 27), (237, 170, 163), (158, 211, 188)]
tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for _ in range(10):
    for i in range(10):
        random_color = random.choice(color_list)
        tim.penup()
        tim.dot(20, random_color)
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)


screen = Screen()
screen.exitonclick()