import turtle

t = turtle.Turtle()


t.color("yellow")
t.goto(-50,-20)
t.begin_fill()
t.goto(50,-20)
t.goto(50,60)
t.goto(-50,60)
t.end_fill()


t.goto(-50,60)
t.color("red")
t.begin_fill()
t.goto(0,120)
t.goto(50,60)
t.end_fill()

t.penup()
t.home()
t.pendown()
t.color("blue", "blue")

t.begin_fill()
t.circle(18)
t.end_fill()

t.penup()
t.goto(-70,-20)












