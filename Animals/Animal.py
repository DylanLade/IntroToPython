import random

class Animal:
    
    def __init__(self, type, name):
        self.__animal_type = type
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
    