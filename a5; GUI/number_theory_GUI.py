# Author: Samuel Bai
# Date: 03/11/2020
# Purpose: GUI - Question 1
#          Using Tkinter to Create GUI for Number Theory Assignment
# =================================================================

from tkinter import *

userScreen = Tk()


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
    if m != 0 and n != 0:
        t = m % n

        while t != 0:
            m, n = n, t
            t = m % n

        gcd = n
    else:
        gcd = 0

    return gcd


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Calculates the LCM of 2 Integers
# Input: Positive Integers (m, n)
# Output: LCM of 2 Positive Integers
# ====================================================================
def calcLCM(m, n):
    # Dependant on calcFactorial()
    if m != 0 and n != 0:
        lcm = (m * n) / calcGCD(m, n)
    else:
        lcm = 0

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


userScreen.resizable(0, 0)
objN = StringVar()
objM = StringVar()
varFuncSelect = StringVar()
objOutput = StringVar()


# ====================================================================
# Author: Samuel Bai
# Date: 04/06/2020
# Purpose: Clears the Pattern being Displayed
# Input: N/A
# Output: Blank String
# ====================================================================
def clearButtonClicked():
    objN.set("")
    objM.set("")
    objOutput.set("")


# Author: Samuel Bai
# Date: 04/06/2020
# Purpose: Determines the Type of Function to Perform, Based on User Input
# Input: N/A
# Output: Permutation, Combination, LCM, GCD Calculation or if 2 Integers are Relative Primes
# Dependencies: calcPermutations(), calcCombinations(), calcLCM(), calcGCD(), isRelativePrime()
# ====================================================================
def selectButtonClicked():
    strN = objN.get()
    strM = objM.get()
    functionProperty = varFuncSelect.get()

    if strN.isdigit() and strM.isdigit():

        intN, intM = int(strN), int(strM)
        if intN <= 150 and intM <= 150:

            if functionProperty == "permutations":
                permutation = int(calcPermutations(intN, intM))
                objOutput.set(str(permutation))

            elif functionProperty == "combinations":
                combinations = int(calcCombinations(intN, intM))
                objOutput.set(str(combinations))

            elif functionProperty == "lcm":
                lcm = int(calcLCM(intN, intM))
                if lcm == 0:
                    lcm = 'Invalid Input'
                objOutput.set(str(lcm))

            elif functionProperty == "gcd":
                gcd = int(calcGCD(intN, intM))
                if gcd == 0:
                    gcd = 'Invalid Input'
                objOutput.set(str(gcd))

            elif functionProperty == "relative prime":
                relativePrime = isRelativePrime(intN, intM)

                if relativePrime:
                    objOutput.set('Yes')
                else:
                    objOutput.set('No')

            else:
                objOutput.set('Please Choose a Function')
        else:
            objOutput.set('Please Keep Inputs Under 150')
    else:
        objOutput.set('Invalid Input')


# ====================================================================
widLabelTitle = Label(userScreen, font="Helvetica 10 bold", text='NUMBER THEORY \n Samuel\'s Number Theory Calculator \n ')
widLabelRules = Label(userScreen, justify=LEFT, text='Rules: \n1. Inputs must be less than / equal to 150 \n2. Inputs must be positive integers \n3. Inputs cannot be 0 for GCD, LCM, & Is Relative Prime \n')

widLabelInt = Label(userScreen, font="Helvetica 9 underline", text='2 Positive Integers:')
widLabelN = Label(userScreen, text='Enter the first integer: ')
widEntryN = Entry(userScreen, textvariable=objN)
widLabelM = Label(userScreen, text='Enter the second integer: ')
widEntryM = Entry(userScreen, textvariable=objM)

widLabelFunc = Label(userScreen, font="Helvetica 9 underline", text="Function Selection:")
widCalcPermutations = Radiobutton(userScreen, text='Calculate Permutations', anchor=W, width=18, variable=varFuncSelect, value="permutations")
widCalcCombinations = Radiobutton(userScreen, text='Calculate Combinations', anchor=W, width=18, variable=varFuncSelect, value="combinations")
widCalcLCM = Radiobutton(userScreen, text='Calculate LCM', anchor=W, width=18, variable=varFuncSelect, value="lcm")
widCalcGCD = Radiobutton(userScreen, text='Calculate GCD', anchor=W, width=18, variable=varFuncSelect, value="gcd")
widRelativePrime = Radiobutton(userScreen, text='Is Relative Prime', anchor=W, width=18, variable=varFuncSelect, value="relative prime")

widLabelSpacer = Label(userScreen, text="")
widCalculate = Button(userScreen, text="Calculate", width=19, relief=GROOVE, bg="white", activebackground="white", command=lambda: selectButtonClicked())

widClear = Button(userScreen, text='Clear', width=19, relief=GROOVE, bg="white", activebackground="white", command=lambda: clearButtonClicked())
widExit = Button(userScreen, text='Exit', width=19, relief=GROOVE, bg="white", activebackground="red", activeforeground="white", command=lambda: userScreen.destroy())

widLabelOutput = Label(userScreen, height=10, width=40, wraplength=250, justify=LEFT, relief=RIDGE, textvariable=objOutput)

# ====================================================================
widLabelTitle.grid(row=0, column=1, columnspan=4)
widLabelRules.grid(row=1, column=1, columnspan=4)

widLabelInt.grid(row=2, column=2)
widLabelN.grid(row=3, column=2)
widEntryN.grid(row=4, column=2)
widLabelM.grid(row=6, column=2)
widEntryM.grid(row=7, column=2)

widLabelFunc.grid(row=2, column=1)
widCalcPermutations.grid(row=3, column=1)
widCalcCombinations.grid(row=4, column=1)
widCalcGCD.grid(row=5, column=1)
widCalcLCM.grid(row=6, column=1)
widRelativePrime.grid(row=7, column=1)

widLabelSpacer.grid(row=8, column=2)
widCalculate.grid(row=8, column=1, columnspan=2, rowspan=2)

widLabelOutput.grid(row=2, column=3, columnspan=2, rowspan=6)

widClear.grid(row=9, column=3)
widExit.grid(row=9, column=4)

# ====================================================================
mainloop()