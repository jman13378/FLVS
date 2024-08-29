# Jonathan Meyer
# 8/23/24

hasRan = False
# how many items to show that the user can buy
productListLimit = 2
# the products that the store sells 
products = [
    {"price":11.99, "itemName":"Product1"},
    {"price":100, "itemName":"Product2"},
    {"price":7.00, "itemName":"Product3"},
    {"price":50, "itemName":"Product4"},
    {"price":70, "itemName":"Product5"},
    {"price":19, "itemName":"Product6"},
    {"price":200, "itemName":"Product7"}
]
# sort the list based on the price fom high to low
products = sorted(products, key=lambda x: 200-x["price"])
# a functio nto show the user x(amountToShow) products based on y(amount_spent)
def showProducts(amount_spent,amountToShow):
    productLimit =0

    for product in products:
        if (productLimit==amountToShow): return
        price = product.get("price")
        if (price<=amount_spent):
            productLimit+=1
            print("You can afford " + str(product.get("itemName")) + " for $" + str(price))
        else:
            continue
        # check if the user inputted teh word "quit"
def checkIfQuit(input):
    global hasRan
    if (input == "quit"):
        hasRan=True
        return True
    return False

# main function
def main():
    global hasRan
    #spacer
    print("")
    # Print a description of the online store
    print("Welcome to our online store! Recieve a free gift for qualifying purchases over $200 or more")
    try:
    # try to Obtain user input except if the value is a non-positive float or isnt a float
        amount_spent =  input("How much money would you like to spend today?: ")
        # @see {checkIfQuit}
        if (checkIfQuit(amount_spent)): return

        amount_spent = float(amount_spent)
        #check if the input is a non positive number
        if (amount_spent<1):
            print("Invalid Input. Value must be a positive input!")
            return
        productsToSee = input(f"How many products would you like to see? Default ({productListLimit}): ")
        # @see {checkIfQuit}
        if (checkIfQuit(productsToSee)): return

        if (productsToSee=="" or productsToSee==" " or productsToSee==None): productsToSee=productListLimit 
        else: productsToSee=int(productsToSee)
    except ValueError:
        print("Invalid Input. Value must be a Number!")
        return
    # tell the program that all of the inputs are valid and to kill the program after this current run
    hasRan=True
    # print a list of products the user can buy based on the productListLimit(How many can be listed)
    showProducts(amount_spent,productsToSee)
    seeMore = input("Want to see more? Default(n) (y/n):")
    if (checkIfQuit(seeMore)): return
    if (seeMore=="y" or seeMore=="yes" or seeMore=="ye"): showProducts(amount_spent,productsToSee*2)

    # Recommend a product based on the amount spent
    if amount_spent >= 100 and amount_spent < 200:
        print("We recommend our best-selling items within your budget.")
    elif amount_spent >= 200:
        print("Congratulations! You qualify for a free gift with your purchase.")
    else:
        # Calculate how much more is needed
        print(f"You need to spend an additional ${200 - amount_spent:.2f} to receive a free gift.")


print("Type 'quit' at anytime to quit the program")
# run the program till the user how fully inputted all values correctly
while (not hasRan):
    # run teh main function
    main()
# thank the user for shopping
print("Thank you for shopping with us today!")