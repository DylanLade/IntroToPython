
# Python Interview Questions

## Dylan Lade dclqn8

# 1. What is Python?
Python is a high-level programming language with built in high-level data structures. Python also has support for Object Oriented programming and scripting.

# 2. What is a variable?
A variable is a portion of allocated memory that can be accessed and altered by a program.

# 3. What is a namespace?
A namespace is a set of symbols used to organize objects to be referred to by a name. Helping all identifiers within the namespace have unique names so they can be easily identified.

# 4. What is the difference between list and tuple?
A list is a dynamic collection of one type similar to arrays of other languages. While a tuple is an unchangeable collection of many different types.

# 5. How you can convert a number to a string?

Pass the variable containing the number throught the str() funtion

# 6. What are the rules for local and global variables?
Global variables are formed outside any functions and can be use across many, while local variables are formed inside functions and can only be used while inside the function.

# 7. Explain how to generate random numbers.
After imorting the random library you can use one of the many functions to generate different type of numbers.

# 8. What is a dictionary?
A dictionary is a data type build off of key : value pairs. This can be used to assosiate data of one type with data of another.

# 9. What is the self keyword?
The self keyword refers to the current working object. When working in a class the self keyword will call that instance of the class.

# 10. What are loop interruption statements?
These are the conditions of the loop, they can pass the loop onto the next iteration or they can end the loop.

# 11. Explain List, Tuple, Set, and Dictionary and provide at least one instance where each of these collection types can be used.
List: Dynamic list of a single type EX. ToDo list
Tuple: Fixed set of varrying types EX. Employee Information (Name, Contact number, Employee ID)
Set: Dynamic Unordered collection of a single data type EX. Grocery List
Dictionary: Dynamic Collection with key : value pairs EX. Product Info (Model, Type, color)

# 12. How is Exception Handling done?
Exception handling is done through try except statements, you can customize what exceptions are caught or you can have it catch all.

# 13. What does ‘#’ symbol do?
The # symbol allows for comments to be added into the program.

# 14. Write the command to get all keys from a dictionary.
dictionary.keys() will return all of the keys

# 15. What is range()? Give an example to explain it.
The range function returns a sequence of numbers based off of the given value. range(4) will return {0,1,2,3}

# 16. What does the // arithmetic operator do?
This operator performs floor division x // y will divide x by y and rounf the result down to the nearest whole number.

# 17. What is a data type?
A data type is one of many different types a variable can be set to (string, int, float, boolean).

# 18. What are the basic data types that are supported by the language?
Integer, Float, Complex-numbers, Strings, Boolean, List, Tuple, Dictionary

# 19. How do you check whether the two variables are pointing to the same object?
Using the is keyword will return true if the two variables are pointing to the same object.

# 20. What is for-else and while-else?
The else when after the for and while loop
# 21. What does immutable mean in the context of programming?
When something is immutable it cannot be changed after it is created.

# 22. What is a list in Python?
A list in python is an ordered mutable structure of a single data type.

# 23. What is a tuple in Python?
A tupe in python is an ordered immutable structure of more than one data type.

# 24. When do you choose a list over a tuple?
A list should be chosen when you have only one data type in the structure and need to dynamically add and remove entries in the list.

# 25. How do you get the last value in a list or a tuple?
The last value is stored at the max index minus 1 because the indexing in python starts at 0.

# 26. What is Index Out Of Range Error?
This error happens when the program tries to reash an index that is past the max or before the min of a object.

# 27. Why should a program close a file when it is finished using it?
Closing a file after use frees up the space and recource that was used to read and store the info for the file.

# 28. Assume the names variable references a list of strings. Write code that determines whether 'Dale' is in the names list. If it is, display the message 'Hello Dale'.  Otherwise, display the message 'No Dale'.
``` Python
names = {
    "Billy",
    "Sam",
    "Dale"
}

if("Dale" in names):
    print("Hello Dale!")
else:
    print("No Dale!")
```
# 29. Write a program that opens a specified text file then displays a list of all the unique words found in the file. Hint: Store each word as an element of a set.
``` Python
sample = set()

with open("test.txt", "r") as a_file:
    for line in a_file:
        for word in line.split():
            sample.add(word)

print(sample)
```
# 30. Write a program that reads the contents of a text file. The program should create a dictionary in which the keys are the individual words found in the file and the values are the number of times each word appears. For example, if the word "the" appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. The program should either display the frequency of each word or create a second file containing a list of each word and its frequency.
``` Python
sample = dict()

with open("test.txt", "r") as a_file:
    for line in a_file:
        for word in line.split():
            if word in sample:
                sample[word] = sample[word] + 1
            else:
                sample[word] = 1

print(sample)
```