from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(pos)
    
    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -220:
            self.goto(self.xcor(), self.ycor() - 20)