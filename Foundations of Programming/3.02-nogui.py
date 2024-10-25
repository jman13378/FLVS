# Jonathan Meyer
# 10/7/2024
# A program to draw a repetitive pattern or outline of a shape using for loops and Turtle Graphics
import turtle

# Create the turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)  # Set the drawing speed

# Set a color for the turtle (not black)
pen.color("blue")

# define function to draw a star
def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)  # Angle for drawing a star

for i in range(50):  # draw 50 stars in a spiral
    draw_star(i * 5)  # Increment star size with each iteration
    pen.right(20)     # Rotate the turtle slightly after each star

