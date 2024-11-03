# Jonathan Meyer
# 11.2.2024
# a program to define a Superhero class, set attributes and call the methods to save the world.

# Implementation in Python:
class Superhero:
    # Superhero class represents the facts related to a superhero.

    def __init__(self, name="", strengthPts=0, motto="", villain=""):
        # Create a new Superhero with a name and other attributes.
        self.name = name
        self.strengthPts = strengthPts
        self.motto = motto
        self.villain = villain

    def addStrengthPts(self, points):
        # Adds points to the superhero's strength.
        self.strengthPts = self.strengthPts + points

    def saveWorld(self):
        # If strength points are greater than a threshold, the superhero saves the world.
        if self.strengthPts >= 50:
            print(self.name + " has successfully saved the world from " + self.villain + "! Motto: \"" + self.motto + "\"")
        else:
            print(self.name + " needs more strength to defeat " + self.villain + " and save the world.")

# Main function to create and use the Superhero class
def main():
    # Creating an instance of Superhero
    my_hero = Superhero(name="Captain Valor", strengthPts=30, motto="Justice Always Prevails!", villain="Dr. Chaos")

    # Describe the hero
    print("Introducing our hero: " + my_hero.name + ". They stand for: \"" + my_hero.motto + "\".")
    print("Their current strength points: " + str(my_hero.strengthPts) + ".")
    print("Their arch-nemesis is: " + my_hero.villain + ".")

    # Add strength points
    print("\nCaptain Valor is training to increase their strength...")
    my_hero.addStrengthPts(25)
    print("Captain Valor's updated strength points: " + str(my_hero.strengthPts) + ".")

    # Hero tries to save the world
    print("\nThe world is in danger!")
    my_hero.saveWorld()

# Calling the main function
main()
