from turtle import Turtle
start_position = [(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segement=[]
        self.create()
        self.head=self.segement[0]


    # turtle position
    def create(self):
        for position in start_position:
            self.add_segement(position)

    def add_segement(self,position):
        my_segement = Turtle("square")
        my_segement.color("white")
        my_segement.penup()
        my_segement.goto(position)
        self.segement.append(my_segement)

    #Extend the tail or turtle
    def extend(self):
        self.add_segement(self.segement[-1].position())




    def move(self):
        for seg_num in range(len(self.segement) - 1, 0, -1):
            new_x = self.segement[seg_num - 1].xcor()
            new_y = self.segement[seg_num - 1].ycor()
            self.segement[seg_num].goto(new_x, new_y)
        self.head.forward(20)
    def UP(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def DOWN(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def RIGHT(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def LEFT(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)











