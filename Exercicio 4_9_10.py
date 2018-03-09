import turtle

def draw_star(t,length):
    for i in range(5):
        t.left(-144)
        t.forward(length)
        t.hideturtle()

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("fuchsia")          
tess.pensize(3)

for i in range(5):
    draw_star(tess,100)
    tess.penup()
    tess.right(144)
    tess.forward(350)
    tess.pendown()

wn.mainloop()