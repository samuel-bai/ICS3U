# Author: Samuel Bai
# Date: 02/11/2020
# Purpose: Introductory Flowcharting - Question 4
#          Using Counting Loops to Calculate Equations
# ====================================================

# Series 1:
total = 1
int = 1

while int <= 20:

    total *= int

    int += 1

# Prints the result of the sequence
print('The result of Sequence 1 is ', total)
print('')


# Series 2:
count = 0
pretotal = 0

while count < 1000000:

    denom = 2 * count + 1

    if 0 == count % 2:
        pretotal += 1 / denom
    else:
        pretotal -= 1 / denom

    count += 1

total = pretotal * 4

# Prints the result of the sequence
print('The result of Sequence 2 is ', total)
print('')


# Series 3:
count = 0
total = 0

while count < 1000000:

    denom1 = 2 * count + 1

    denom2 = denom1 + 2

    denom = denom1 * denom2

    total += 1 / denom

    count += 1

# Prints the result of the sequence
print('The result of Sequence 3 is ', total)