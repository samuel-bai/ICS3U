# Author: Samuel Bai
# Date: 02/20/2020
# Purpose: Nesting, Div & Mod Exercise - Question 3
#          Using Booleans to Classify Triangles Based on Side Lengths
# ===================================================================

restart = 'Y'

while restart == 'Y':

    # Asks the user for the triangle's side lengths
    print('')
    sidea = float(input("Enter the first side length: "))
    sideb = float(input("Enter the second side length: "))
    sidec = float(input("Enter the third side length: "))

    # Checks to see if a side length/s is negative
    while sidea <= 0 or sideb <= 0 or sidec <= 0 or sidec >= sidea + sideb or sideb >= sidea + sidec or sidea >= sideb + sidec:
        print('')
        print('ERROR')

        # Asks the user to input a new first side length
        if sidea <= 0:
            print('Your first side length is not positive')
            sidea = float(input("Enter the first side length: "))

        # Asks the user to input a new second side length
        if sideb <= 0:
            print('Your second side length is not positive')
            sideb = float(input("Enter the second side length: "))

        # Asks the user to input a new third side length
        if sidec <= 0:
            print('Your third side length is not positive')
            sidec = float(input("Enter the third side length: "))

        # Checks to see if a side length/s form a triangle
        if sidec >= sidea + sideb or sideb >= sidea + sidec or sidea >= sideb + sidec:
            print('')
            print('ERROR')
            print('Side lengths do not form a triangle.')

            # Asks the user to input 3 new triangle side lengths
            sidea = float(input("Enter the first side length: "))
            sideb = float(input("Enter the second side length: "))
            sidec = float(input("Enter the third side length: "))

    print('')

    # Checks the length property of the triangle
    equilateral = False
    scalene = False
    isosceles = False

    # Equilateral Triangle
    if abs(sidea - sideb) < 0.000005 and abs(sidea - sidec) < 0.000005 and abs(sidec - sideb) < 0.000005:
        equilateral = True

    # Scalene Triangle
    elif sidea != sideb and sidea != sidec and sidec != sideb:
        scalene = True

    # Isosceles Triangle
    else:
        isosceles = True

    # Determines length property
    if equilateral:
        lengthProperty = 'an equilateral'

    elif scalene:
        lengthProperty = 'a scalene'

    else:
        lengthProperty = 'an isosceles'

    # Checks the angle property of the triangle
    right = False
    obtuse = False
    acute = False

    # Right Triangle
    if abs(sidec ** 2 - (sidea ** 2 + sideb ** 2)) < 0.000005 or abs(sideb ** 2 - (sidea ** 2 + sidec ** 2)) < 0.000005 or \
            abs(sidea ** 2 - (sideb ** 2 + sidec ** 2)) < 0.000005:
        right = True

    # Obtuse Triangle
    elif sidec ** 2 > sidea ** 2 + sideb ** 2 or sideb ** 2 > sidea ** 2 + sidec ** 2 or sidea ** 2 > sideb ** 2 + sidec ** 2:
        obtuse = True

    # Acute Triangle
    else:
        acute = True

    # Determines angle property
    if right:
        angleProperty = 'right triangle'
    elif obtuse:
        angleProperty = 'obtuse triangle'
    else:
        angleProperty = 'acute triangle'

    # Converts floats into integers where possible
    if sidea == int(sidea):
        sidea = int(sidea)

    if sideb == int(sideb):
        sideb = int(sideb)

    if sidec == int(sidec):
        sidec = int(sidec)

    # Prints the dimensions of the triangle and its properties
    print(sidea, sideb, sidec, '- is %s %s' % (lengthProperty, angleProperty))

    # Asks the user if they wish to re-execute the program
    print('')
    restart = input('Classify another triangle? (Y/N): ').upper()

    # Checks if the user input is either Y/N
    while restart != 'Y' and restart != 'N':
        print('')
        print('ERROR: Please enter Y/N')
        restart = input('Classify another triangle? (Y/N): ').upper()