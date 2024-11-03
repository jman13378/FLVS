def convert_inches_to_centimeters(inches):
    return inches * 2.54

def convert_centimeters_to_inches(cm):
    return cm / 2.54

def calculate_area(length, width):
    return length * width

def main():
    # Test values for conversion
    test_values_in_inches = [10, -5, 0]
    test_values_in_cm = [25.4, 0, -10]
    
    # Test values for area calculation
    length_width_pairs = [(5, 10), (-3, 4), (0, 5)]

    # Convert inches to centimeters
    print("Inches to Centimeters Conversion:")
    for inch in test_values_in_inches:
        cm = convert_inches_to_centimeters(inch)
        print(str(inch) + " inches is " + str(cm) + " centimeters")

    # Convert centimeters to inches
    print("\nCentimeters to Inches Conversion:")
    for cm_value in test_values_in_cm:
        inches = convert_centimeters_to_inches(cm_value)
        print(str(cm_value) + " cm is " + str(inches) + " inches")

    # Calculate area of rectangles
    print("\nArea Calculations:")
    for length, width in length_width_pairs:
        area = calculate_area(length, width)
        print("Area of rectangle with length " + str(length) + " and width " + str(width) + " is " + str(area))

main()
