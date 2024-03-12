from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_num = 0
        self.penup()
        self.goto(0,230)
        self.score_increment()
        self.hideturtle()




    def score_increment(self):
        self.color("white")
        self.clear()
        self.write(arg=f"Score: {self.score_num} ", move=False, align="center")
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER ", move=False, align="center")







