## per 350 sqft 1 can of paint and 6 hours labor
## $62.25 per hour of labor
import math
### Number of gallons (ceiling) and price of paint
### Hours of labor and total price of labor
### Price of whole job
repeat = True
while(repeat):
    try:
        area = math.ceil(float(input("Please enter the square feet of wall to be painted: ")))
    except ValueError:
        print("Please enter a round numerical value.")

    try:
        paint_price = float(input("Please enter the price per gallon of the paint to be used: "))
    except ValueError:
        print("Only numbers will be accepted. Please enter a numerical value.")


    paint_needed = math.ceil( area / 350 )
    hours = 6 * ( area / 350 )
    total_pprice = paint_needed * paint_price
    total_hprice = hours * (62.25)
    job_price = total_hprice + total_pprice

    print("The ammount of paint needed: " + str(paint_needed) + " gallons")
    print("The total hours of labor: " + str(hours) + " hours")
    print("The total cost of paint: $" + str(format(total_pprice, '.2f')))
    print("The total cost of labor: $" + str(format(total_hprice, '.2f')))
    print("The overall cost of the paint: $" + str(format(job_price, '.2f')))

    temp = input("Would you like to estimate another job(y/n): ")
    if(str(temp) == "y"):
        repeat = True
    else:
        repeat = False