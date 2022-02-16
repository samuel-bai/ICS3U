# Author: Samuel Bai
# Date: 02/11/2020
# Purpose: Introductory Flowcharting - Question 3
#          Using Counting Loops to Produce Sequences
# ==================================================


# Sequence 1:
print('Sequence 1 is:')

num = 5

while num <= 50:

    # Decides if the number should be printed with/out a ',' afterwards
    if num == 50:
        print(num)
    else:
        print(num, end=', ')

    num += 3

print('')


# Sequence 2:
print('Sequence 2 is:')

num = 90

while num >= 50:

    # Decides if the number should be printed with/out a ',' afterwards
    if num == 50:
        print(num)
    else:
        print(num, end=', ')

    num -= 4

print('')


# Sequence 3:
print('Sequence 3 is:')

num = 3

while num <= 24576:

    # Decides if the number should be printed with/out a ',' afterwards
    if num == 24576:
        print(num)
    else:
        print(num, end=', ')

    num *= 2

print('')


# Sequence 4:
print('Sequence 4 is:')

term = 0

while term <= 14:

    num = 3 ** term

    # Decides if the number should be printed with/out a ',' afterwards
    if term == 14:
        print(num)
    else:
        print(num, end=', ')

    term += 1