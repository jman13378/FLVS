import csv
import builtins
# import libraries
# if you want to run teh program in teh FLVS IDLE set to False
debug= False
file_path = "battle_royale.csv"
if debug:
    file_path = "C:/Users/1300286/Desktop/FLVS/Procedural Programming/battle_royale.csv"
# override the default function input
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
    

# function to load the contents of the csv file
def load_csv():
    global file_path
    players_list = []
    # open the csv and read teh data
    with open(file_path,mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            players_list.append(row)
    return players_list
# return the avilable menu options
def get_menu_options():
    return "quit. To quit the program at anytime\n1. Search for a pre-registered player\n"+"2. Find the number of a specific player\n"+"3. Print a list of players and their information"
# search for an available player
def search_player(players_list, player_name):
    for player in players_list:
        if player['Player Name'] == player_name:
            print("\nPlayer found:\n")
            print("--------------------------")
            print(f"Avatar Name: {player['Avatar Name']}")
            print(f"Player Name: {player['Player Name']}")
            print(f"Player Number: {player['Player Number']}")
            print(f"Hometown: {player['Hometown']}")
            print("--------------------------")
            return
    print("Player not found")

def find_player_count(players_list, player_name):
    count = 0
    for player in players_list:
        if player['Player Name'] == player_name:
            count += 1
    print(f"Number of occurrences of {player_name}: {count}")
# print the player list
def print_players(players_list):
    print("List of all players:")
    for player in players_list:
        # print out all player details
        print(f"Avatar Name: {player['Avatar Name']}")
        print(f"Player Name: {player['Player Name']}")
        print(f"Player Number: {player['Player Number']}")
        print(f"Hometown: {player['Hometown']}")
        print()

def main():
    # load the csv
    players_list = load_csv()
    while True:
        # choices 
        choice = input( get_menu_options() + "\nEnter your choice: " )
        if choice == '1':
            player_name = input("Enter the player name to search: ")
            search_player(players_list, player_name)
        elif choice == '2':
            player_name = input("Enter the player name to count: ")
            find_player_count(players_list, player_name)
        elif choice == '3':
            print_players(players_list)
        else:
            print("Invalid choice. Please select again.")

main()
