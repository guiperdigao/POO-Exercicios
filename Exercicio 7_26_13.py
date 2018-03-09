import math
import turtle

wn = turtle.Screen()
tess = turtle.Turtle()
tess.color("black")          
tess.pensize(3)
tess.penup()
tess.forward(-175)
tess.pendown()

pairs = [(50,-90),(50,90),(50,90),(50,90),(25*math.sqrt(2),-135),(25*math.sqrt(2),-90)]

for (dist,degrees) in pairs:
    tess.left(degrees)
    tess.forward(dist)

tess.penup()
pairs = [(50,-45),(100,90)]

for (dist,degrees) in pairs: #walk to next point
    tess.left(degrees)
    tess.forward(dist)

tess.pendown()
pairs = [(50*math.sqrt(2),135),(25*math.sqrt(2),-90),(25*math.sqrt(2),-90),(50,-135),(50,90),(50,90),(50,90)]
for (dist,degrees) in pairs:
    tess.left(degrees)
    tess.forward(dist)

tess.penup()
pairs = [(50,180),(75,90)]

for (dist,degrees) in pairs: #walk to next point
    tess.left(degrees)
    tess.forward(dist)
tess.pendown()

pairs = [(50,0),(50,90),(50,90),(50,90),(25*math.sqrt(2),-135),(50*math.sqrt(2),-90),(50*math.sqrt(2),-90),
(25*math.sqrt(2),-90)]

for (dist,degrees) in pairs:
    tess.left(degrees)
    tess.forward(dist)

tess.penup()
pairs = [(75,135),(50*math.sqrt(2),45)]

for (dist,degrees) in pairs: #walk to next point
    tess.left(degrees)
    tess.forward(dist)
tess.pendown()

pairs = [(50*math.sqrt(2),180),(25*math.sqrt(2),-90),(50*math.sqrt(2),-90),(50*math.sqrt(2),-90),
(25*math.sqrt(2),-90),(50*math.sqrt(2),-90),(50,135),(50,90),(50,90),(50,90)]

for (dist,degrees) in pairs:
    tess.left(degrees)
    tess.forward(dist)

tess.hideturtle()
wn.mainloop()
