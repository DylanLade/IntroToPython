# Random Read python assignment
# By Dylan Lade

import sys

try:
    file = open("randomnum.txt", "r")
except FileNotFoundError:
    print("The File was not found")
    sys.exit()
except:
    print("The file failed to open")
    sys.exit()

print("List of random numbers in randomnum.txt: ")

lines = file.readlines()

for i in lines:
    print(i.rstrip("\n"))
    
print("\nRandom number count: " + str(len(lines)))