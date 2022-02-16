# Author: Samuel Bai
# Date: 02/13/2020
# Purpose: Nesting, Div & Mod Exercise - Question 2
#          Calculating the Digits of a Positive Integer, their Sum
#          the Integer's Reverse, if it's a Palindrome, and it's Digital Root
# ===========================================================================

restart = 'Y'

while restart == 'Y':

    # Asks the user for a positive integer
    print('')
    posInt = int(input('Please input a positive integer: '))

    # Checks if the integer is positive and asks the user for another input when necessary
    while posInt <= 0:
        print('ERROR: You did not enter a positive integer')
        posInt = int(input('Please input a positive integer: '))

    print('')

    # Number of digits in the number
    intCon1 = posInt
    digCount = 0

    while intCon1 != 0:
        intCon1 = intCon1 // 10
        digCount += 1

    print('Your integer has %i digits' % digCount)

    # Sum of the digits
    intCon2 = posInt
    intSum = 0

    while intCon2 != 0:
        intSum += intCon2 % 10
        intCon2 //= 10

    print('The sum of its digits is %i' % intSum)

    # Reverse of the number
    intCon3 = posInt
    intRev = 0

    while digCount != 0:
        digCount -= 1
        intRev += (intCon3 % 10) * (10 ** digCount)
        intCon3 //= 10

    print('Its reverse is %i' % intRev)

    # Palindrome or not
    if intRev == posInt:
        print('This integer is a palindrome')

    else:
        print('This integer is not a Palindrome')

    # Digital Root
    digRoot = 0
    rootCount = 0

    while rootCount != 20:

        while intSum != 0:
            digRoot += intSum % 10
            intSum //= 10

        intSum = digRoot
        digRoot = 0
        rootCount += 1

    print('Its digital root is %i' % intSum)

    # Asks the user if they wish to re-execute the program
    print('')
    restart = input('Calculate another integer? (Y/N): ').upper()

    # Checks if the user input is either Y/N
    while restart != 'Y' and restart != 'N':
        print('')
        print('ERROR: Please enter Y/N')
        print('')
        restart = input('Calculate another integer? (Y/N): ').upper()