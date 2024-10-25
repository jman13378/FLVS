import csv
import builtins
hasRan=False
debug =False
file_name = "sun_data.csv"
# if the program is in debug mode use my location path
if debug:
    file_name = "C:/Users/1300286/Desktop/FLVS/Procedural Programming/sun_data.csv"
# override the default input to include a default and a quit message
def input(prompt:object="",default=""):
    input = builtins.input(prompt).strip().lower()
    # if the input equals quit quit the program
    if (input == "quit"):
        print("Thank you for your time! Goodbye :)")
        quit()
    if (input==""):
        return default
    return input
def find_sunrise_time(search_time):
    found = False
    global file_name

    # Open the CSV file and read the contents
    with open(file_name) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        
        # Iterate through each row in the CSV file
        for row in csv_reader:
            date, sunrise_time, location = row
            
            # Check if the current row's sunrise time matches the search time
            if sunrise_time == search_time:
                found = True
                print(f"Sunrise time {search_time} found on {date} at {location}.")
                break
    
    # If the sunrise time was not found
    if not found:
        print(f'Sunrise time "{search_time}" not found in the dataset.\n\n')
    
    return found

def main():
    global hasRan

    
    # Ask for user input
    search_time = input("Please enter the sunrise time you are looking for (e.g., 06:45): ", "")

    # Find the sunrise time in the CSV file

    
    found = find_sunrise_time(search_time)
    
    # Additional user input if the sunrise time was found
    if found:
        schedule_choice = input("Would you like to schedule the race for this time? (yes/no): ","yes")
        if schedule_choice == 'yes':
            hasRan=True
            
            print(f"Race scheduled for {search_time}.")
        else:
            print("Race not scheduled. Please choose another time.")
    
    print("Thank you for using the Sunrise Beach 5K Race Scheduler. Have a great day!")

print("\nType quit to quit the program.\n")
# welcome the user
print("Welcome to the Sunrise Beach 5K Race Scheduler!")
print("We need to find a weekend date with a sunrise at 6:45 a.m. for the perfect race experience.")
# Run the main function unless hasRan = True
while not hasRan:
    
    main()