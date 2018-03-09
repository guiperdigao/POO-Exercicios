import turtle
wn = turtle.Screen()

tess = turtle.Turtle()
tess.color("black")          
tess.pensize(3) 

for i in range(5):
    tess.left(-144)
    tess.forward(100)
tess.hideturtle()
wn.mainloop()