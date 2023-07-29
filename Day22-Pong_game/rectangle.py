from turtle import Turtle


class Rectangle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.right(90)
        self.forward(300)
        self.right(90)
        self.forward(360)
        self.pendown()
        self.color("white")
        self.right(90)
        self.forward(600)
        self.right(90)
        self.forward(720)
        self.right(90)
        self.forward(600)
        self.right(90)
        self.forward(720)
        self.right(90)
        self.hideturtle()

    def line(self):
        self.penup()
        self.goto(0, 300)
        self.right(180)
        self.pendown()
        for i in range(12):
            self.pendown()
            self.color("white")
            self.forward(25)
            self.penup()
            self.forward(25)



