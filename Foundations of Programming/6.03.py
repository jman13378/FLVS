# Jonathan Meyer
# 11.2.2024
# a program to play rock, paper, scissors
import random

def main():
    # Display the rules
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    
    # List of possible moves
    moves = ["rock", "paper", "scissors", "1", "2", "3"]
    while input("Play a round? (y/n): ").lower() == "y":
        play_round(moves)
    print("Thank you for playing!")

def play_round(moves):
    # Ask for user's choice
    user_choice = get_user_choice(moves)
    
    # Generate computer's choice
    computer_choice = random.choice(moves)
    
    # Display both choices
    print("You chose: " + (moves[int(user_choice)-1] if user_choice.isdigit() else user_choice))
    print("Computer chose: " + computer_choice)
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

def get_user_choice(moves):
    # Prompt the user to choose
    while True:
        user_input = input("Enter your choice (rock:1, paper:2, scissors:3): ").lower()
        if user_input in moves:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif ((user == "rock" or user == "1") and computer == "scissors") or \
         ((user == "scissors" or user == "2") and computer == "paper") or \
         ((user == "paper" or user == "3") and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Entry point
main()
