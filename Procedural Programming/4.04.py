import csv
debug =True
file_name = "sun_data.csv"
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
        print(f"Sunrise time {search_time} not found in the dataset.")
    
    return found

def main():
    print("Welcome to the Sunrise Beach 5K Race Scheduler!")
    print("We need to find a weekend date with a sunrise at 6:45 a.m. for the perfect race experience.")
    
    # Ask for user input
    search_time = input("Please enter the sunrise time you are looking for (e.g., 06:45): ").strip()
    
    # Find the sunrise time in the CSV file

    
    found = find_sunrise_time(search_time)
    
    # Additional user input if the sunrise time was found
    if found:
        schedule_choice = input("Would you like to schedule the race for this time? (yes/no): ").strip().lower()
        if schedule_choice == 'yes':
            print("Race scheduled for sunrise time.")
        else:
            print("Race not scheduled. Please choose another time.")
    
    print("Thank you for using the Sunrise Beach 5K Race Scheduler. Have a great day!")

# Run the main function
main()
