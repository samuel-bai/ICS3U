# Author: Samuel Bai
# Date: 05/14/2020
# Purpose: OOP 3 - Question 3
#          Using Overloaded Operators to Practice
#          Arithmetic Operations on Fractions
# =================================================================

import random
from tkinter import *

userScreen = Tk()
userScreen.title("Fraction Test")


# Author: Samuel Bai
# Date: 05/22/2020
# Purpose: Create Fraction Object
# Data Elements:
#   intNumerator = int
#   intDenominator = int, != 0
# Methods:
#   __init__: Initializes OBJECT
#   calcGCD: Returns GCD of 2 Integers
#   reduce: Returns Reduced Fraction
#   setValue: Changes Fraction Using Parameter
#   randomize: Changes Fraction to Random Fraction
#   __str__: Prepares OBJECT for Print-Use
#   calcInverse: Returns Inverse of Fraction
#   __eq__: Returns if 2 Fractions are Equal
#   __add__: Returns Sum of 2 Fractions
#   __sub__: Returns Difference of 2 Fractions
#   __mul__: Returns Product of 2 Fractions
#   __truediv__: Returns Quotient of 2 Fractions
# ====================================================================
class Fraction:
    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Initializes Class; Constructor
    #   Parameters: intNumerator, intDenominator
    #   Return/Output: Fraction Object
    # ================================================================
    def __init__(self, intNumerator=0, intDenominator=1):
        if str(intNumerator).lstrip("-").isdigit():
            self.intNumerator = intNumerator
        else:
            self.intNumerator = 0

        if str(intDenominator).lstrip("-").isdigit():
            self.intDenominator = intDenominator
        else:
            self.intDenominator = 1

        self.reduce()

    #   Author: Samuel Bai
    #   Date: 03/04/2020
    #   Purpose: Calculates the GCD of 2 Integers
    #   Parameters: Positive Integers (m, n)
    #   Return/Output: GCD of 2 Positive Integers
    # ================================================================
    def calcGCD(self, int1, int2):
        m, n = int1, int2
        t = m % n

        while t != 0:
            m, n = n, t
            t = m % n

        gcd = n
        return gcd

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Reduces Fraction to Lowest Terms
    #   Parameters: N/A
    #   Return/Output: Reduced Fraction
    # ================================================================
    def reduce(self):
        if self.intDenominator == 0:
            self.intNumerator = 0
            self.intDenominator = 1

        else:
            gcd = self.calcGCD(self.intNumerator, self.intDenominator)
            self.intNumerator = self.intNumerator // gcd
            self.intDenominator = self.intDenominator // gcd

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Changes Fraction Using Parameter
    #   Parameters: intNumerator, intDenominator
    #   Return/Output: Changed Fraction
    # ================================================================
    def setValue(self, intNumerator, intDenominator):
        if str(intNumerator).isdigit():
            self.intNumerator = intNumerator
        else:
            self.intNumerator = 0

        if str(intDenominator).isdigit():
            self.intDenominator = intDenominator
        else:
            self.intDenominator = intDenominator

        self.reduce()

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Changes Fraction to Random Value
    #   Parameters: maxInt
    #   Return/Output: Randomized Fraction
    # ================================================================
    def randomize(self, maxInt=10):
        if not str(maxInt).isdigit():
            maxInt = 10

        self.intNumerator = random.randint(-maxInt, maxInt)
        self.intDenominator = random.randint(-maxInt, maxInt)
        self.reduce()

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Convert and Prepare OBJECT for Print-Use
    #   Parameters: N/A
    #   Return/Output: String Conversion
    # ================================================================
    def __str__(self):
        wholeNum = abs(self.intNumerator) // self.intDenominator
        numerator = abs(self.intNumerator) % self.intDenominator
        denominator = self.intDenominator

        if self.intNumerator >= 0:
            if numerator == 0:
                mixedFraction = "%i" % wholeNum
            elif wholeNum == 0:
                mixedFraction = "%i / %i" % (numerator, denominator)
            else:
                mixedFraction = "%i  %i / %i" % (wholeNum, numerator, denominator)

        else:
            if numerator == 0:
                mixedFraction = "%i" % -wholeNum
            elif wholeNum == 0:
                mixedFraction = "%i / %i" % (-numerator, denominator)
            else:
                mixedFraction = "%i  %i / %i" % (-wholeNum, numerator, denominator)

        return mixedFraction

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Returns Inverse of Fraction
    #   Parameters: N/A
    #   Return/Output: Inverted Fraction
    # ================================================================
    def calcInverse(self):
        if self.intNumerator != 0:
            denominator = self.intNumerator
            numerator = self.intDenominator
        else:
            denominator = self.intDenominator
            numerator = self.intNumerator

        tempFraction = Fraction(intNumerator=numerator, intDenominator=denominator)

        return tempFraction

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Overloads '==' for Fraction Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Fraction == Other Fraction
    # ================================================================
    def __eq__(self, other):
        if self.intNumerator == other.intNumerator and \
                self.intDenominator == other.intDenominator:
            equal = True

        else:
            equal = False

        return equal

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Overloads '+' for Fraction Class
    #   Parameters: N/A
    #   Return/Output: Sum of 2 Fractions
    # ================================================================
    def __add__(self, other):
        numerator1 = self.intNumerator * other.intDenominator
        numerator2 = other.intNumerator * self.intDenominator

        denominator = self.intDenominator * other.intDenominator
        numerator = numerator1 + numerator2

        tempFraction = Fraction(intNumerator=numerator, intDenominator=denominator)

        return tempFraction

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Overloads '-' for Fraction Class
    #   Parameters: N/A
    #   Return/Output: Difference of 2 Fractions
    # ================================================================
    def __sub__(self, other):
        numerator1 = self.intNumerator * other.intDenominator
        numerator2 = other.intNumerator * self.intDenominator

        denominator = self.intDenominator * other.intDenominator
        numerator = numerator1 - numerator2

        tempFraction = Fraction(intNumerator=numerator, intDenominator=denominator)

        return tempFraction

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Overloads '*' for Fraction Class
    #   Parameters: N/A
    #   Return/Output: Product of 2 Fractions
    # ================================================================
    def __mul__(self, other):
        denominator = self.intDenominator * other.intDenominator
        numerator = self.intNumerator * other.intNumerator

        tempFraction = Fraction(intNumerator=numerator, intDenominator=denominator)

        return tempFraction

    #   Author: Samuel Bai
    #   Date: 05/22/2020
    #   Purpose: Overloads '/' for Fraction Class
    #   Parameters: N/A
    #   Return/Output: Quotient of 2 Fractions
    # ================================================================
    def __truediv__(self, other):
        inverseOther = other.calcInverse()

        denominator = self.intDenominator * inverseOther.intDenominator
        numerator = self.intNumerator * inverseOther.intNumerator

        tempFraction = Fraction(intNumerator=numerator, intDenominator=denominator)

        return tempFraction


