# Author: Samuel Bai
# Date: 05/13/2020
# Purpose: OOP 3 - Question 2
#          Using Overloaded Operators to Compare and
#          Perform Arithmetic Operations on Dominoes
# =================================================================

import random
from tkinter import *

userScreen = Tk()
userScreen.title("Domino")


# Author: Samuel Bai
# Date: 04/21/2020
# Purpose: Create Domino Objects
# Data Elements:
#   value = 0 - 66, 0 <= value % 10 <= 6
#   size = 30 - 100
#   diameter = size // 5
#   gap = diameter // 2
#   orientation = V or H
#   faceUp = True or False
# Methods:
#   __init__: Initializes OBJECT
#   __str__: Prepares OBJECT for Print-Use
#   getValue: Asks User to Set Domino value
#   setValue: Changes value using Parameter
#   flip: Swaps 10's and 1's Value
#   setOrientation: Changes orientation using Parameter
#   setSize: Changes size using Parameter
#   setFace: Changes faceUp using Parameter
#   randomize: Sets a Random Domino value
#   draw: Calls on drawHalf twice
#   drawHalf: Draws Half of Domino
#   getLessorValue: Converts Domino Value to its Lessor Value
#   __add__: Returns Sum of 2 Dominoes
#   __sub__: Returns Difference of 2 Dominoes
#   __mul__: Returns Product of 2 Dominoes
#   __gt__: Returns if One Domino is > Other Domino
#   __lt__: Returns if One Domino is < Other Domino
#   __ge__: Returns if One Domino is >= Other Domino
#   __le__: Returns if One Domino is <= Other Domino
#   __eq__: Returns if 2 Dominoes are Equal
#   __ne__: Returns if 2 Dominoes are Not Equal
# ====================================================================
class Domino:
    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Initializes Class; Constructor
    #   Parameters: value, size, orientation, faceUp
    #   Return/Output: Domino Object
    # ================================================================
    def __init__(self, value=11, size=30, orientation='H', faceUp=True):
        if value < 0 or value > 66 or value // 10 > 6 or value % 10 > 6:
            self.randomize()
        else:
            self.value = value

        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 60

        if orientation == "H" or orientation == "V":
            self.orientation = orientation
        else:
            self.orientation = "H"

        if faceUp or not faceUp:
            self.faceUp = faceUp
        else:
            self.faceUp = True

        self.diameter = size // 5
        self.gap = self.diameter // 2

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Convert and Prepares OBJECT for Print-Use
    #   Parameters: N/A
    #   Return/Output: String Conversion
    # ================================================================
    def __str__(self):
        return str(self.value)

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Asks User to Set Domino value
    #   Parameters: N/A
    #   Return/Output: Domino value
    # ================================================================
    def getValue(self):
        value1 = self.getPositiveInteger(0, 6, "Enter your first domino value")
        value2 = self.getPositiveInteger(0, 6, "Enter your second domino value")

        self.value = value1 * 10 + value2

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Changes value using Parameter
    #   Parameters: value
    #   Return/Output: Domino value
    # ================================================================
    def setValue(self, value=0):
        if value <= 0 or value > 66 or value // 10 > 6 or value % 10 > 6:
            self.value = value
        else:
            self.value = 0

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Swaps 10's and 1's Value
    #   Parameters: N/A
    #   Return/Output: Flipped Domino value
    # ================================================================
    def flip(self):
        value1 = self.value % 10
        value2 = self.value // 10
        value1 *= 10

        self.value = value1 + value2

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Changes orientation using Parameter
    #   Parameters: orientation
    #   Return/Output: Domino orientation
    # ================================================================
    def setOrientation(self, orientation="H"):
        if orientation == "H" or orientation == "V":
            self.orientation = orientation
        else:
            self.orientation = "H"

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Changes size using Parameter
    #   Parameters: size
    #   Return/Output: Domino size
    # ================================================================
    def setSize(self, size=30):
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 60

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Changes faceUp using Parameter
    #   Parameters: faceUp
    #   Return/Output: Is Domino faceUp (True/False)
    # ================================================================
    def setFace(self, faceUp=True):
        if faceUp or not faceUp:
            self.faceUp = faceUp
        else:
            self.faceUp = True

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Sets a Random Domino value
    #   Parameters: N/A
    #   Return/Output: Domino value
    # ================================================================
    def randomize(self):
        self.value = random.randint(1, 6) * 10 + random.randint(1, 6)

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Draws Domino by Calling drawHalf() Twice
    #   Parameters: canvas, x, y
    #   Return/Output: Domino Object
    # ================================================================
    def draw(self, canvas, x=60, y=30):
        self.drawHalf(canvas, x, y, self.value // 10)

        if self.orientation == "H":
            self.drawHalf(canvas, x + self.size, y, self.value % 10)
        else:
            self.drawHalf(canvas, x, y + self.size, self.value % 10)

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Draws Half of Domino
    #   Parameters: canvas, x, y, value
    #   Return/Output: Half of Domino Object
    # ================================================================
    def drawHalf(self, canvas, x, y, value):
        gap = self.gap
        diameter = self.diameter
        size = self.size
        faceUp = self.faceUp

        if faceUp:
            canvas.create_rectangle(x, y, x + size, y + size, width=1, outline="black", fill="white")

            if value == 1:
                canvas.create_oval(x + 2 * gap + diameter, y + 2 * gap + diameter, x + 2 * (gap + diameter),
                                   y + 2 * (gap + diameter), fill="black")

            elif value == 2:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill="black")
                canvas.create_oval(x + 3 * gap + 2 * diameter, y + 3 * gap + 2 * diameter, x + 3 * (gap + diameter),
                                   y + 3 * (gap + diameter), fill="black")

            elif value == 3:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill="black")
                canvas.create_oval(x + 2 * gap + diameter, y + 2 * gap + diameter, x + 2 * (gap + diameter),
                                   y + 2 * (gap + diameter), fill="black")
                canvas.create_oval(x + 3 * gap + 2 * diameter, y + 3 * gap + 2 * diameter, x + 3 * (gap + diameter),
                                   y + 3 * (gap + diameter), fill="black")

            elif value == 4:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill="black")
                canvas.create_oval(x + gap, y + 3 * gap + 2 * diameter, x + gap + diameter, y + 3 * (gap + diameter),
                                   fill="black")
                canvas.create_oval(x + 3 * gap + 2 * diameter, y + gap, x + 3 * (gap + diameter), y + gap + diameter,
                                   fill="black")
                canvas.create_oval(x + 3 * gap + 2 * diameter, y + 3 * gap + 2 * diameter, x + 3 * (gap + diameter),
                                   y + 3 * (gap + diameter), fill="black")

            elif value == 5:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill="black")
                canvas.create_oval(x + gap, y + 3 * gap + 2 * diameter, x + gap + diameter, y + 3 * (gap + diameter),
                                   fill="black")
                canvas.create_oval(x + 2 * gap + diameter, y + 2 * gap + diameter, x + 2 * (gap + diameter),
                                   y + 2 * (gap + diameter), fill="black")
                canvas.create_oval(x + 3 * gap + 2 * diameter, y + gap, x + 3 * (gap + diameter), y + gap + diameter,
                                   fill="black")
                canvas.create_oval(x + 3 * gap + 2 * diameter, y + 3 * gap + 2 * diameter, x + 3 * (gap + diameter),
                                   y + 3 * (gap + diameter), fill="black")

            elif value == 6:
                canvas.create_oval(x + gap, y + gap, x + gap + diameter, y + gap + diameter, fill="black")
                canvas.create_oval(x + gap, y + 2 * gap + diameter, x + gap + diameter, y + 2 * (gap + diameter),
                                   fill="black")
                canvas.create_oval(x + gap, y + 3 * gap + 2 * diameter, x + gap + diameter, y + 3 * (gap + diameter),
                                   fill="black")
                canvas.create_oval(x + 3 * gap + 2 * diameter, y + gap, x + 3 * (gap + diameter), y + gap + diameter,
                                   fill="black")
                canvas.create_oval(x + 3 * gap + 2 * diameter, y + 2 * gap + diameter, x + 3 * (gap + diameter),
                                   y + 2 * (gap + diameter), fill="black")
                canvas.create_oval(x + 3 * gap + 2 * diameter, y + 3 * gap + 2 * diameter, x + 3 * (gap + diameter),
                                   y + 3 * (gap + diameter), fill="black")

        else:
            canvas.create_rectangle(x, y, x + size, y + size, width=1, outline="black", fill="grey")

    #   Author: Samuel Bai
    #   Date: 03/04/2020
    #   Purpose: Asks for a Positive Integer; Boundary + Type Check
    #   Parameters: low, high, prompt
    #   Return/Output: Positive Integer that Passes Boundary + Type Check
    # ================================================================
    def getPositiveInteger(self, low=0, high=100, prompt='Enter a positive integer '):
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

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Sets a Domino to its lessor value
    #   Parameters: domino
    #   Return/Output: lessor value of Domino
    # ================================================================
    def getLessorValue(self, domino):
        if domino.value // 10 > domino.value % 10:
            domino.flip()

        return domino

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Overloads '+' for Domino Class
    #   Parameters: N/A
    #   Return/Output: Sum of 2 Domino Values
    # ================================================================
    def __add__(self, other):
        firstDomino = self
        secondDomino = other

        firstDomino = self.getLessorValue(firstDomino)
        secondDomino = self.getLessorValue(secondDomino)

        addition = firstDomino.value + secondDomino.value

        return addition

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Overloads '-' for Domino Class
    #   Parameters: N/A
    #   Return/Output: Difference of 2 Domino Values
    # ================================================================
    def __sub__(self, other):
        firstDomino = self
        secondDomino = other

        firstDomino = self.getLessorValue(firstDomino)
        secondDomino = self.getLessorValue(secondDomino)

        subtraction = firstDomino.value - secondDomino.value

        return subtraction

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Overloads '*' for Domino Class
    #   Parameters: N/A
    #   Return/Output: Product of 2 Domino Values
    # ================================================================
    def __mul__(self, other):
        firstDomino = self
        secondDomino = other

        firstDomino = self.getLessorValue(firstDomino)
        secondDomino = self.getLessorValue(secondDomino)

        multiplication = firstDomino.value * secondDomino.value

        return multiplication

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Overloads '>' for Domino Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Domino > Other Domino
    # ================================================================
    def __gt__(self, other):
        firstDomino = self
        secondDomino = other

        firstDomino = self.getLessorValue(firstDomino)
        secondDomino = self.getLessorValue(secondDomino)

        if firstDomino.value > secondDomino.value:
            greaterThan = True
        else:
            greaterThan = False

        return greaterThan

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Overloads '<' for Domino Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Domino < Other Domino
    # ================================================================
    def __lt__(self, other):
        firstDomino = self
        secondDomino = other

        firstDomino = self.getLessorValue(firstDomino)
        secondDomino = self.getLessorValue(secondDomino)

        if firstDomino.value < secondDomino.value:
            lessThan = True
        else:
            lessThan = False

        return lessThan

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Overloads '>=' for Domino Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Domino >= Other Domino
    # ================================================================
    def __ge__(self, other):
        firstDomino = self
        secondDomino = other

        firstDomino = self.getLessorValue(firstDomino)
        secondDomino = self.getLessorValue(secondDomino)

        if firstDomino.value >= secondDomino.value:
            greaterEqual = True
        else:
            greaterEqual = False

        return greaterEqual

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Overloads '<=' for Domino Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Domino <= Other Domino
    # ================================================================
    def __le__(self, other):
        firstDomino = self
        secondDomino = other

        firstDomino = self.getLessorValue(firstDomino)
        secondDomino = self.getLessorValue(secondDomino)

        if firstDomino.value <= secondDomino.value:
            lessEqual = True
        else:
            lessEqual = False

        return lessEqual

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Overloads '==' for Domino Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Domino == Other Domino
    # ================================================================
    def __eq__(self, other):
        firstDomino = self
        secondDomino = other

        firstDomino = self.getLessorValue(firstDomino)
        secondDomino = self.getLessorValue(secondDomino)

        if firstDomino.value == secondDomino.value:
            equal = True
        else:
            equal = False

        return equal

    #   Author: Samuel Bai
    #   Date: 05/13/2020
    #   Purpose: Overloads '!=' for Domino Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Domino != Other Domino
    # ================================================================
    def __ne__(self, other):
        firstDomino = self
        secondDomino = other

        firstDomino = self.getLessorValue(firstDomino)
        secondDomino = self.getLessorValue(secondDomino)

        if firstDomino.value != secondDomino.value:
            notEqual = True
        else:
            notEqual = False

        return notEqual


# MAIN
domino1 = Domino(value=22)
domino2 = Domino(value=51)
domino3 = Domino(value=22)

print("domino1 = %s" % domino1)
print("domino2 = %s" % domino2)
print("domino3 = %s" % domino3)

# Arithmetic Overloads
sum = domino1 + domino2
difference = domino1 - domino2
product = domino1 * domino2

print()
print("domino1 + domino2 = %s" % sum)
print("domino1 - domino2 = %s" % difference)
print("domino1 x domino2 = %s" % product)

# Relational Overloads
print()
if domino1 < domino2:
    print("domino1 < domino2")
elif domino1 > domino2:
    print("domino1 > domino2")

if domino1 != domino3:
    print("domino1 /= domino3")
elif domino1 == domino3:
    print("domino1 = domino3")

if domino2 >= domino3:
    print("domino2 >= domino3")
elif domino2 <= domino3:
    print("domino2 <= domino3")