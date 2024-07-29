import random
from turtle import  Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bouncey(self):
        self.y_move *= -1
    def bouncex(self):
        self.x_move *= -1
    def reset_positoin(self):
        self.goto(0,0)





