# Author: Samuel Bai
# Date: 03/11/2020
# Purpose: GUI - Question 2
#          Using Tkinter to Create GUI for Star Patterns Assignment
# =================================================================

from tkinter import *

userScreen = Tk()


# Author: Samuel Bai
# Date: 04/01/2020
# Purpose: Outputs a Square Shape with Size Between 1-20
# Input: Size of Pattern, If Pattern is Hollow
# Output: Square Shape Pattern
# ====================================================================
def squarePattern(patternSize=1, patternHollow=False):
    stars = "\n"
    
    if patternHollow:
        for i in range(patternSize):

            if i == 0 or i == patternSize - 1:
                stars = stars + "* " * patternSize + "\n"

            else:
                spacingInner = "  " * (patternSize - 2)
                stars = stars + "* " + spacingInner + "*" + "\n"
    else:
        for i in range(patternSize):
            stars = stars + "* " * patternSize + "\n"

    return stars


# Author: Samuel Bai
# Date: 04/01/2020
# Purpose: Outputs a Right Triangle Shape with Size Between 1-20
# Input: Size of Pattern, If Pattern is Hollow
# Output: Right Triangle Shape Pattern
# ====================================================================
def trianglePattern(patternSize=1, patternHollow=False):
    stars = "\n"

    if patternHollow:
        for i in range(patternSize):

            if i == 0 or i == patternSize - 1:
                stars = stars + "* " * (i + 1) + "\n"

            else:
                spacingInner = "  " * (i - 1)
                stars = stars + "* " + spacingInner + "*" + "\n"
    else:
        for i in range(patternSize):
            stars = stars + "* " * (i + 1) + "\n"

    return stars


