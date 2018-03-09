import turtle
import math

wn = turtle.Screen()
tess = turtle.Turtle()
tess.color("black")          
tess.pensize(3)

pairs = [(50*math.sqrt(2),45),(25*math.sqrt(2),90),(25*math.sqrt(2),90),(50*math.sqrt(2),90),(50,135),(50,90),(50,90),(50,90)]

for (dist,degrees) in pairs:
    tess.left(degrees)
    tess.forward(dist)

tess.hideturtle()
wn.mainloop()