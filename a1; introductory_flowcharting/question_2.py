# Author: Samuel Bai
# Date: 02/11/2020
# Purpose: Introductory Flowcharting - Question 2
#          Area of a Triangle with an Edit Loop to Verify the Side Lengths
# ========================================================================

from math import *


# Asks the user for the triangle's side lengths
sidea = float(input("Enter the first side length: "))
sideb = float(input("Enter the second side length: "))
sidec = float(input("Enter the third side length: "))


# Checks to see if a side length/s is negative
while sidea <= 0 or sideb <= 0 or sidec <= 0:

    print('')
    print('ERROR. Side length/s is not positive.')

    # Asks the user to input 3 new triangle side lengths
    sidea = float(input("Enter the first side length: "))
    sideb = float(input("Enter the second side length: "))
    sidec = float(input("Enter the third side length: "))


# Checks to see if a side length/s form a triangle
while sidec >= sidea + sideb or sideb >= sidea + sidec or sidea >= sideb + sidec:

    print('')
    print('ERROR. Side lengths do not form a triangle.')

    # Asks the user to input 3 new triangle side lengths
    sidea = float(input("Enter the first side length: "))
    sideb = float(input("Enter the second side length: "))
    sidec = float(input("Enter the third side length: "))


# Calculates the Semi-Perimeter
semip = 1/2 * (sidea + sideb + sidec)


# Calculates and outputs the area
area = sqrt(semip * (semip - sidea) * (semip - sideb) * (semip - sidec))

print("The area of the triangle is %0.1f units squared." % area)