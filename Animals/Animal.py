import Lib/random.py

class Animal:
    
    def __init__(self, type, name):
        self.__animal_type = type
        self.__name = name
        choose_mood = random.randint(1,3)
        if choose_mood is 1:
            self.__mood = "happy"
        if choose_mood is 2:
            self.__mood = "hungry"
        if choose_mood is 3:
            self.__mood = "sleepy"

    def get_animal_type():
        return __animal_type

    def get_name():
        return __name

    def check_mood():
        return __mood
    