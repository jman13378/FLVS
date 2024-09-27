# Jonathan Meyer
# 9/25/24
# a program to introduce the user to the program
#initialize animals
animals = ["zebra","zebu","zonkey","zebra shark","zebra spider","zorse","zokor","zorro","zorilla","zuchon","zebra moray eel", "zapata wren","zapata","zebra moray", "zanzaibar","zabra duiker"]
def main():
    global animals
    print("Hi im your new virtural friend! You can call me Juice.")
    name = input("What is your name?: ")
    if (len(name)<=1):
        print("Thats Cool")
    else:
        print("Thats Cool, The second letter of your name is " + name[2])
    while True:
        animal = input("Name an animal that starts with the letter 'z': ").strip().lower()

        if (animal[0]=="z" and animal in animals):
            print("Good Job! " + animal + " does start with the letter 'z'")
            break
        else:
            print("Not quite, Try again!")
    print("It was nice chatting with you " +name+". Have a good day!")
main()