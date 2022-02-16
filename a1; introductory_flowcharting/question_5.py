# Author: Samuel Bai
# Date: 02/12/2020
# Purpose: Introductory Flowcharting - Question 5
#          Using Elif Statements to Determine Academic Level
# ================================================================

# Asks the user to input their mark
mark = float(input('Please enter your mark: '))

# Checks if the mark inputted is invalid
while mark < 0 or mark > 100:

    print('Error. Mark entered was not between 1 - 100.')

    # Asks the user to input a valid mark
    mark = float(input('Please enter your mark: '))


# Determines the academic level of the mark
print('You', end=' ')

if mark < 39.5:
    print('have been Unsuccessful')

elif mark < 49.5:
    print('need Credit Recovery')

elif mark < 59.5:
    print('have achieved Level 1')

elif mark < 69.5:
    print('have achieved Level 2')

elif mark < 79.5:
    print('have achieved Level 3')

else:
    print('have achieved Level 4')