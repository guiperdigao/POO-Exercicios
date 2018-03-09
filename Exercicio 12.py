import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Relogio")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

size = 20

for i in range(12):
    tess.penup()
    tess.forward(75)
    tess.pendown()
    tess.forward(15)
    tess.penup()
    tess.forward(10)
    tess.stamp()
    tess.left(180)
    tess.forward(100)
    tess.left(150)

wn.mainloop()