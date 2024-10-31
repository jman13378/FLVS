#Jonathan Meyer
# 10/30/24
# a program to encode and decode a message
def main():
    # Step 2: Define a secret message
    message = "toes"
    
    # Step 3: Initialize an empty string for the encoded message
    encoded_message = ""
    
    # Step 4: Loop through each character in the message
    for character in message:
        # Add 2 to the ASCII value of the character
        encoded_character = chr(ord(character) + 2)
        # Append the new character to the encoded message
        encoded_message += encoded_character
    
    # Step 5: Display the encoded message in binary
    print("Encoded message (binary representation):")
    for character in encoded_message:
        # Convert to binary and slice '0b' prefix
        binary_representation = bin(ord(character))[2:]  # Remove '0b' prefix
        print(binary_representation.zfill(8), end=' ')  # Pad with zeros to ensure 8 bits
    print("\n")
    
    # Step 6: Prompt user to guess the message
    user_guess = input("Guess the secret message: ")
    
    # Step 7: Check the user's guess
    if user_guess == message:
        print("Correct!")
    else:
        print("Try again!")
    
    # Step 9: Initialize an empty string for the decoded message
    decoded_message = ""
    
    # Step 10: Loop through each character in the encoded message
    for character in encoded_message:
        # Subtract 2 from the ASCII value of the character
        decoded_character = chr(ord(character) - 2)
        # Append the new character to the decoded message
        decoded_message += decoded_character
    
    # Step 11: Display the decoded message
    print("\nDecoded message:")
    print(decoded_message)

main()
