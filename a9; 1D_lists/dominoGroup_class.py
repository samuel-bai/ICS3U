# Author: Samuel Bai
# Date: 05/24/2020
# Purpose: 1D Lists - Question 2
#          Using Lists to Create Domino Groups
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

        self.diameter = self.size // 5
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

        self.diameter = self.size // 5
        self.gap = self.diameter // 2

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


# Author: Samuel Bai
# Date: 05/26/2020
# Purpose: Create Domino Groups
# Data Elements:
#   size >= 0; <= 7
#   dominoList = []
# Methods:
#   __init__: Initializes OBJECT
#   __str__: Prepares OBJECT for Print-Use
#   initDeal: Randomizes Each Domino in dominoList
#   calcTotal: Calculates Total Sum of Every Domino in dominoList
#   findLargest: Finds Largest Domino in dominoList
#   findPossible: Finds the First Domino Matching Given Value in dominoList
#   calcFreq: Finds the Frequency of a Given Domino in dominoList
#   insertAt: Inserts a Given Domino at a Given Position in dominoList
#   removeAt: Removes a Domino from a Given Position in dominoList
#   drawList: Draws All Dominoes in dominoList
#   setSize: Sets the Size of All Dominoes in dominoList
# Dependencies: Domino Class
# ====================================================================
class DominoGroup:
    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Initializes Class; Constructor
    #   Parameters: size
    #   Return/Output: DominoGroup Object
    # ================================================================
    def __init__(self, size=0):
        if size >= 0 and size <= 7:
            self.size = size
        else:
            self.size = 0

        initialList = []
        for i in range(0, self.size):
            randDomino = Domino()
            randDomino.randomize()
            initialList.append(randDomino)
        self.dominoList = initialList

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Convert and Prepares OBJECT for Print-Use
    #   Parameters: N/A
    #   Return/Output: String Conversion
    # ================================================================
    def __str__(self):
        outputList = []
        for i in range(self.size):
            outputList.append(self.dominoList[i].__str__())

        outputSize = self.size

        output = "%s size: %i" % (outputList, outputSize)

        return output

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Randomizes Each Domino in dominoList
    #   Parameters: N/A
    #   Return/Output: Random dominoList
    # ================================================================
    def initDeal(self):
        initialList = []

        for i in range(0, self.size):
            randDomino = Domino()
            randDomino.randomize()

            while randDomino in initialList:
                randDomino.randomize()

            initialList.append(randDomino)
        self.dominoList = initialList

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Finds the Sum of All Dominoes in dominoList
    #   Parameters: N/A
    #   Return/Output: Domino Sum
    # ================================================================
    def calcTotal(self):
        total = 0

        for i in range(self.size):
            total = total + (Domino(value=0) + self.dominoList[i])

        return total

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Finds Largest Domino in dominoList
    #   Parameters: N/A
    #   Return/Output: Largest Domino
    # ================================================================
    def findLargest(self):
        largest = self.dominoList[0]

        for i in range(1, self.size):
            if self.dominoList[i] > largest:
                largest = self.dominoList[i]

        return largest

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Finds the First Domino Matching Given Value in dominoList
    #   Parameters: value
    #   Return/Output: First Matching Domino
    # ================================================================
    def findPossible(self, value=0):
        valueFound = False

        for i in range(self.size):
            if not valueFound:
                if self.dominoList[i].value // 10 == value or self.dominoList[i].value % 10 == value:
                    valueFound = True
                    valueDomino = self.dominoList[i].value

                else:
                    valueDomino = -1

        return valueDomino

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Finds the Frequency of a Given Domino in dominoList
    #   Parameters: value
    #   Return/Output: Matching Domino Frequency
    # ================================================================
    def calcFreq(self, value=0):
        calcDomino = Domino(value=value)

        frequencyCount = 0
        for i in range(self.size):
            if calcDomino == self.dominoList[i]:
                frequencyCount = frequencyCount + 1

        return frequencyCount

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Inserts a Given Domino at a Given Position in dominoList
    #   Parameters: value, position
    #   Return/Output: Inserted Domino in dominoList
    # ================================================================
    def insertAt(self, value=0, position=1):
        insertionDomino = Domino(value=value)

        if position > 0 and position <= self.size:
            insertionPosition = position - 1
        else:
            insertionPosition = self.size

        self.dominoList.insert(insertionPosition, insertionDomino)
        self.size = len(self.dominoList)

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Removes a Domino from a Given Position in dominoList
    #   Parameters: position
    #   Return/Output: Removed Domino in dominoList
    # ================================================================
    def removeAt(self, position=1):
        if position > 0 and position <= self.size:
            deletionPosition = position - 1

            del self.dominoList[deletionPosition]

        self.size = len(self.dominoList)

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Draws All Dominoes in dominoList
    #   Parameters: canvas, x, y
    #   Return/Output: Horizontal Row of Dominoes in List
    # ================================================================
    def drawList(self, canvas, x, y):
        size = self.dominoList[0].size
        gap = self.dominoList[0].gap

        for i in range(self.size):
            self.dominoList[i].draw(canvas, x + i * (2 * size + gap), y)

    #   Author: Samuel Bai
    #   Date: 05/26/2020
    #   Purpose: Sets the Size of All Dominoes in dominoList
    #   Parameters: size
    #   Return/Output: New Size for Dominoes
    # ================================================================
    def setSize(self, size):
        for i in range(self.size):
            self.dominoList[i].setSize(size)


userScreen.resizable(0, 0)


# ====================================================================
# Author: Samuel Bai
# Date: 05/31/2020
# Purpose: Displays a Domino Group on the Canvas
# Input: N/A
# Output: Domino Group
# Dependencies: DominoGroup Class
# ====================================================================
def keyPressed(event):
    if event.char == "h" or event.char == "H":
        myGroup = DominoGroup(size=5)
        myGroup.initDeal()
        myGroup.setSize(random.randint(30, 100))
        myGroup.drawList(playBoard, random.randint(0, 440), random.randint(0, 540))

    else:
        print('Invalid Input')


# MAIN
# ====================================================================
# Size Setting, Group Drawing, Group Dealing
playBoard = Canvas(userScreen, width=1060, height=640)
playBoard.config(background="green")
playBoard.bind("<Key>", keyPressed)
playBoard.focus_set()
playBoard.pack()

# ====================================================================
mainloop()

# ====================================================================
firstDominoGroup = DominoGroup(size=5)
firstDominoGroup.initDeal()
print("firstDominoGroup: %s" % firstDominoGroup)

# Total Domino Value, Largest Domino Value
print()
dominoTotal = firstDominoGroup.calcTotal()
dominoLargest = firstDominoGroup.findLargest()
print("The sum of all Dominoes in List is %i" % dominoTotal)
print("The largest of all Dominoes in List is %s" % dominoLargest)

# Domino Insertion
print()
firstDominoGroup.insertAt(value=31, position=1)
print("firstDominoGroup: %s" % firstDominoGroup)

# Possibility of a Value in a List, Frequency of a Domino
print()
possibleValue = firstDominoGroup.findPossible(value=3)
dominoFrequency = firstDominoGroup.calcFreq(value=31)
print("first Domino containing a 3 is %s" % possibleValue)
print("there are %i Dominoes with a lessor value of 31 in List" % dominoFrequency)

# Domino Removal
print()
firstDominoGroup.removeAt(position=1)
print("firstDominoGroup: %s" % firstDominoGroup)