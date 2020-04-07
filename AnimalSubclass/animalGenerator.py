from Animal import Animal
from Animal import Mammal
from Animal import Bird

def main():

    print("Welcome to the Animal Generator!")
    print("This program creates Animal Objects\n")

    zoo = []
    loop = 'y'
    

    while(loop == 'y'):

        print("would you like to create a Mammal or Bird")
        print("1. Mammal")
        print("2. Bird")
        create = int(input("Which would you like to create? "))

        if(create == 1):
            while(True):
                try:
                    mammalType = input('What type of mammal would you like to create? ')
                    if (mammalType.isdigit()):
                        print('The type cannot be a number.')
                        continue
                except:
                    print('Please enter a string.')
                    continue
                else:
                    break

            while(True):
                try:
                    name = input("What is the mammal's name? ")
                    if (name.isdigit()):
                        print('The name cannot be a number.')
                        continue
                except:
                    print('Please enter a string')
                    continue
                else:
                    break
            
            while(True):
                try:
                    hairColor = input("What color is the mammal's hair? ")
                    if (hairColor.isdigit()):
                        print('The name cannot be a number.')
                        continue
                except:
                    print('Please enter a string')
                    continue
                else:
                    break
            newMammal = Mammal(mammalType, name, hairColor)
            zoo.append(newMammal)

        if(create == 2):
            while(True):
                try:
                    birdType = input('What type of bird would you like to create? ')
                    if (birdType.isdigit()):
                        print('The type cannot be a number.')
                        continue
                except:
                    print('Please enter a string.')
                    continue
                else:
                    break

            while(True):
                try:
                    name = input("What is the brid's name? ")
                    if (name.isdigit()):
                        print('The name cannot be a number.')
                        continue
                except:
                    print('Please enter a string')
                    continue
                else:
                    break
            
            while(True):
                try:
                    canFly = input("Can the bird fly? ")
                    if (canFly.isdigit()):
                        print('The name cannot be a number.')
                        continue
                except:
                    print('Please enter a string')
                    continue
                else:
                    break
            newBird = Bird(birdType, name, canFly)
            zoo.append(newBird)

        loop = input("\nWould you like to evaluate another file? (y/n) ")

    print("\nAnimal List:")
    for animal in zoo:
        print(animal.get_name() + " the " + animal.get_animal_type() + " is " + animal.check_mood())

if __name__ == "__main__":
    main()