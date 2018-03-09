import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Formas geometricas")      # Set the window title

tess = turtle.Turtle()
tess.color("blue")            # Tell tess to change her color
tess.pensize(3)               # Tell tess to set her pen width

for i in range(3):
 tess.forward(50)
 tess.left(120)

for i in range(4):
 tess.forward(50)
 tess.left(90)

for i in range(6):
 tess.forward(50)
 tess.left(60)

for i in range(8):
 tess.forward(50)
 tess.left(45)

wn.mainloop()