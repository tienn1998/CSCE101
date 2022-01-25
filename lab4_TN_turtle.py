# Tien Nguyen
# Section #
# 01/20/2022
# tienn@email.sc.edu
# lab 4 drawing shape
import turtle
tienNguyen = turtle.Turtle()
turtle.Screen().bgcolor('teal')
tienNguyen.width(2)
colors = ["orange","red","yellow","green"]
for i in range(40):
    tienNguyen.color(colors[i%4])
    tienNguyen.forward(15 + (4*i))
    tienNguyen.left(45)
