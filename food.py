from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        x_rand_Pos = random.randint(-230, 230)
        y_rand_Pos = random.randint(-230, 230)
        self.goto(x_rand_Pos, y_rand_Pos)

