from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

#screen backkground
screen = Screen()
screen.setup(width=500,height=500)
screen.bgcolor("black")
screen.title("This a snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.UP,"Up")
screen.onkey(snake.DOWN,"Down")
screen.onkey(snake.RIGHT,"Right")
screen.onkey(snake.LEFT,"Left")

#to run the program repeatly
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.4)

    snake.move()


    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
       #to increment the score
        score.score_num+=1
        score.score_increment()
       #to add the tail or turtle
        snake.extend()
    #Detect collision with wall
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() <-240:
        score.game_over()
        game_is_on=False


    #Detect collision with tail
    for segement in snake.segement[1:]:
        #if head collides with any other segement tail
        if snake.head.distance(segement) < 10:
            # trigger game_over
            game_is_on=False
            score.game_over()
















screen.exitonclick()