from turtle import Turtle,Screen,bgcolor
from bonus_point import Bonuspoint
from snake import Snake
from snake_food import Food
from score_point import Scorepoint
from score_board import Board
import random
import time
C = bgcolor("black")
screen = Screen()
screen.title("Snake Game")
screen.setup(600,600)

screen.tracer(0)
#creating a snake
snake = Snake()
snake_food = Food()
ob_score_point = Scorepoint()
bonus_second = 0

#controlling the snake
screen.listen()
score_board = Board()

heading1 = snake.list_turtle[0].heading()

screen.onkey(fun=snake.snake_forward, key="Up")
screen.onkey(fun=snake.snake_backward, key="Down")
screen.onkey(fun=snake.snake_left, key="Left")
screen.onkey(fun=snake.snake_right, key="Right")

flag = True
count = 200
food_eaten = 0
ob_of_Bonus_point = Bonuspoint()
ob_of_Bonus_point.temp_position()
hm = False

while flag:
    snake_pos_x = snake.list_turtle[0].xcor()
    snake_pos_y = snake.list_turtle[0].ycor()
    if(snake_pos_x < -276 or snake_pos_x > 276 or snake_pos_y > 276 or snake_pos_y < -276):
        flag = False
        score_board.game_over()
    screen.update()
    time.sleep(0.1)

    if hm==True:
        if(snake.list_turtle[0].distance(ob_of_Bonus_point)<25):
            ob_of_Bonus_point.clearing()
            ob_of_Bonus_point.temp_position()
            count = 0
            count += 600
            hm = False
            bonus_second = 0
            if(food_eaten%6==0):
                ob_score_point.score_point_of_snake += count
                ob_score_point.score_point_refresh()
                count = 200
        else:
            if(bonus_second>50):
                ob_of_Bonus_point.clearing()
                ob_of_Bonus_point.temp_position()
                hm = False
                bonus_second = 0
            else:
                bonus_second += 1


    if snake.list_turtle[0].distance(snake_food) < 15:
        food_eaten += 1
        ob_score_point.score_point_of_snake += count
        ob_score_point.score_point_refresh()
        score_board.score += 1
        score_board.score_track()

        if food_eaten%6==0:
            ob_of_Bonus_point.bonus_score()
            snake_food.refresh()
            hm = True

        else:
            snake_food.refresh()
            snake.extend()
        count = 200

    else:
        count-=3
        if count <= 0:
            count = 5
    for i in snake.list_turtle[1:]:
        if snake.list_turtle[0].distance(i) < 10:
            flag = False
            score_board.game_over()



    snake.snake_move()


screen.exitonclick()