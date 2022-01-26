# Tien Nguyen
# Section #
# 01/25/2022
# tienn@email.sc.edu
# lab 5 control turtle with keyboard
import turtle
interface = turtle.Screen()
chocolate = turtle.Turtle()
chocolate.shape('turtle')
chocolate.color('pink')

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

# Turn 90 degree 
def turn90():
    chocolate.left(90)

# stop the turtle just press 'up' arrow 
def stop():
    global speed
    speed = 0
    
interface.listen()
interface.onkey(up, 'Up')
interface.onkey(down, 'Down')
interface.onkey(left, 'Left')
interface.onkey(right, 'Right')
interface.onkey(home, 'space')
interface.onkey(turn90, 'p')
interface.onkey(stop, 'q')

while running:
    chocolate.forward(speed)
