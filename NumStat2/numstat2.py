# Numstat2 python assignment
# By Dylan Lade

import math
import statistics
from collections import Counter

loop = "y"

while(loop == 'y'):
    filename = input('What file would you like to read? ')

    total = 0

    try:
        file = open(filename, "r")
    except:
        print("File failed to open. Would you like to try another file? (y/n) ")
        loop = input()
        if(loop == 'y'):
            continue
        else:
            break

    lines = file.readlines()

    array = []

    for i in lines:
        temp = i.strip("\n")
        total += int(temp)
        array.append(int(temp))
    
    if(len(array) == 0):
        print("There are no numbers in " + filename)
        loop = input("Would you like to evaluate another file? (y/n) ")
        if(loop == 'y'):
            continue
        else:
            break

    n = len(array)
    
    data = Counter(array)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    

    average = (total/len(array))
    arrayRange = (max(array) - min(array))
    median = statistics.median(array)


    print("Grabbing number information from : " + filename)

    print("Sum: " + str(total))
    print("Count: " + str(len(array)))
    print("Average: " + str(average))
    print("Maximum: " + str(max(array)))
    print("Minimum: " + str(min(array)))
    print("Range: " + str(arrayRange))
    print("Median: " + str(median))
    print("Mode: " + str(mode))

    loop = input("Would you like to evaluate another file? (y/n) ")
