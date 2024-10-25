import turtle


# Create a turtle object
pen = turtle.Turtle()
pen.speed(3)

# Function to draw a square (used for walls, windows)
def draw_square(t, side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()

# Function to draw a triangle (used for roof)
def draw_triangle(t, side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()

# Function to draw the house body
def draw_house():
    pen.penup()
    pen.goto(-50, 50)
    pen.pendown()
    draw_square(pen, 100, "lightgrey")  # House walls

# Function to draw the roof
def draw_roof():
    pen.penup()
    pen.goto(-60, 50)
    pen.pendown()
    draw_triangle(pen, 120, "brown")  # Roof

# Function to draw a sun (circle shape)
def draw_sun():
    pen.penup()
    pen.goto(80, 150)
    pen.pendown()
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()

# Function to draw the window
def draw_window():
    pen.penup()
    pen.goto(-30, 15)
    pen.pendown()
    draw_square(pen, 30, "white")  # Window
    pen.penup()
    pen.goto(0,0)
    pen.pendown()
    pen.goto(-30,0)
    pen.penup()
    pen.goto(-15,15)
    pen.pendown()
    pen.goto(-15,-15)

# Drawing the picture
print("Drawing: Sunny House")
draw_house()
draw_roof()
draw_window()
draw_sun()

# Hide the turtle after drawing
pen.hideturtle()

