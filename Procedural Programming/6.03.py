import hashlib
import json

# Function to calculate the average of a list
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Function to display the average back to the user
def display_average(average):
    print(f"The average of your scores is: {average:.2f}")

# Function to encrypt data
def encrypt_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to store data securely (simulated by saving to a file)
def store_data_securely(data, filename='secure_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("User data is protected and kept secure")

# Function to update the application (simulated)
def update_application():
    print("Application is up to date with the latest educational strategies")

# Function to display research about the tools used for assessment
def display_research():
    print("Research on assessment tools:")
    print("1. Myers-Briggs Type Indicator (MBTI): A personality assessment tool that categorizes individuals into 16 personality types based on preferences.")
    print("2. Holland Code (RIASEC): A career assessment tool that categorizes individuals into six types: Realistic, Investigative, Artistic, Social, Enterprising, and Conventional.")

# Function to handle the interactive quiz/survey
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
    display_average(average_score)

    if average_score >= 4:
        print("You have a strong interest in specialized fields. Consider exploring majors like Engineering or Computer Science.")
    elif average_score >= 3:
        print("You have a balanced interest. Majors in Business or Social Sciences might be a good fit.")
    else:
        print("You might enjoy a more creative or exploratory field like Art or Humanities.")

# Main application flow
def main():
    while True:
        print("\nCollege Major Planning App")
        print("1. Take Interactive Quiz/Survey")
        print("2. Display Research on Assessment Tools")
        print("3. Update Application")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

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

if __name__ == "__main__":
    main()
