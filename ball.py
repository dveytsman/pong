from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1