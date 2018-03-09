import turtle
wn = turtle.Screen()

tess = turtle.Turtle()
tess.color("black")          
tess.pensize(3) 

def draw_star(t,length):
    for i in range(5):
        t.left(-144)
        t.forward(length)
        t.hideturtle()

draw_star(tess,100)
wn.mainloop()