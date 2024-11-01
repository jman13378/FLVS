def main():
    # Welcome message
    print("Welcome to the Eco-Friendly Online Store!")
    
    # Input statements
    age = int(input("Please enter your age: "))  # Input age
    product_type = input("Please enter the product type (e.g., sustainable): ")  # Input product type
    community_involvement = input("Have you participated in a community clean-up event in the last 6 months? (yes/no): ")  # Input involvement

    # Assume a predefined total purchase amount
    total_purchase_amount = float(input("Enter your total purchase amount: $"))  # Input total purchase amount

    # Initialize discount variables
    discount_amount = 0
    discount_message = ""

    # Decision statements
    if age < 25:
        discount_amount += 10
        discount_message += "You receive a $10 discount for being under 25.\n"
    
    if product_type.lower() == "sustainable":
        discount = 0.15 * total_purchase_amount
        discount_amount += discount
        discount_message += "You receive a 15% discount of $" + str(round(discount, 2)) + " for purchasing sustainable products.\n"
    
    if community_involvement.lower() == "yes":
        discount_amount += 5
        discount_message += "You receive a $5 discount for participating in community clean-up events.\n"

    # Calculate final amount
    final_amount = total_purchase_amount - discount_amount

    # Output statements
    print("\nThank you for your purchase!")
    print("Your total purchase amount is: $" + str(round(total_purchase_amount, 2)))
    print(discount_message)
    print("Your total discount is: $" + str(round(discount_amount, 2)))
    print("Your final amount after discount is: $" + str(round(final_amount, 2)))

# Run the discount program
main()
