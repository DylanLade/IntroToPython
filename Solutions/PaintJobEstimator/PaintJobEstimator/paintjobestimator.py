# Paint Job Estimator
# paintjobestimator.py
# Author: Dale Musser

import math

hourly_labor_cost = 62.25  # dollars per hour
unit_of_wall_area = 350    # square feet requiring 1 gallon of paint
hours_labor_per_unit = 6   # hours of labor per unit of wall area

print ('Paint job cost estimator')

do_estimate = True
while(do_estimate):

    print ('')  # this is done to get a line spacing that looks good

    while(True):
        try:
            wall_area = float(input('What is the area of wall space in square feet? '))
            if (wall_area <= 0):
                print('Wall area must be a positive value.')
                continue
        except:
            print('Only numerical values are valid.')
            continue
        else:
            break

    while(True):
        try:
            paint_price = float(input('What is the price of the paint per gallon? '))
            if (paint_price <= 0):
                print('The price of paint must be a positive value.')
                continue
        except:
            print('Only numerical values are valid.')
            continue
        else:
            break

    # requirements specified rounded up whole gallons.
    # math.ceil rounds up a decimal value
    gallons_of_paint = math.ceil(wall_area / unit_of_wall_area)
    
    paint_cost = gallons_of_paint * paint_price
    hours_of_labor = (wall_area / unit_of_wall_area) * hours_labor_per_unit
    labor_cost = hours_of_labor * hourly_labor_cost
    total_cost = paint_cost + labor_cost

    print ('Gallons of paint:', gallons_of_paint)
    print ('Hours of labor:', format(hours_of_labor, '.1f'))
    print ('Paint cost: $', format(paint_cost,'.2f'), sep='')
    print ('Labor cost: $', format(labor_cost,'.2f'), sep='')
    print ('Total cost: $', format(total_cost,'.2f'), sep='')

    another_estimate = input('\nWould you like to do another estimate? (y/n) ')
    if (another_estimate != 'y'):
        do_estimate = False
    
