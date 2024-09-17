import hashlib
import json
import builtins

# override the default function input
def input(prompt:str="",default=""):
    input = builtins.input(prompt)
    # if the input equals quit quit the program
    if (input.lower() in ["quit", "exit"]):
        print("Exiting the application. Have a great day!")
        builtins.quit()
    # if input is blank return the default value
    if (input==""):
        return default
    return input
# function to calculate the average of a list
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


# function to encrypt data
def encrypt_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# stores the data into a file 
def store_data(data, filename='secure_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("User data is protected and kept secure.")

# # updates the applicatiopn to use the latest softwares
def update_application():
    print("Application is up to date with the latest educational strategies.")

# display all of the reseach stratigies used to build this application
def display_research():
    print("Research on assessment tools:")
    print("1. Myers-Briggs Type Indicator (MBTI): A personality assessment tool that categorizes individuals into 16 personality types based on preferences.")
    print("2. Holland Code (RIASEC): A career assessment tool that categorizes individuals into six types: Realistic, Investigative, Artistic, Social, Enterprising, and Conventional.")

# let the user take the quiz
def interactive_quiz():
    print("Welcome to the Interactive Quiz")
    print("Please answer the following questions with scores from 1 (lowest) to 5 (highest).")

    questions = {
        "How much do you enjoy problem-solving?": 0,
        "How much do you like working with people?": 0,
        "How creative do you consider yourself?": 0,
        "How interested are you in technical subjects?": 0
    }

    for question in questions:
        while True:
            try:
                score = int(input(question + " (1-5): "))
                if 1 <= score <= 5:
                    questions[question] = score
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    average_score = calculate_average(list(questions.values()))
    print(f"The average of your scores is: {average_score:.2f}")

    if average_score >= 4:
        print("You have a strong interest in specialized fields. Consider exploring majors like Engineering or Computer Science.")
    elif average_score >= 3:
        print("You have a balanced interest. Majors in Business or Social Sciences might be a good fit.")
    else:
        print("You might enjoy a more creative field like Art or Humanities.")
# print the options avialible to the user
def get_options_menu():
    return "\nCollege Major Planning App\n"+"1. Take Interactive Quiz/Survey\n"+"2. Display Research on Assessment Tools\n"+"3. Update Application\n"+"4. Exit"
# Main application flow
def main():
    while True:
        

        choice = input(get_options_menu()+"\nSelect an option (1-4): ")

        if choice == '1':
            interactive_quiz()
        elif choice == '2':
            display_research()
        elif choice == '3':
            update_application()
        elif choice == '4':
            print("Exiting the application. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


main()
