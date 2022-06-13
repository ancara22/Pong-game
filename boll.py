from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed_y = 1
        self.speed_x = 1
        self.speed = 5

    def move(self):
        margin_x = 390
        margin_y = 290
        #if self.xcor() > margin_x or self.xcor() < -margin_x:
            #self.speed_x = -self.speed_x

        if self.ycor() > margin_y or self.ycor() < -margin_y:
            self.speed_y = -self.speed_y


        x = self.xcor() + (self.speed * self.speed_x)
        y = self.ycor() + (self.speed * self.speed_y)
        self.goto(x, y)