userScreen.resizable(0, 0)
objEquation = StringVar()
varAnswer = StringVar()
varResponse = StringVar()

objScoreboard = StringVar(value="Score :  0 / 0")
correctAnswers = 0
totalAnswers = 0


# ====================================================================
# Author: Samuel Bai
# Date: 05/26/2020
# Purpose: Generates a Fraction Equation, Correct & Incorrect Answers
# Input: N/A
# Output: Random Fraction Equation, Correct & Incorrect Answers
# Dependencies: Fraction Class
# ====================================================================
def createEquation():
    firstFraction = Fraction()
    firstFraction.randomize()

    secondFraction = Fraction()
    secondFraction.randomize()

    operator = random.choice(["+", "-", "x", "÷"])

    while secondFraction.intNumerator == 0 and operator == "÷":
        secondFraction.randomize()

    if operator == "+":
        correctAnswer = firstFraction + secondFraction
    elif operator == "-":
        correctAnswer = firstFraction - secondFraction
    elif operator == "x":
        correctAnswer = firstFraction * secondFraction
    else:
        correctAnswer = firstFraction / secondFraction

    incorrectAnswer = correctAnswer.calcInverse()

    if correctAnswer == incorrectAnswer:
        output = "%s   %s   %s   =   %s" % (firstFraction, operator, secondFraction, correctAnswer)
        answer = "Right"

    else:
        outputSelection = random.randint(0, 1)
        if outputSelection == 0:
            output = "%s   %s   %s   =   %s" % (firstFraction, operator, secondFraction, correctAnswer)
            answer = "Right"
        else:
            output = "%s   %s   %s   =   %s" % (firstFraction, operator, secondFraction, incorrectAnswer)
            answer = "Wrong"

    objEquation.set(output)
    varAnswer.set(answer)


# Author: Samuel Bai
# Date: 05/26/2020
# Purpose: Determines if User Response Matches Correct Answer, Keeps Score
# Input: N/A
# Output: Fraction Test Score, Updated Every Round
# Dependencies: Tkinter
# ====================================================================
def updateScoreboard():
    global correctAnswers
    global totalAnswers
    
    answer = varAnswer.get()
    response = varResponse.get()
    
    totalAnswers += 1
    if answer == response:
        correctAnswers += 1
        
    output = "Score :  %i / %i" % (correctAnswers, totalAnswers)
    
    objScoreboard.set(output)
    

# Author: Samuel Bai
# Date: 05/26/2020
# Purpose: Sets User Response to "Right"
# Input: N/A
# Output: User Response "Right", Updated Scoreboard, New Equation
# Dependencies: Tkinter
# ====================================================================
def rightButtonClicked():
    varResponse.set("Right")
    updateScoreboard()
    createEquation()


# Author: Samuel Bai
# Date: 05/26/2020
# Purpose: Sets User Response to "Wrong"
# Input: N/A
# Output: User Response "Wrong", Updated Scoreboard, New Equation
# Dependencies: Tkinter
# ====================================================================
def wrongButtonClicked():
    varResponse.set("Wrong")
    updateScoreboard()
    createEquation()
    

# ====================================================================
widLabelEquation = Label(userScreen, textvariable=objEquation, font="TkFixedFont 12 bold")

widLabelScoreboard = Label(userScreen, height=2, font="TkFixedFont 12", textvariable=objScoreboard)

widButtonRight = Button(userScreen, text="Right", font="TkFixedFont 10", relief=GROOVE, bg="white", activebackground="white", width=20, command=lambda: rightButtonClicked())
widButtonWrong = Button(userScreen, text="Wrong", font="TkFixedFont 10", relief=GROOVE, bg="white", activebackground="white", width=20, command=lambda: wrongButtonClicked())

# ====================================================================
widLabelEquation.grid(row=1, column=1, columnspan=2)

widLabelScoreboard.grid(row=2, column=1, columnspan=2)

widButtonRight.grid(row=3, column=1)
widButtonWrong.grid(row=3, column=2)


# ====================================================================
userScreen.after_idle(createEquation)
userScreen.mainloop()