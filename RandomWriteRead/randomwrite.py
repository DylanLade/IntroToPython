# Random Write python assignment
# By Dylan Lade

from random import seed
from random import randint

while(True):
    try:
        count = int(input('How many random numbers do you? '))
        if (count <= 0):
            print('The value must be positive.')
            continue
    except:
        print('Only numerical values are valid.')
        continue
    else:
        break

while(True):
    try:
        low = int(input('What is the lowest the random number should be: '))
        if (low <= 0):
            print('The value must be positive.')
            continue
    except:
        print('Only numerical values are valid.')
        continue
    else:
        break

while(True):
    try:
        high = int(input('What is the highest the random number should be: '))
        if (high <= 0):
            print('The value must be positive.')
            continue
    except:
        print('Only numerical values are valid.')
        continue
    else:
        break

seed(((low*low) + high) * count)

try:
    file = open("randomnum.txt", "w")
except:
    print("File failed to open.")

for i in range(count):
    file.write("%d\n" % randint(low, high))

print("The random numbers were written to randomnum.txt")
