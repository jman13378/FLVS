# Jonathan Meyer
# 10/7/24
# An interactive program to calculate the volume and surface area of a three-dimensional object.
import math
# initialize constant variables

def main():
    # print the problem description
    print("You are designing a cylindrical water tank.")
    print("Calculate the volume and surface area of the tank.")
    print("Type quit to quit the program.")
    # ask the user for the height and radius while respecting the units
    radius = float(input("Enter the radius of the cylinder (in meters): ").replace("m",""))
    height = float(input("Enter the height of the cylinder (in meters): ").replace("m",""))

    # Calculations
    volume = math.pi * radius**2 * height
    surface_area = 2 * math.pi * radius**2 + 2 * math.pi * radius * height

    # Output results
    print(f"The volume of the cylinder is: {volume:.2f} cubic meters.")
    print(f"The surface area of the cylinder is: {surface_area:.2f} square meters.")

# Call the function to execute
main()
