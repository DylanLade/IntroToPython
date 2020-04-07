# randomread.py

# Read a series of random numbers from a file,
# display the numbers, count how many there are,
# and display the count.  Each random number is
# on a separate line in the file.

random_number_file_name = 'randomnum.txt'
random_number_count = 0

try: 
    random_number_file = open(random_number_file_name, "r")

    print ('List of random numbers in ', random_number_file_name, ':', sep='')

    for number in random_number_file:
        random_number_count += 1
        number = int(number)  # convert the read string to an int
        print (number)
    
    random_number_file.close()
except:
    print ('An error occurred reading', random_number_file_name)

print ('Random number count:', random_number_count)
