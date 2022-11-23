from turtle import *

def Eye():
    begin_fill()
    circle(25)
    end_fill()
    begin_fill()
    color("Black")
    circle(10)
    end_fill()

begin_fill()
color("#e6b800")
circle(100)
end_fill()

color("White")
left(90)
penup()
forward(100)
left(90)
forward(50)

#Eye
pendown()
color("White")
right(180)

Eye()

#Eye

color("White")
penup()
forward(100)
pendown()

Eye()

penup()
left(180)
forward(50)
left(90)
forward(40)
right(90)

#Mouth
pendown()
begin_fill()
color("Black")
circle(25)
end_fill()

left(90)
forward(50)
right(270)
begin_fill()
color("Pink")
circle(10)
end_fill()


done()