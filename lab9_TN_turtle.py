# Tien Nguyen
# Section #
# 01/29/2022
# tienn@email.sc.edu
# lab 9 sharks vs hunters
import turtle
interface = turtle.Screen()
invisible = turtle.Turtle()
invisible.width(4)
invisible.hideturtle()
invisible.penup()
invisible.right(90)
invisible.forward(300)
invisible.left(90)
invisible.pendown()
invisible.circle(300)
hunter = turtle.Turtle()
hunter.shape('turtle')
hunter.color('red')
hunter.penup()
sharks = []
for i in range(2):
    sharks.append(turtle.Turtle())
    sharks[i].penup()
    sharks[i].shape('arrow')
    sharks[i].color('black')
    if i == 0:
        sharks[i].setposition(-100, 0)
    else:
        sharks[i].setposition(100, 0)

speed = 1
speedHunter = 1
running = True
def up():
    global speedHunter
    if speedHunter <= 10:
        speedHunter += 1

def down():
    global speedHunter
    if speedHunter > 1:
        speedHunter -= 1

def left():
    hunter.left(15)

def right():
    hunter.right(15)

interface.listen()
interface.onkey(up, 'Up')
interface.onkey(down, 'Down')
interface.onkey(left, 'Left')
interface.onkey(right, 'Right')

while running:
    hunter.forward(speedHunter)
    if hunter.distance(0,0) > 300:
        hunter.goto(0,0)
    for i in range(2):
        angleToHunter = sharks[i].towards(hunter)
        sharks[i].setheading(angleToHunter)
        sharks[i].forward(speed)
