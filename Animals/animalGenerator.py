from Animal import Animal

def main():

    print("Welcome to the Animal Generator!")
    print("This program creates Animal Objects\n")

    zoo = []
    loop = 'y'

    while(loop == 'y'):
        while(True):
            try:
                animalType = input('What type of animal would you like to create? ')
                if (animalType.isdigit()):
                    print('The type cannot be a number.')
                    continue
            except:
                print('Please enter a string.')
                continue
            else:
                break

        while(True):
            try:
                name = input("What is the animal's name? ")
                if (name.isdigit()):
                    print('The name cannot be a number.')
                    continue
            except:
                print('Please enter a string')
                continue
            else:
                break
            
        zoo.append(Animal(animalType, name))    

        loop = input("\nWould you like to evaluate another file? (y/n) ")

    print("\nAnimal List:")
    for animal in zoo:
        print(animal.get_name() + " the " + animal.get_animal_type() + " is " + animal.check_mood())

if __name__ == "__main__":
    main()