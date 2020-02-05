## Forgot this in the first one
## Python program by Dylan Lade for Python Programming 1

## Make a function to do the calcualtion
def calcPos(x, v,  a, t):
    return ((x)+(v*t)+((.5*(a*(t*t)))))

## Get the input values
loop = True
while(loop):
    initialX = input("Enter the initial position in meters: ")
## Loop if the value entered is not a valid number
    while(not initialX.isdigit()):
        initialX = input("Enter the initial position in meters(Must be a number): ")

    initialV = input("Enter the initial velocity in meters per second: ")
## Loop if the value entered is not a valid number
    while(not initialV.isdigit()):
        initialV = input("Enter the initial velocity in meters per second(Must be a number): ")

    accel = input("Enter the acceleration in meters per second per second: ")
## Loop if the value entered is not a valid number
    while(not accel.isdigit()):
        accel = input("Enter the acceleration in meters per second per second(Must be a number): ")

    time = input("Enter the time elapsed in seconds: ")

    while(not time.isdigit() or float(time) < 0): ## Keep asking for time if it is negative
        time = input("Enter the time elapsed in seconds(time must be a number and can't be negative): ")

## Convert the strings to float and pass them into the function

    finalPosition = calcPos(float(initialX), float(initialV), float(accel), float(time))

    print("The final position of the object is " + str(finalPosition) + "m.\n")

    anotherOne = input("Would you like to calculate again?(yes/no) ")
    if(anotherOne == "yes"):
        loop = True
    else:
        loop = False