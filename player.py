from turtle import Turtle


class Player(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(4, 0.5)
        self.goto(pos)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 60)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 60)
