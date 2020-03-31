import random

class Animal(object):
    
    def __init__(self, animaltype, name):
        self.__animal_type = animaltype
        self.__name = name
        choose_mood = random.randint(1,3)
        if choose_mood == 1:
            self.__mood = "happy"
        if choose_mood == 2:
            self.__mood = "hungry"
        if choose_mood == 3:
            self.__mood = "sleepy"

    def get_animal_type(self):
        return self.__animal_type

    def get_name(self):
        return self.__name

    def check_mood(self):
        return self.__mood

class Mammal(Animal):
    def __init__(self, mammaltype, name, haircolor):
        self.__hair_color = haircolor
        Animal.__init__(self, mammaltype, name)

    def get_hair_color(self):
        return self.__hair_color

class Bird(Animal):
    def __init__(self, birdtype, name, canfly):
        self.__can_fly =  canfly
        Animal.__init__(self, birdtype, name)

    def get_can_fly(self):
        return self.__can_fly