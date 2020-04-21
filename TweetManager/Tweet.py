import time
import math

class Tweet:

    def __init__(self, author, text, age):
        self.__author = author
        self.__text = text
        if age is 0:
            self.__age = time.time()
        else:
            self.__age = float(age)

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        return self.__age

