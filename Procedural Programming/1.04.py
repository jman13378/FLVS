#Jonathan Meyer
#8/21/24

import datetime 




ran = False

def main():
    # if the age is not a number print and rerun the function
    try:
        # get the users age
        age = int(input("How old are you: "))
        # if age is 0 or under then tell the user their age is invalid
        if (age<=0): 
            print("Invalid age")
            return
        fact = input("What is something you know about voting?: ")
        # tell the user that that fact is nice
        print("Thats a nice Fact")
        # tell the program that the program successfully got all its info
        ran=True
        # tell the users their current age and how many years till they can vote
        print("You are currently " + str(age) + " Years old! You can register to vote in " + str((18-age)) +" Years!")
    # error out if inputted age is not a number
    except ValueError:
        print("Invalid value entered.")
        return

while (not ran):
    main()