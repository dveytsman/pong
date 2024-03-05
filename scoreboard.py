from turtle import Turtle

FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.goto(0, 250)
        self.write(f"{self.left_player_score} : {self.right_player_score}", align="center", font=FONT)

    def left_player_scored(self):
        self.left_player_score += 1
        self.update_score()
    
    def right_player_scored(self):
        self.right_player_score += 1
        self.update_score()

    def show_score(self):
        self.write(f"{self.left_player_score} : {self.right_player_score}", align="center", font=FONT)
    
    def update_score(self):
        self.clear()
        self.show_score()