# Author: Samuel Bai
# Date: 04/01/2020
# Purpose: Outputs a Diamond Shape with Size Between 1-20
# Input: Size of Pattern, If Pattern is Hollow
# Output: Diamond Shape Pattern
# ====================================================================
def diamondPattern(patternSize=1, patternHollow=False):
    pattern = "\n"

    if patternSize % 2 == 0:
        return 'ERROR: The diamond size is even\nPlease choose an odd size for your pattern'

    if patternHollow:
        for i in range(patternSize):

            if i == 0 or i == patternSize - 1:
                spacingOuter = '  ' * (abs(patternSize // 2 - i))
                stars = '* ' * (patternSize - 2 * abs(patternSize // 2 - i))
                pattern = pattern + spacingOuter + stars + "\n"

            else:
                spacingOuter = '  ' * (abs(patternSize // 2 - i))
                spacingInner = '  ' * ((patternSize - 2 * abs(patternSize // 2 - i)) - 2)
                pattern = pattern + spacingOuter + '* ' + spacingInner + '*' + "\n"
    else:
        for i in range(patternSize):
            spacingOuter = '  ' * abs(patternSize // 2 - i)
            stars = '* ' * (patternSize - 2 * abs(patternSize // 2 - i))
            pattern = pattern + spacingOuter + stars + "\n"

    return pattern


# Author: Samuel Bai
# Date: 04/01/2020
# Purpose: Outputs a Cross(X) Shape with Size Between 1-20
# Input: Size of Pattern, If Pattern is Hollow
# Output: Cross(X) Shape Pattern
# ====================================================================
def crossPattern(patternSize=1, patternHollow=False):
    pattern = "\n"

    if patternHollow:
        for i in range(patternSize * 2 + 1):

            if i == 0 or i == patternSize * 2 or patternSize == 1:
                # Left side gap
                spacingLeft = patternSize - abs(patternSize - i)
                spacingLeftPrint = '  ' * spacingLeft

                # Left side of cross
                stars1 = patternSize
                stars1Print = ' *' * stars1

                # Middle gap
                spacingMid = abs((patternSize * 2) - (2 * i)) - patternSize
                if spacingMid < 0:
                    spacingMid = 0
                spacingMidPrint = '  ' * spacingMid

                # Right side of cross
                stars2 = patternSize
                if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 + 1) and spacingMid == 0:
                    stars2 = ((patternSize * 2) - (spacingLeft + stars1)) * 2
                stars2Print = ' *' * stars2

                pattern = pattern + spacingLeftPrint + stars1Print + spacingMidPrint + stars2Print + "\n"

            else:
                # Left side gap
                spacingLeft = patternSize - abs(patternSize - i)
                spacingLeftPrint = '  ' * spacingLeft

                # Left side of cross
                stars1 = patternSize
                stars1Print = ' *' + '  ' * (stars1 - 2) + ' *'

                # Middle gap
                spacingMid = abs((patternSize * 2) - (2 * i)) - patternSize
                if spacingMid < 0:
                    spacingMid = 0
                spacingMidPrint = '  ' * spacingMid

                # Right side of cross
                stars2 = patternSize
                if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 + 1) and spacingMid == 0:
                    stars2 = ((patternSize * 2) - (spacingLeft + stars1)) * 2

                # Right-mid of cross
                stars2Print = ' *' + '  ' * (stars2 - 2) + ' *'
                if patternSize % 2 == 0:
                    if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 - 1) and spacingMid == 0:
                        stars2Print = '  ' * (stars2 - 1) + ' *'
                else:
                    if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 + 1) and spacingMid == 0:
                        stars2Print = '  ' * (stars2 - 1) + ' *'

                # Left-mid of cross
                if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 - 1) and spacingMid == 0:
                    if i == patternSize:
                        stars1Print = ' *' + '  ' * (stars1 - 2)
                    else:
                        stars1Print = ' *' + '  ' * (stars1 - 1)

                pattern = pattern + spacingLeftPrint + stars1Print + spacingMidPrint + stars2Print + "\n"
    else:
        for i in range(patternSize * 2 + 1):
            # Left side gap
            spacingLeft = patternSize - abs(patternSize - i)
            spacingLeftPrint = '  ' * spacingLeft

            # Left side of cross
            stars1 = patternSize
            stars1Print = ' *' * stars1

            # Middle gap
            spacingMid = abs((patternSize * 2) - (2 * i)) - patternSize
            if spacingMid < 0:
                spacingMid = 0
            spacingMidPrint = '  ' * spacingMid

            # Right side of cross
            stars2 = patternSize
            if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 + 1) and spacingMid == 0:
                stars2 = ((patternSize * 2) - (spacingLeft + stars1)) * 2
            stars2Print = ' *' * stars2

            pattern = pattern + spacingLeftPrint + stars1Print + spacingMidPrint + stars2Print + "\n"

    return pattern


userScreen.resizable(0, 0)
varHollowToggle = BooleanVar()
varShapeSelect = StringVar()
objOutputPattern = StringVar()


# =================================================================
# Author: Samuel Bai
# Date: 04/06/2020
# Purpose: Clears the Pattern being Displayed
# Input: N/A
# Output: Blank String
# ====================================================================
def clearButtonClicked():
    objOutputPattern.set("")


# Author: Samuel Bai
# Date: 04/06/2020
# Purpose: Determines the Type of Pattern to Display, Based on User Input
# Input: N/A
# Output: Square, Triangle, Diamond, or Cross Pattern
# Dependencies: squarePattern(), trianglePattern(), diamondPattern(), crossPattern()
# ====================================================================
def displayButtonClicked():
    hollowProperty = varHollowToggle.get()
    shapeProperty = varShapeSelect.get()
    sizeProperty = widSelectSize.get()

    if shapeProperty == "square":
        shape = squarePattern(sizeProperty, hollowProperty)
        objOutputPattern.set(shape)

    elif shapeProperty == "triangle":
        shape = trianglePattern(sizeProperty, hollowProperty)
        objOutputPattern.set(shape)

    elif shapeProperty == "diamond":
        shape = diamondPattern(sizeProperty, hollowProperty)
        objOutputPattern.set(shape)

    elif shapeProperty == "cross":
        shape = crossPattern(sizeProperty, hollowProperty)
        objOutputPattern.set(shape)


# ====================================================================
widToggleHollow = Checkbutton(userScreen, text="Hollow", relief=GROOVE, bg="white", activebackground="white", width=8, variable=varHollowToggle, onvalue=True, offvalue=False)

widSelectShape = Menubutton(userScreen, text="Shape", relief=GROOVE, bg="white", bd=2, activebackground="white", width=12)
widSelectShape.menu = Menu(widSelectShape, tearoff=0)
widSelectShape["menu"] = widSelectShape.menu

widSelectShape.menu.add_radiobutton(label="Square", variable=varShapeSelect, value="square")
widSelectShape.menu.add_radiobutton(label="Triangle", variable=varShapeSelect, value="triangle")
widSelectShape.menu.add_radiobutton(label="Diamond", variable=varShapeSelect, value="diamond")
widSelectShape.menu.add_radiobutton(label="Cross", variable=varShapeSelect, value="cross")

widSelectSize = Scale(userScreen, from_=1, to=20)
widDisplayShape = Button(userScreen, text="Display Shape", relief=GROOVE, bg="white", activebackground="white", command=lambda: displayButtonClicked())

widLabelOutputShape = Label(userScreen, textvariable=objOutputPattern, relief=RIDGE, justify=LEFT, font='TkFixedFont', height=42, width=120)

widClear = Button(userScreen, text="Clear", relief=GROOVE, bg="white", activebackground="white", width=9, command=lambda: clearButtonClicked())
widExit = Button(userScreen, text="Exit", relief=GROOVE, bg="white", activebackground="red", activeforeground="white", width=9, command=lambda: userScreen.destroy())

# ====================================================================
widSelectShape.grid(row=1, column=1)
widToggleHollow.grid(row=2, column=1)
widSelectSize.grid(row=3, column=1)
widDisplayShape.grid(row=4, column=1)

widLabelOutputShape.grid(row=1, column=2, rowspan=106)

widClear.grid(row=105, column=3)
widExit.grid(row=106, column=3)

# ====================================================================
mainloop()