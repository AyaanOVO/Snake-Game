from turtle import Turtle,Screen,bgcolor
class Scorepoint(Turtle):
    score_point_of_snake = 0
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280,-280)
        self.write(f"Score point: {self.score_point_of_snake}",font=("Arial", 15, "bold"))

    def score_point_refresh(self):
        self.undo()
        self.write(f"Score point: {self.score_point_of_snake}",font=("Arial", 15, "bold"))

