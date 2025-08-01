import turtle
import random

win = turtle.Screen()
win.bgcolor("black")
ball = turtle.Turtle()
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.speed(0)

ball.goto(0, 0)
dx = 3
dy = 2

while True:
    x, y = ball.pos()
    x += dx
    y += dy

    if abs(x) > 300:
        dx *= -1
    if abs(y) > 300:
        dy *= -1

    ball.goto(x, y)
