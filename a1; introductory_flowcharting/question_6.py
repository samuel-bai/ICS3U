# Author: Samuel Bai
# Date: 02/12/2020
# Purpose: Introductory Flowcharting - Question 6
#          Middle Number of 3 Different Positive, Odd Integers
# ============================================================

# Asks the user for the 3 integers
print('Please enter 3 different positive, odd integers.')

num1 = int(input('Please enter your first integer: '))
num2 = int(input('Please enter your second integer: '))
num3 = int(input('Please enter your third integer: '))

# Checks for an input error
while num1 == num2 or num2 == num3 or num3 == num1 or num1 % 2 == 0 or num2 % 2 == 0 or num3 % 2 == 0 or num1 < 0 or num2 < 0 or num3 < 0:

    # States that there is an error
    print('')
    print('ERROR:')

    # States the specific error/s that the inputs have
    if num1 == num2 or num2 == num3 or num3 == num1:
        print('2 or more inputs are the same.')

    if num1 % 2 == 0 or num2 % 2 == 0 or num3 % 2 == 0:
        print('1 or more inputs are even.')

    if num1 < 0 or num2 < 0 or num3 < 0:
        print('1 or more inputs are negative.')

    # Asks the user to input 3 integers again
    print('')
    print('Please enter 3 different positive, odd integers.')
    num1 = int(input('Please enter your first number: '))
    num2 = int(input('Please enter your second number: '))
    num3 = int(input('Please enter your third number: '))

# Selects and prints the middle number
print('The middle number is', end=' ')

if num1 > num2 > num3 or num3 > num2 > num1:
    print(num2)

elif num2 > num1 > num3 or num3 > num1 > num2:
    print(num1)

else:
    print(num3)
