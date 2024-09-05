from random import randrange
import time
import builtins




print ("Type quit at any time to quit the program!")
#3 initialize the items that can be colleted
items = [
    {"name": "rusty sword"},  # add other options
    {"name": "stone"},
    {"name": "wood"},
    {"name": "leaf"},
    {"name": "iron"},
]
#initialize the score and the current items collected
score = 0
itemsCollected = []
# teh base amount of items to collect
itemsCollectCount=3

#min search time in sec
minSearchTime = 3
#max search time in sec
maxSearchTime = 15
def addItem(item):
    global itemsCollected
    itemName = item.get("name")
    itemQuantity = int(item.get("quantity", 0))
    
    # Flag to check if the item was found and updated
    itemFound = False

    # Iterate over the collected items
    for i in range(len(itemsCollected)):
        collected = itemsCollected[i]
        if collected.get("name") == itemName:
            # Update the quantity for the existing item
            currentQuantity = int(collected.get("quantity", 0))
            newQuantity = itemQuantity + currentQuantity
            itemsCollected[i] = {"name": itemName, "quantity": newQuantity}
            itemFound = True
            break

    # If the item was not found in the list, add it as a new item
    if not itemFound:
        itemsCollected.append({"name": itemName, "quantity": itemQuantity})
def input(prompt: object = "",default:str="") -> str:
    input = builtins.input(prompt)
    # if the input is equal to "quit" quit the progam and exit any processes that be linger
    if input.lower().strip() == "quit":
        print("Thank You for playing! Goodbye :)")
        quit()
    input = input.strip().lower()
    # if the input is blank return the default value if there is one
    if (input==""): return default
    return input

# welcome the user 
def printWelcomeMessage():
    time.sleep(1)
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print(f"Your goal is to collect {itemsCollectCount} items before completing the level.")
    time.sleep(1)


def collectItems():
    # allow the inner function to use the outside variables
    global items, itemsCollected, score,itemsCollectCount,minSearchTime,maxSearchTime



    while score < itemsCollectCount:
        print("Searching...")
        # tell teh program to sleep whle it searches for an item
        time.sleep(randrange(minSearchTime,maxSearchTime+1))
        itemToFind = items[randrange(len(items))]
        # ask the user if they want the item
        userInput = input(
            "You have found 1x "
            + itemToFind.get("name")
            + ". Do you want to collect it? (default:y) (y/n): ","yes"
        )
        # if the input equals y or yes make the user pickup the item
        if userInput.lower() == "yes" or "y":
            addItem({"name": itemToFind.get("name"), "quantity": 1})
            score += 1
            print(f"You collected an item! Current score: {score}")
            # if no tell the user they didnt want the item
        elif userInput == "no" or "n":
            print("You chose not to collect the item.")
            # if its an input other than yes y no n then tell tghe user its an invalid input and that they collected the item
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            addItem({"name": itemToFind.get("name"), "quantity": 1})
            score += 1
            print(f"You collected an item! Current score: {score}")
            
    # tell the user the items they have collected
    print("Congratulations! You collected the Following items: ")
    for item in itemsCollected:
        print(str(item.get("quantity")) + "x " + item.get("name"))
    print(f"Your final score is: {score}")


def main():
    global itemsCollectCount
    # print the welcome messages
    printWelcomeMessage()

    while True:
        userInput = input("Do you want to start collecting items? (default:y) (y/n): ","yes")
        if userInput == "yes" or userInput == "y" or userInput == "ye":
            collectItems()
        else:
            print("Thank you for playing! Goodbye.")
            break

        playAgainInput = input("Do you want to play again? (default:y) (y/n): ","yes")

        if playAgainInput != "yes" or not "y":
            print("Thank you for playing! Goodbye.")
            break
        itemsCollectCount=+5


main()
