from turtle import Turtle, Screen
from random import choice as rand_choice, randint


colors = ["blue", "purple", "Red","Green", "Yellow", "Gold", "Cyan"]
direction = [90,80,180,79,60, 270, 30, 90]

class MyTurtle(Turtle):
    def random_shape(self, x ,y):
        self.color(rand_choice(colors))
        self.penup()
        self.setposition(randint(-200, 200), randint(-200,200))
        self.pendown()
        self.circle(randint(10,60), steps=randint(4,12))

    def __init__(self):
        super().__init__()
        self.random_shape(0, 0)
        self.onclick(self.random_shape)


x = MyTurtle()
y = MyTurtle()

x.forward(50)
y.backward(50)

screen = Screen()

screen.mainloop()

