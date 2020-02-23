# randomwrite.py

# Write a specified number of random numbers to a file.
# Each random number is on a separate line.

import random

random_number_file_name = 'randomnum.txt'

while(True):
    try:
        quantity = int(input('How many random numbers do you want? '))
        if (quantity <= 0):
            print('The number must be a positive integer value.')
            continue           
    except:
        print('Only positive integer values are valid.')
        continue
    else:
        break

while(True):
    try:
        lower_bound = int(input('What is the lowest the random numbers should be: '))
        if (lower_bound <= 0):
            print('The number must be a positive integer value.')
            continue
    except:
        print('Only positive integer integer are valid.')
        continue
    else:
        break

while(True):
    try:
        upper_bound = int(input('What is the highest the random numbers should be: '))
        if (upper_bound <= 0):
            print('The number must be a positive integer value.')
            continue
    except:
        print('Only positive integer integer are valid.')
        continue
    else:
        break

try:
    random_number_file = open(random_number_file_name, "w")

    for n in range(quantity):
        random_number = random.randint(lower_bound, upper_bound)
        random_number_file.write(str(random_number))
        random_number_file.write('\n')

    random_number_file.close()
    print('The random numbers were written to', random_number_file_name)
except:
    print('An error occurred writing random numbers to', random_number_file_name)



    
