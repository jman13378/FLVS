import turtle

# Set up the screen and turtle
wn = turtle.Screen()
wn.title("Turtle Movement Program")
wn.bgcolor("lightblue")  # Set background color

t = turtle.Turtle()
t.color("green")  # Set turtle color
t.shape("turtle")

# Function to display the menu
def display_menu():
    print("\nTurtle Movement Menu:")
    print("1: Move Forward")
    print("2: Move Backward")
    print("3: Turn Left")
    print("4: Turn Right")
    print("5: Draw a Square")
    print("Q: Quit")

# Function to draw a square
def draw_square():
    for _ in range(4):
        t.forward(50)
        t.right(90)

# Main program loop
while True:
    display_menu()  # Show the menu
    choice = input("Enter your choice: ").strip().upper()
    if choice == '1':
        t.forward(50)
    elif choice == '2':
        t.backward(50)
    elif choice == '3':
        t.left(45)  # Rotate left by 45 degrees
    elif choice == '4':
        t.right(45)  # Rotate right by 45 degrees
    elif choice == '5':
        draw_square()
    elif choice == 'Q':
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and program
    else:
        print("Invalid choice! Please try again.")

# Close the turtle graphics window when finished
wn.bye()
