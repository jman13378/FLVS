import random

def print_welcome_message():
    print("Welcome to the Adventure Game!")
    print("Your goal is to collect three items before completing the level.")

def collect_items():
    score = 0
    items_collected = 0
    
    while items_collected < 3:
        user_input = input("You find an item. Do you want to collect it? (y/n): ").strip().lower()
        
        if user_input == "yes" or "y":
            items_collected += 1
            score += 1
            print(f"You collected an item! Current score: {score}")
        elif user_input == "no" or "n":
            print("You chose not to collect the item.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    print("Congratulations! You collected all three items.")
    print(f"Your final score is: {score}")

def main():
    print_welcome_message()
    
    while True:
        user_input = input("Do you want to start collecting items? (y/n): ").strip().lower()
        
        if user_input != "yes" or not "y":
            print("Thank you for playing! Goodbye.")
            break
        
        collect_items()
        
        play_again_input = input("Do you want to play again? (y/n): ").strip().lower()
        
        if play_again_input != "yes" or not "y":
            print("Thank you for playing! Goodbye.")
            break


main()
