# Tien Nguyen
# Section #
# 01/26/2022
# tienn@email.sc.edu
# lab 6 control turtle 2
import turtle
import random
interface = turtle.Screen()
chocolate = turtle.Turtle()
chocolate.shape('turtle')
chocolate.color('pink')
tiger = turtle.Turtle()
tiger.shape('arrow')
tiger.color('blue')

slow = 1
speed = 1
running = True
def up():
    global speed
    if speed <= 15:
        speed = speed + 1

def down():
    global speed
    if speed > 1:
        speed = speed - 1

def left():
    chocolate.left(15)

def right():
    chocolate.right(15)

def home():
    chocolate.penup()
    chocolate.goto(0, 0)
    global speed
    speed = 1
    chocolate.pendown()

def homev2():
    tiger.penup()
    tiger.goto(0, 0)
    tiger.pendown()

# Turn 90 degree
def turn90():
    chocolate.left(90)

# stop the turtle just press 'up' arrow
def stop():
    global speed
    speed = 0

def randMove():
    degree = random.randint(0, 359)
    tiger.left(degree)

interface.listen()
interface.onkey(up, 'Up')
interface.onkey(down, 'Down')
interface.onkey(left, 'Left')
interface.onkey(right, 'Right')
interface.onkey(home, 'space')
interface.onkey(turn90, 'p')
interface.onkey(stop, 'q')

move = 0
randMove()
while running:
    chocolate.forward(speed)
    if chocolate.distance(0,0) > 250:
        home()
    tiger.forward(slow)
    move += 1
    if tiger.distance(0,0) > 250:
        homev2()
    if(move%30 == 0):
        randMove()
