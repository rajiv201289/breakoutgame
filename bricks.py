from turtle import Turtle
import random

import bricks

col = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']

class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.color(random.choice(col))
        self.shapesize(stretch_wid=1.5,stretch_len=3)
        self.penup()
        self.goto(x=x_cor,y=y_cor)

        # Defining borders of the brick
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 20
        self.bottom_wall = self.ycor() - 20


class Bricks:
    def __init__(self):
        self.y_start =60
        self.y_end = 240
        self.bricks = []
        self.creat_all_lanes()
    def creat_lane(self,y_cor):
        for i in range(-300,300,60):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)
    def creat_all_lanes(self):
        for i in range(self.y_start,self.y_end,30):
            self.creat_lane(i)



