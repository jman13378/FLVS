# Function to take pizza order from the user
def take_pizza_order():
   # Input: Ask user for pizza size
   size = input("What size pizza would you like (small, medium, or large)? ").strip().lower()
   
   # Input: Ask user for type of crust
   crust = input("What type of crust would you like? ").strip()
   
   # Input: Ask user for type of cheese
   cheese = input("What kind of cheese would you like? ").strip()
   
   # Input: Ask user for topping
   topping = input("What topping would you like? ").strip()
   
   # Output: Display the user's pizza order
   print("\nYour pizza order:")
   print("Size: "+size.capitalize())
   print("Crust: "+crust.capitalize())
   print("Cheese: "+cheese.capitalize())
   print("Topping: "+topping.capitalize())

# Call the function to take the order
take_pizza_order()

