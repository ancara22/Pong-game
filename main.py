from turtle import Turtle, Screen
from score import Score
from player import Player
from boll import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

score = Score()
ball = Ball()
player1 = Player((-385, 0))
player2 = Player((375, 0))

line = Turtle()
line.speed("fastest")
line.hideturtle()
line.pen(pensize=1)
line.color("gray")
line.goto(0, 230)
line.goto(0, -260)

screen.update()
score.update_score()


def message():
    message = Turtle()
    message.hideturtle()
    message.color("white")
    message.write("Game over", align="center", font=("Arial", 36, "normal"))


game_over = True
while game_over:

    ball.move()
    screen.update()
    screen.listen()
    screen.onkeypress(player1.up, "w")
    screen.onkeypress(player1.down, "s")
    screen.listen()
    screen.onkeypress(player2.up, "Up")
    screen.onkeypress(player2.down, "Down")

    if ball.distance(player2) < 50 and ball.xcor() > 350 or ball.distance(player1) < 50 and ball.xcor() < -360:
        ball.speed_x = - ball.speed_x

    if ball.xcor() > 390:
        score.increase_score(1)
        time.sleep(0.5)
        ball.goto(0, 0)
        ball.speed_x = - ball.speed_x
        if score.score_player1 >= 3:
            score.game_over()
            game_over = False

    elif ball.xcor() < -390:
        score.increase_score(0)
        time.sleep(0.5)
        ball.goto(0, 0)
        ball.speed_x = - ball.speed_x
        if score.score_player2 >= 3:
            score.game_over()
            game_over = False






screen.exitonclick()
