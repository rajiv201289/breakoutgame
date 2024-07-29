from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('steel blue')
        self.shapesize(stretch_len=8, stretch_wid=1)
        self.penup()
        self.goto(0, -185)

    def go_l(self):
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def go_r(self):
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
