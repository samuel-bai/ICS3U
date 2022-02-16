# Author: Samuel Bai
# Date: 04/25/2020
# Purpose: OOP 2 - Question 1
#          Using Class Composition to Make Domino Hands
# =================================================================

import random
from tkinter import *

userScreen = Tk()
userScreen.title("Domino Hand")


# Author: Samuel Bai
# Date: 04/21/2020
# Purpose: To Create a Domino Object
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
    #   Input: Positive Integer
    #   Output: Positive Integer that Passes Boundary + Type Check
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


# Author: Samuel Bai
# Date: 04/30/2020
# Purpose:
# Data Elements:
#   size = 30 - 100
#   firstDomino = Domino Object
#   secondDomino = Domino Object
#   thirdDomino = Domino Object
# Methods:
#   __init__: Initializes OBJECT
#   __str__: Prepares OBJECT for Print-Use
#   setSize: Changes size using Parameter
#   sort: Organizes Dominoes from smallest to largest value
#   roll: Randomizes the value of the 3 Dominoes
#   draw: Draws 3 Dominoes Arranged in a line
#   getRun: Determines the Run of the Domino Hand
# Dependencies: Domino Class
# ====================================================================
class Hand:
    #   Author: Samuel Bai
    #   Date: 04/30/2020
    #   Purpose: Initializes Class; Constructor
    #   Parameters: size
    #   Return/Output: Domino Hand Object
    # ================================================================
    def __init__(self, size=30):
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 60

        self.firstDomino = Domino(size=self.size)
        self.secondDomino = Domino(size=self.size)
        self.thirdDomino = Domino(size=self.size)

    #   Author: Samuel Bai
    #   Date: 04/30/2020
    #   Purpose: Convert and Prepares OBJECT for Print-Use
    #   Parameters: N/A
    #   Return/Output: String Conversion
    # ================================================================
    def __str__(self):
        firstDomino = self.firstDomino.__str__()
        secondDomino = self.secondDomino.__str__()
        thirdDomino = self.thirdDomino.__str__()

        output = "%s - %s - %s" % (firstDomino, secondDomino, thirdDomino)

        return output

    #   Author: Samuel Bai
    #   Date: 04/30/2020
    #   Purpose: Changes size using Parameter
    #   Parameters: size
    #   Return/Output: Domino Hand size
    # ================================================================
    def setSize(self, size=60):
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 60

        self.firstDomino.setSize(size=size)
        self.secondDomino.setSize(size=size)
        self.thirdDomino.setSize(size=size)

    #   Author: Samuel Bai
    #   Date: 04/30/2020
    #   Purpose: Organizes Dominoes by value from Left to Right
    #            Smallest to Largest
    #   Parameters: N/A
    #   Return/Output: Reorganized Domino Hand
    # ================================================================
    def sort(self):
        value1 = self.firstDomino.value
        value2 = self.secondDomino.value
        value3 = self.thirdDomino.value

        values = [value1, value2, value3]
        values.sort()

        self.firstDomino.value = values[0]
        self.secondDomino.value = values[1]
        self.thirdDomino.value = values[2]

    #   Author: Samuel Bai
    #   Date: 04/30/2020
    #   Purpose: Randomizes Domino Values
    #   Parameters: N/A
    #   Return/Output: Domino Hand with Randomized Values
    # ================================================================
    def roll(self):
        self.firstDomino.randomize()
        self.secondDomino.randomize()
        self.thirdDomino.randomize()

    #   Author: Samuel Bai
    #   Date: 04/22/2020
    #   Purpose: Draws Domino Hand by Calling Domino.draw() Three Times
    #   Parameters: canvas, x, y
    #   Return/Output: Domino Hand Object
    # ================================================================
    def draw(self, canvas, x=60, y=30):
        gap = self.size // 10

        self.firstDomino.draw(canvas, x, y)
        self.secondDomino.draw(canvas, x + 2 * self.size + gap, y)
        self.thirdDomino.draw(canvas, x + 2 * (2 * self.size + gap), y)

    #   Author: Samuel Bai
    #   Date: 04/30/2020
    #   Purpose: Calculates the Run of the Domino Hand
    #   Parameters: N/A
    #   Return/Output: Run Value (0, 2, 3)
    # ================================================================
    def getRun(self):
        firstDominoRun = [self.firstDomino.value // 10, self.firstDomino.value % 10]
        secondDominoRun = [self.secondDomino.value // 10, self.secondDomino.value % 10]
        thirdDominoRun = [self.thirdDomino.value // 10, self.thirdDomino.value % 10]

        if firstDominoRun[0] in secondDominoRun and firstDominoRun[1] in thirdDominoRun or \
                firstDominoRun[1] in secondDominoRun and firstDominoRun[0] in thirdDominoRun or \
                secondDominoRun[0] in firstDominoRun and secondDominoRun[1] in thirdDominoRun or \
                secondDominoRun[1] in firstDominoRun and secondDominoRun[0] in thirdDominoRun or \
                thirdDominoRun[0] in firstDominoRun and thirdDominoRun[1] in secondDominoRun or \
                thirdDominoRun[1] in firstDominoRun and thirdDominoRun[0] in secondDominoRun:
            run = 3

        elif firstDominoRun[0] in secondDominoRun or firstDominoRun[1] in secondDominoRun or \
                secondDominoRun[0] in thirdDominoRun or secondDominoRun[1] in thirdDominoRun or \
                thirdDominoRun[0] in firstDominoRun or thirdDominoRun[1] in firstDominoRun:
            run = 2

        else:
            run = 0

        return run


userScreen.resizable(0, 0)
runVar = StringVar(value="Run: \n ")
runsVar = StringVar(value="Runs: \n0 \n2 \n3 \nTotal")


# ====================================================================
# Author: Samuel Bai
# Date: 04/30/2020
# Purpose: Displays a Domino Hand on the Canvas
# Input: N/A
# Output: Domino Hand
# Dependencies: Domino Class
# ====================================================================
def displayButtonClicked():
    sizeProperty = widSelectSize.get()

    myHand = Hand(size=sizeProperty)

    xLocationProperty = widSelectX.get()
    y1LocationProperty = widSelectY.get()
    y2LocationProperty = y1LocationProperty + myHand.size + (myHand.size // 10)

    myHand.roll()
    myHand.draw(playBoard, xLocationProperty, y1LocationProperty)

    myHand.sort()
    myHand.draw(playBoard, xLocationProperty, y2LocationProperty)

    run = "Run: \n" + str(myHand.getRun())

    runVar.set(run)


# Author: Samuel Bai
# Date: 04/30/2020
# Purpose: Display the Run Results of 10K Domino Hands
# Input: N/A
# Output: Run Results of 10K Domino Hands
# Dependencies: Domino Class
# ====================================================================
def simulateButtonClicked():
    run0 = 0
    run2 = 0
    run3 = 0
    myHand = Hand()

    for i in range(10000):
        myHand.roll()
        run = myHand.getRun()

        if run == 0:
            run0 += 1

        elif run == 2:
            run2 += 1

        elif run == 3:
            run3 += 1

    percentRun0 = run0 / 100
    percentRun2 = run2 / 100
    percentRun3 = run3 / 100

    displayPercentRun0 = "%0.2f" % percentRun0 + "%"
    displayPercentRun2 = "%0.2f" % percentRun2 + "%"
    displayPercentRun3 = "%0.2f" % percentRun3 + "%"

    percentTotal = str(percentRun0 + percentRun2 + percentRun3) + "%"

    outputStr = "Runs: \n0 %10s \n2 %10s \n3 %10s \nTotal %6s" % (displayPercentRun0, displayPercentRun2, displayPercentRun3, percentTotal)

    runsVar.set(outputStr)


# ====================================================================
playBoard = Canvas(userScreen, width=1060, height=640)
playBoard.config(background="green")

widLabelSize = Label(userScreen, text="Size:")
widSelectSize = Scale(userScreen, from_=30, to=100)

widLabelX = Label(userScreen, text="X Coordinate:")
widSelectX = Scale(userScreen, from_=20, to=420)

widLabelY = Label(userScreen, text="Y Coordinate:")
widSelectY = Scale(userScreen, from_=20, to=420)

widDisplayHand = Button(userScreen, text="Display Shape", relief=GROOVE, bg="white", activebackground="white", command=lambda: displayButtonClicked())
widLabelRun = Label(userScreen, textvariable=runVar, justify=LEFT, font='TkFixedFont')

widSimulate10K = Button(userScreen, text="Simulate 10K Runs", relief=GROOVE, bg="white", activebackground="white", command=lambda: simulateButtonClicked())
widLabelRuns = Label(userScreen, textvariable=runsVar, justify=LEFT, width=12, anchor=W, font='TkFixedFont')

widExit = Button(userScreen, text="Exit", relief=GROOVE, bg="white", activebackground="red", activeforeground="white", width=9, command=lambda: userScreen.destroy())

# ====================================================================
playBoard.grid(row=1, column=1, rowspan=100)

widLabelSize.grid(row=1, column=2)
widSelectSize.grid(row=2, column=2)

widLabelX.grid(row=11, column=2)
widSelectX.grid(row=12, column=2)

widLabelY.grid(row=21, column=2)
widSelectY.grid(row=22, column=2)

widDisplayHand.grid(row=31, column=2)
widLabelRun.grid(row=41, column=2)

widSimulate10K.grid(row=61, column=2)
widLabelRuns.grid(row=71, column=2)

widExit.grid(row=91, column=2)

# ====================================================================
mainloop()