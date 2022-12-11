from turtle import Turtle , Screen , bgcolor
import random
MOVE_DISTANCE = 20
TURTLE_LOCATION = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.list_turtle = []
        self.creating_snake()

    def creating_snake(self):
        for location in TURTLE_LOCATION:
            self.add_segment(location)

    def add_segment(self,location):
        mypet = Turtle("square")
        mypet.color("white")
        mypet.penup()
        mypet.goto(location)
        self.list_turtle.append(mypet)

    def extend(self):
        self.add_segment(self.list_turtle[len(self.list_turtle)-1].position())


    def snake_move(self):
        for i in range(len(self.list_turtle) - 1, 0, -1):
            x_position = self.list_turtle[i - 1].xcor()
            y_position = self.list_turtle[i - 1].ycor()
            self.list_turtle[i].goto(x_position, y_position)

        self.list_turtle[0].forward(MOVE_DISTANCE)


    def snake_forward(self):
        if(self.list_turtle[0].heading() != 270):
            self.list_turtle[0].setheading(90)

    def snake_backward(self):
        if (self.list_turtle[0].heading() != 90):
            self.list_turtle[0].setheading(270)

    def snake_left(self):
        if (self.list_turtle[0].heading() != 0):
            self.list_turtle[0].setheading(180)

    def snake_right(self):
        if (self.list_turtle[0].heading() != 180):
            self.list_turtle[0].setheading(0)





