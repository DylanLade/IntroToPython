# Numstat python assignment
# By Dylan Lade

import math

total = 0

file = open("numbers.txt", "r")
lines = file.readlines()

array = []

for i in lines:
    temp = i.strip("\n")
    total += int(temp)
    array.append(int(temp))
    
average = (total/len(array))
arrayRange = (max(array) - min(array))

print("Grabbing number information from : numbers.txt")

print("Sum: " + str(total))
print("Count: " + str(len(array)))
print("Average: " + str(average))
print("Maximum: " + str(max(array)))
print("Minimum: " + str(min(array)))
print("Range: " + str(arrayRange))
