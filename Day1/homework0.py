import turtle

# open window
wn = turtle.Screen()
wn.title("home")
wn.bgcolor("skyblue")   #sky color

pen = turtle.Turtle()
pen.speed(5)

# --- grass---
pen.penup()
pen.goto(-400, -100)
pen.pendown()
pen.color("green")
pen.begin_fill()
for _ in range(2):
    pen.forward(800)
    pen.right(90)
    pen.forward(300)
    pen.right(90)
pen.end_fill()

# --- home wall ---
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.color("black", "lightyellow")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# --- roof
pen.color("black", "brown")
pen.begin_fill()
pen.goto(-100, 100)
pen.goto(0, 200)
pen.goto(100, 100)
pen.goto(-100, 100)
pen.end_fill()

# ---door---
pen.penup()
pen.goto(-30, -100)
pen.pendown()
pen.color("black", "saddlebrown")
pen.begin_fill()
for _ in range(2):
    pen.forward(60)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()

# --- window ---
pen.penup()
pen.goto(-80, 20)
pen.pendown()
pen.color("black", "lightblue")
pen.begin_fill()
for _ in range(4):
    pen.forward(50)
    pen.left(90)
pen.end_fill()

# --- sun ---
pen.penup()
pen.goto(150, 150)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(40)
pen.end_fill()
