from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


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


game_on = True
while game_on:
    screen.update()
    time.sleep(.05)
    game_ball.move()

    # Detect collision
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce()

    if game_ball.xcor() > 380 or game_ball.xcor() < -380:
        game_ball.hit()

screen.exitonclick()