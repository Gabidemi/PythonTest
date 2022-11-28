from turtle import *
from random import randint, choice as rand_choice


speed(0)

colors = ["blue", "purple", "Red","Green", "Yellow", "Gold", "Cyan"]
direction = [90,80,180,79,60, 270, 30, 90]
for i in range(200):
    penup()
    setposition(randint(-200,200),randint(-200,200))
    pendown()
    color(rand_choice(colors))
    pencolor(rand_choice(colors))
    fillcolor(rand_choice(colors))
    pensize(5)

    begin_fill()
    left(rand_choice(direction))
    circle(randint(10,60), steps=randint(4,12))
    end_fill()

done()