from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time 

FONT = ("Arial", 13, "normal")

screen = Screen()
screen.setup(width=screen.window_width(), height=screen.window_height())
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:   
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collosion with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extand()
        scoreboard.increase_score()
    #Detect collosion of wall
    if (snake.head.xcor() > screen.window_width()/2 or snake.head.xcor() < -screen.window_width()/2 or 
    snake.head.ycor() > screen.window_height()/2 or snake.head.ycor() < -screen.window_height()/2):
        game_is_on = False

    #if snake head touchs the any segment:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
        
scoreboard.GameOver()
        


screen.exitonclick()
