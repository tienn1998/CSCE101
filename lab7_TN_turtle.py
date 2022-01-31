# Tien Nguyen
# Section #
# 01/20/2022
# tienn@email.sc.edu
# lab 7 red vs blue
import turtle
import random
red = []
blue = []
running = True
speed = 2
invisible = turtle.Turtle()
invisible.width(4)
invisible.hideturtle()
invisible.penup()
invisible.right(90)
invisible.forward(300)
invisible.left(90)
invisible.pendown()
invisible.circle(300)
for i in range(4):
    red.append(turtle.Turtle())
    red[i].penup()
    red[i].shape('turtle')
    red[i].color('red')
    x = random.randint(-100, 0)
    y = random.randint(-100, 100)
    red[i].setposition(x, y)
    blue.append(turtle.Turtle())
    blue[i].penup()
    blue[i].shape('turtle')
    blue[i].color('blue')
    x = random.randint(0, 100)
    y = random.randint(-100, 100)
    blue[i].setposition(x, y)

def randMove():
    for i in range(4):
        degree = random.randint(0, 359)
        degree1 = random.randint(0, 359)
        red[i].left(degree)
        blue[i].left(degree1)

move = 0
elapsed_time = 0
while running:
    for i in range(4):
        red[i].forward(speed)
        blue[i].forward(speed)
        if red[i].distance(0,0) >= 300:
            red[i].color('black')
            red[i].goto(0,0)
        if blue[i].distance(0,0) >= 300:
            blue[i].color('black')
            blue[i].goto(0,0)
    move +=1
    if(move%30 == 0):
        randMove()
    elapsed_time += 1
    if elapsed_time == 1000:
        running = False
