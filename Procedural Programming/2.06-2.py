# Jonathan Meyer
# 8/28/24
import builtins
# tell the while loop that the main function hasnt been ran
hasRan = False
# initialize all of the outfits that may be recommended to the user
outfits = [
    {
        "season": "spring",
        "options": [
            {
                "name": "beach",
                "recommendation": "[color] Light jacket, [color] T-shirt, [color] shorts, and [color] sunglasses.",
            },
            {
                "name": "mountain",
                "recommendation": "[color] Light sweater, [color] hiking pants, and [color] comfortable shoes.",
            },
            {
                "name": "other",
                "recommendation": "[color] Casual spring attire with a [color] light jacket.",
            },
        ],
    },
    {
        "season": "summer",
        "options": [
            {
                "name": "beach",
                "recommendation": "[color] Swimsuit, [color] beachwear, and a [color] hat.",
            },
            {
                "name": "mountain",
                "recommendation": "[color] Lightweight and breathable clothing, [color] hiking boots.",
            },
            {
                "name": "other",
                "recommendation": "[color] Light and cool summer clothing suitable for the weather.",
            },
        ],
    },
    {
        "season": "fall",
        "options": [
            {
                "name": "beach",
                "recommendation": "[color] Long sleeve shirt, [color] light sweater, and [color] jeans.",
            },
            {
                "name": "mountain",
                "recommendation": "[color] Warm layers, [color] insulated jacket, and sturdy boots.",
            },
            {
                "name": "other",
                "recommendation": "[color] Fall attire, [color] layering options, and [color] comfortable shoes.",
            },
        ],
    },
    {
        "season": "winter",
        "options": [
            {
                "name": "beach",
                "recommendation": "[color] Light jacket, [color] warm layers for evening, and comfortable shoes.",
            },
            {
                "name": "mountain",
                "recommendation": "[color] Heavy winter coat, [color] thermal wear, and snow boots.",
            },
            {
                "name": "other",
                "recommendation": "[color] Warm winter clothing suitable for the climate.",
            },
        ],
    },
]
# welcome the user
print("Welcome to the Vacation Attire Selector!")
print("We will help you choose the perfect outfit for your vacation.")
print("Please answer the following questions to get your recommendation.")
# create a function that will quit the program if the user inputs the word `quit`
def input(prompt:object = "")-> str:
    global hasRan
    # use builtin methods instead of recursivly calling this function
    input = builtins.input(prompt)
    if (input.lower()=="quit"):
        hasRan=True
        # tell the user goodbye
        builtins.print("Goodbye :)!")
        quit()
         
    return input
def main():
    global hasRan
    try:
        name = str(input("What may we call you?: "))
        #ask the user where their destination will be
        destination = input("Where would you like to go?: ")
        if (destination== " " or destination== "" or destination== None):
            # if destination is null print 
            print("Invalid Input. Please Try Again")
            return
        # ask the user their fav color
        color = input("What is your Favorite Color?: ")
        season = input("What season would you like to travel in?: ")
    except ValueError: 
        #tell the user they have an invalid input
        print("Invalid Input. Please Try Again")
        return
    # tell the user to wait for their recommendation
    print("Thank you for providing the information. Based on your inputs, we will recommend an outfit.")
    for outfit in outfits:
        if (season.lower()==outfit.get("season")):
            global other
            other = ""

            for option in outfit.get("options"):
                # initialize the other outfit
                if (option.get("name")=="other"):
                    other = option.get("recommendation")
                # if the destination matched that of the database then print the recommendation
                if (option.get("name")==destination.lower()):
                    print(f"\n {name} Your Recommended Option is: " + option.get("recommendation").replace("[color]", color))
                    hasRan=True
                    return
            # if the destination downs exist in the database reccomend the other option
            if (other != ""):
                print ("\nRecommended Option: " + other)
            elif (other ==""):
                # tell the user their outfit isnt in teh database
                print("Sorry we cannot recommend an option for you at this time :(")
            else:
                # tell the user an error occurred
                print("An Error has occurred")
            hasRan=True
            return
            
            
            
            
            
            
    return

print("\nType Quit to quit the program at any time!\n")
while not hasRan: 
    main()
# tell the user thank you after successfully completing
print("\nThank you for using the Vacation Attire Selector. Have a great trip!")
