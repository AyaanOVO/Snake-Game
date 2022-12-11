from turtle import Turtle,Screen
class Board(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-10,270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "bold"))


    def score_track(self):
        self.undo()
        self.write(f"Score: {self.score}",align="center",font=("Arial",15,"bold"))

    def game_over(self):
        self.goto(-20,0)
        self.write("Game Over", align="center", font=("Arial", 15, "bold"))










