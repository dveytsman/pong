from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

game_ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "i")
screen.onkey(r_paddle.down, "k")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

score = ScoreBoard()
game_on = True
while game_on:
    screen.update()
    time.sleep(.05)
    game_ball.move()

    # Detect collision
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce()

    if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320:
        game_ball.hit()
    
    if game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.hit()

    # detect if the right paddle missed
        
    if game_ball.xcor() > 400:
        game_ball.reset()
        score.left_player_scored()

    if game_ball.xcor() < -400:
        game_ball.reset()
        score.right_player_scored()

screen.exitonclick()