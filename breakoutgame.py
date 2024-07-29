from turtle import Screen,Turtle
from paddle import Paddle
from bricks import Bricks
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height=400)
screen.title('Break Out')
screen.tracer(0)

paddle = Paddle()
bricks = Bricks()
ball = Ball()



screen.listen()
screen.onkey(paddle.go_l,'Left')
screen.onkey(paddle.go_r,'Right')


def check_collision_with_bricks():
    global ball, score, bricks

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.goto(3000, 3000)
            bricks.bricks.remove(brick)

            if ball.xcor()<brick.left_wall:
                ball.bouncex()
            elif ball.xcor()>brick.right_wall:
                ball.bouncex()
            elif ball.ycor()<brick.bottom_wall:
                ball.bouncey()
            elif ball.ycor()>brick.upper_wall:
                ball.bouncex()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>179:
        ball.bouncey()
    if ball.xcor()>275 or  ball.xcor()<-278:
        ball.bouncex()
    if ball.distance(paddle)<70 and ball.ycor()<-155:
        ball.bouncey()
    if ball.ycor()<-190:
        ball.reset_positoin()
        ball.bouncey()
        ball.bouncex()
    check_collision_with_bricks()



screen.exitonclick()