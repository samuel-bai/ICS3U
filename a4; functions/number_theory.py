# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Functions - Question 1
#          Using Functions to print permutations, combinations,
#          GCD, and LCM of 2 numbers and if they are Relatively Prime
# ===================================================================


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Asks for a Positive Integer; Boundary + Type Check
# Input: Positive Integer
# Output: Positive Integer that Passes Boundary + Type Check
# ====================================================================
def getPositiveInteger(low=0, high=100, prompt='Enter a positive integer '):
    strPosInt = ''
    dynaPrompt = prompt + 'between ' + str(low) + ' and ' + str(high) + ': '
    rangeCheck = False

    while not (strPosInt.isdigit() and rangeCheck):
        strPosInt = input(dynaPrompt)

        if strPosInt.isdigit():
            posInt = int(strPosInt)

            if posInt >= low and posInt <= high:
                rangeCheck = True
            else:
                print()
                print('ERROR: integer is not within the range')

        else:
            print()
            print('ERROR: input is not an integer')

    return posInt


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Calculates the Factorial of an Integer
# Input: Positive Integer
# Output: Factorial of Positive Integer
# ====================================================================
def calcFactorial(int):
    factorial = 1

    for factor in range(1, int + 1):
        factorial *= factor

    return factorial


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Calculates the Permutations of 2 Integers
# Input: Positive Integers (n, r)
# Output: Permutations of 2 Positive Integers
# ====================================================================
def calcPermutations(n, r):
    # Dependant on calcFactorial()
    if n < r:
        n, r = r, n

    permutations = calcFactorial(n) / calcFactorial(n - r)

    return permutations


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Calculates the Combinations of 2 Integers
# Input: Positive Integers (n, r)
# Output: Combinations of 2 Positive Integers
# ====================================================================
def calcCombinations(n, r):
    # Dependant on calcFactorial()
    if n < r:
        n, r = r, n

    combinations = calcFactorial(n) / (calcFactorial(r) * calcFactorial(n - r))

    return combinations


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Calculates the GCD of 2 Integers
# Input: Positive Integers (m, n)
# Output: GCD of 2 Positive Integers
# ====================================================================
def calcGCD(m, n):
    # Dependant on calcFactorial()
    t = m % n

    while t != 0:
        m, n = n, t
        t = m % n

    gcd = n
    return gcd


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Calculates the LCM of 2 Integers
# Input: Positive Integers (m, n)
# Output: LCM of 2 Positive Integers
# ====================================================================
def calcLCM(m, n):
    # Dependant on calcFactorial()
    lcm = (m * n) / calcGCD(m, n)

    return lcm


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Determines if 2 Integers are Relatively Prime
# Input: Positive Integers (m, n)
# Output: (True/False) if 2 Integers are Relatively Prime
# ====================================================================
def isRelativePrime(m, n):
    # Dependant on calcGCD()
    if calcGCD(m, n) == 1:
        return True

    else:
        return False


# Main
restart = 'Y'

while restart == 'Y':

    print()
    int1 = getPositiveInteger()
    print()
    int2 = getPositiveInteger(prompt='Enter another positive integer ')

    permutations = calcPermutations(int1, int2)
    combinations = calcCombinations(int1, int2)

    if int1 != 0 and int2 != 0:
        gcd = calcGCD(int1, int2)
        lcm = calcLCM(int1, int2)
        relativePrime = isRelativePrime(int1, int2)

        if relativePrime:
            printRelativePrime = 'Is'
        else:
            printRelativePrime = 'Is not'

    if int1 and int2 != 0:
        print('''
        For the Integers %i and %i:
        %i Permutation/s
        %i Combination/s
        GCD of %i
        LCM of %i
        %s Relatively Prime
        ''' % (int1, int2, permutations, combinations, gcd, lcm, printRelativePrime))

    else:
        print('''
        For the Integers %i and %i:
        %i Permutation/s
        %i Combination/s
        ''' % (int1, int2, permutations, combinations))

    # Asks the user if they wish to re-execute the program
    restart = input('Calculate another 2 Integers? (Y/N): ').upper()

    # Checks if the user input is either Y/N
    while restart != 'Y' and restart != 'N':
        print()
        print('ERROR: Please enter Y/N')
        restart = input('Calculate another 2 Integers? (Y/N): ').upper()