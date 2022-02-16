# Author: Samuel Bai
# Date: 04/13/2020
# Purpose: OOP 1 - Question 2
#          Using Classes to Place Dominoes
# =================================================================

import random
from tkinter import *

userScreen = Tk()
userScreen.title("Domino")


# Author: Samuel Bai
# Date: 04/21/2020
# Purpose:
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


userScreen.resizable(0, 0)
varToggleFaceUp = BooleanVar()
varSelectValue1 = IntVar()
varSelectValue2 = IntVar()


# ====================================================================
# Author: Samuel Bai
# Date: 04/22/2020
# Purpose: Takes Keyboard Input to Create Dominoes
# Input: Keystrokes h/H or v/V
# Output: Domino Object on Canvas
# Dependencies: Domino Class
# ====================================================================
def keyPressed(event):
    sizeProperty = widSelectSize.get()
    faceProperty = varToggleFaceUp.get()

    value1 = varSelectValue1.get()
    value2 = varSelectValue2.get()
    valueProperty = value1 * 10 + value2

    if event.char == "h" or event.char == "H":
        myDomino = Domino(size=sizeProperty, value=valueProperty, faceUp=faceProperty)
        myDomino.draw(playBoard, random.randint(0, 440), random.randint(0, 540))

    elif event.char == "v" or event.char == "V":
        myDomino = Domino(size=sizeProperty, value=valueProperty, faceUp=faceProperty, orientation="V")
        myDomino.draw(playBoard, random.randint(0, 540), random.randint(0, 440))

    else:
        print('Invalid Input')


# ====================================================================
playBoard = Canvas(userScreen, width=640, height=640)
playBoard.config(background="green")
playBoard.bind("<Key>", keyPressed)
playBoard.focus_set()

widLabelRules = Label(userScreen, justify=LEFT, text="  Press: \n  h for Horizontal  \n  v for Vertical  ")

widLabelSize = Label(userScreen, text="Size:")
widSelectSize = Scale(userScreen, from_=30, to=100)

widToggleFaceUp = Checkbutton(userScreen, text="Face-Up", relief=GROOVE, bg="white", activebackground="white",
                              variable=varToggleFaceUp, width=7, onvalue=True, offvalue=False)

widSelectValue1 = Menubutton(userScreen, text="1st Value v", relief=GROOVE, bg="white", bd=2, activebackground="white",
                             width=10)
widSelectValue1.menu = Menu(widSelectValue1, tearoff=0)
widSelectValue1["menu"] = widSelectValue1.menu

widSelectValue1.menu.add_radiobutton(label="0", variable=varSelectValue1, value=0)
widSelectValue1.menu.add_radiobutton(label="1", variable=varSelectValue1, value=1)
widSelectValue1.menu.add_radiobutton(label="2", variable=varSelectValue1, value=2)
widSelectValue1.menu.add_radiobutton(label="3", variable=varSelectValue1, value=3)
widSelectValue1.menu.add_radiobutton(label="4", variable=varSelectValue1, value=4)
widSelectValue1.menu.add_radiobutton(label="5", variable=varSelectValue1, value=5)
widSelectValue1.menu.add_radiobutton(label="6", variable=varSelectValue1, value=6)

widSelectValue2 = Menubutton(userScreen, text="2nd Value v", relief=GROOVE, bg="white", bd=2, activebackground="white",
                             width=10)
widSelectValue2.menu = Menu(widSelectValue2, tearoff=0)
widSelectValue2["menu"] = widSelectValue2.menu

widSelectValue2.menu.add_radiobutton(label="0", variable=varSelectValue1, value=0)
widSelectValue2.menu.add_radiobutton(label="1", variable=varSelectValue2, value=1)
widSelectValue2.menu.add_radiobutton(label="2", variable=varSelectValue2, value=2)
widSelectValue2.menu.add_radiobutton(label="3", variable=varSelectValue2, value=3)
widSelectValue2.menu.add_radiobutton(label="4", variable=varSelectValue2, value=4)
widSelectValue2.menu.add_radiobutton(label="5", variable=varSelectValue2, value=5)
widSelectValue2.menu.add_radiobutton(label="6", variable=varSelectValue2, value=6)

widExit = Button(userScreen, text="Exit", relief=GROOVE, bg="white", activebackground="red", activeforeground="white",
                 width=9, command=lambda: userScreen.destroy())

# ====================================================================
playBoard.grid(row=0, column=1, rowspan=100)

widLabelRules.grid(row=0, column=2)

widLabelSize.grid(row=10, column=2)
widSelectSize.grid(row=11, column=2)

widToggleFaceUp.grid(row=30, column=2)
widSelectValue1.grid(row=40, column=2)
widSelectValue2.grid(row=41, column=2)

widExit.grid(row=95, column=2)

# ====================================================================
mainloop()
