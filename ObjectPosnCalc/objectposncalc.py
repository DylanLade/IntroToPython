## Forgot this in the first one
## Python program by Dylan Lade for Python Programming 1

## Make a function to do the calcualtion
def calcPos(x, v,  a, t):
    return ((x)+(v*t)+((.5*(a*(t*t)))))

## Get the input values


initialX = input("Enter the initial position in meters: ")

initialV = input("Enter the initial velocity in meters per second: ")

accel = input("Enter the acceleration in meters per second per second: ")

time = input("Enter the time elapsed in seconds: ")

while(float(time) < 0): ## Keep asking for time if it is negative
    time = input("Enter the time elapsed in seconds(time can't be negarive): ")

## Convert the strings to float and pass them into the function

finalPosition = calcPos(float(initialX), float(initialV), float(accel), float(time))

print("The final position of the object is " + str(finalPosition) + "m.")