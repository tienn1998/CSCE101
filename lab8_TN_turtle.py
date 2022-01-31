# Tien Nguyen
# Section #
# 01/29/2022
# tienn@email.sc.edu
# lab 8 collision
import turtle
import random
invisible = turtle.Turtle()
invisible.width(4)
invisible.hideturtle()
invisible.penup()
invisible.right(90)
invisible.forward(250)
invisible.left(90)
invisible.pendown()
invisible.circle(250)
invisible.penup()
invisible.setposition(300,300)
invisible.write('Tien Nguyen')
colors = ['green', 'pink', 'blue', 'brown']
turtles = []
running = True
speed = 2
for i in range(8):
    turtles.append(turtle.Turtle())
    turtles[i].penup()
    turtles[i].shape('turtle')
    c = random.randint(0,3)
    turtles[i].color(colors[c])
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    turtles[i].setposition(x, y)

def randMove():
    for i in range(8):
        degree = random.randint(0, 359)
        turtles[i].left(degree)

move = 0
elapsed_time = 0
while running:
    for i in range(8):
        turtles[i].forward(speed)
        if turtles[i].distance(0,0) >= 250:
            turtles[i].color('black')
            turtles[i].goto(0,0)
        for j in range(8):
            if i != j:
                if turtles[i].distance(turtles[j].xcor(), turtles[j].ycor()) <= 30:
                    turtles[i].color('red')
                    turtles[j].color('red')
    move +=1
    if(move%30 == 0):
        randMove()
    elapsed_time += 1
    if elapsed_time == 1000:
        running = False

