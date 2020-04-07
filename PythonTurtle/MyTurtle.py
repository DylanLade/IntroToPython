# Turtle graphics assignment by Dylan Lade

import random
from turtle import Turtle

def drawTriangle(length, turtle):
    turtle.forward(length) # draw base
 
    turtle.left(120)
    turtle.forward(length)
 
    turtle.left(120)
    turtle.forward(length)

def drawSquare(length, turtle):
    turtle.forward(length)

    turtle.left(90)
    turtle.forward(length)
    
    turtle.left(90)
    turtle.forward(length)
    
    turtle.left(90)
    turtle.forward(length)

def drawLine(turtle):
    turtle.forward(80)
    turtle.left(30)
    turtle.forward(40)

def isOdd(x):
    if(x % 2) == 1 :
        return True
    else: 
        return False

def recursive_circles3(turtle, angle, quantity, delta, radius):
    colors = ["red", "orange", "brown", "green", "blue", "purple"]
    color = random.choice(colors)
    turtle.color(color)
    turtle.right(angle)
    turtle.forward(delta)
    unit_angle = 360.0/quantity
    for x in range(quantity):
        if isOdd(x) == True:
            turtle.circle(radius)
            drawSquare(radius, turtle)
        else: 
            drawTriangle(radius, turtle)
            drawLine(turtle)

        turtle.left(unit_angle)
    radius = radius - delta
    if (radius > 1):
        recursive_circles3(turtle, angle, quantity, delta, radius)

def main():
    angle = int(input("Enter a positive number for angle: "))
    quantity = int(input("Enter a positive number for quantity: "))
    delta = int(input("Enter a positive number for delta: "))
    radius = int(input("Enter a radius: "))

    ANIMATION_SPEED = 0
    leonardo = Turtle()
    leonardo.speed(ANIMATION_SPEED)
    recursive_circles3(leonardo, angle, quantity, delta, radius)

main()