#Jonathan Meyer
#10/24/24
# Aprogram to get the price of a set of food along with a tip amount subtotal and with tax rate

# Get user input for the prices of the items
appetizer_price = float(input("Enter the price of the appetizer: "))
entree_price = float(input("Enter the price of the entrée: "))
drink_price = float(input("Enter the price of the drink: "))
dessert_price = float(input("Enter the price of the dessert: "))

# Calculate the subtotal
subtotal = appetizer_price + entree_price + drink_price + dessert_price

# Calculate the tax and tip
tax = subtotal * 0.065  # 6.5% tax
tip = subtotal * 0.20   # 20% tip

# Calculate the total cost
total = subtotal + tax + tip

# Output the results
print("\n---- Receipt ----")
print(f"Appetizer: ${appetizer_price:.2f}")
print(f"Entrée: ${entree_price:.2f}")
print(f"Drink: ${drink_price:.2f}")
print(f"Dessert: ${dessert_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (6.5%): ${tax:.2f}")
print(f"Tip (20%): ${tip:.2f}")
print(f"Total: ${total:.2f}")
