from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 250)

    def update_score(self):
        self.write(f"{self.score_player1}         {self.score_player2}", align="center", font=("Arial", 36, "normal"))

    def increase_score(self, player):
        if player == 1:
            self.score_player1 += 1
        else:
            self.score_player2 += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over ", align="center", font=("Arial", 36, "normal"))
