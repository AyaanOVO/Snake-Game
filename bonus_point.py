from turtle import Turtle,Screen
import random
class Bonuspoint(Turtle):
    def __init__(self):
        super().__init__()


    def temp_position(self):
        self.goto(-600,-600)

    def bonus_score(self):
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=1,stretch_len=1)
        x_value = random.randint(-260,260)
        y_value = random.randint(-260,260)
        self.goto(x_value,y_value)

    def clearing(self):
        for i in range(10):
            self.undo()
