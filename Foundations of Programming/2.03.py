# Jonathan Meyer
# 9/27/24
# Write an interactive program to calculate the volume and surface area of a three-dimensional object.
import builtins
# initialize constant variables
PI = 3.14
def input(prompt:str="",default=""):
    input = builtins.input(prompt).strip().lower()
    # if the input equals quit quit the program
    if (input == "quit"):
        print("Thank you for your time! Goodbye :)")
        quit()
    # if input is blank return the default value
    if (input==""):
        return default
    return input
def main():
    # Print the problem description
    print("You are designing a cylindrical water tank.")
    print("Calculate the volume and surface area of the tank.")
    print("Type quit to quit the program.")
    # ask the user for the height and radius while respecting the units
    radius = float(input("Enter the radius of the cylinder (in meters): ").replace("m",""))
    height = float(input("Enter the height of the cylinder (in meters): ").replace("m",""))

    # Calculations
    volume = PI * radius**2 * height
    surface_area = 2 * PI * radius**2 + 2 * PI * radius * height

    # Output results
    print(f"The volume of the cylinder is: {volume:.2f} cubic meters.")
    print(f"The surface area of the cylinder is: {surface_area:.2f} square meters.")

# Call the function to execute
main()
