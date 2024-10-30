
def main():
    # Step 1: Define the category and list of favorite books
    category = "Favorite Books"
    favorite_books = ["1984", "To Kill a Mockingbird", "The Great Gatsby", "Pride and Prejudice", "Moby-Dick"]
    # Step 2: Ask for user input
    
    user_favorite = input("What is your favorite book? ")
    # Step 3: Output the list of favorite books
    print(f"Category: {category}")
    print("Here are my favorite books:")
    for index, book in enumerate(favorite_books, start=1):
        print(f"{index}. {book}")



    # Step 4: Check if the user's favorite is on the list
    if user_favorite in favorite_books:
        print(f"Great choice! {user_favorite} is also on my list.")
    else:
        print(f"Nice choice, but '{user_favorite}' is not on my list.")
main()