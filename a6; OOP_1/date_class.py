# Author: Samuel Bai
# Date: 04/07/2020
# Purpose: OOP 1 - Question 1
#          Using Classes to Create an Interactive Calender
# =================================================================

from tkinter import *

userScreen = Tk()
userScreen.title("Calender")


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
# Date: 04/12/2020
# Purpose:
# Data Elements:
#   date = 1 - 31
#   month = 1 - 12
#   year = 1600 - 2200
# Methods:
#   __init__: Initializes OBJECT
#   returnMonthName: Returns Month Name from Integer
#   returnLeapYear: Checks if Year is Leap-Year
#   returnMaxDay: Returns # of Days in a Month & Year
#   calcZeller: Returns Integer from 0 - 6
#   returnDayName: Returns Weekday from Integer
#   calcValid: Boundary-Checks Month, Date, & Year Entered
#   getDate: Asks User for Month, Date, & Year
#   __str__: Prepares OBJECT for Print-Use
#   displayCalender: Prints and Returns a Calender of a Month & Year
# ====================================================================
class Date:
    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Initializes Class; Constructor
    #   Parameters: intDay, intMonth, intYear
    #   Return/Output: Date Object
    # ================================================================
    def __init__(self, intDay=1, intMonth=1, intYear=2019):
        self.date = intDay
        self.month = intMonth
        self.year = intYear

        validDate = self.calcValid()

        if not validDate:
            self.date = 1
            self.month = 1
            self.year = 2019

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Returns Month Corresponding to Integers 1 - 12
    #   Parameters: N/A
    #   Return/Output: Name of Month
    # ================================================================
    def returnMonthName(self):

        if self.month == 1:
            outputMonth = 'January'

        elif self.month == 2:
            outputMonth = 'February'

        elif self.month == 3:
            outputMonth = 'March'

        elif self.month == 4:
            outputMonth = 'April'

        elif self.month == 5:
            outputMonth = 'May'

        elif self.month == 6:
            outputMonth = 'June'

        elif self.month == 7:
            outputMonth = 'July'

        elif self.month == 8:
            outputMonth = 'August'

        elif self.month == 9:
            outputMonth = 'September'

        elif self.month == 10:
            outputMonth = 'October'

        elif self.month == 11:
            outputMonth = 'November'

        elif self.month == 12:
            outputMonth = 'December'

        return outputMonth

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Returns Boolean of Year is Leap-Year
    #   Parameters: N/A
    #   Return/Output: True if Leap-Year, False if Not
    # ================================================================
    def returnLeapYear(self):

        if self.year % 100 == 0 and self.year % 400 == 0 or self.year % 100 != 0 and self.year % 4 == 0:
            leapYear = True

        else:
            leapYear = False

        return leapYear

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Returns # of Days in a Month & Year
    #   Parameters: N/A
    #   Return/Output: Maximum Days in a Month of a Year
    # ================================================================
    def returnMaxDay(self):

        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            outputMaxDay = 31

        elif self.month in [4, 6, 9, 11]:
            outputMaxDay = 30

        elif self.month == 2:
            if self.returnLeapYear():
                outputMaxDay = 29
            else:
                outputMaxDay = 28

        return outputMaxDay

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Returns # of Days in a Month & Year
    #   Parameters: Date of Month
    #   Return/Output: Integer Value Between 0-6
    # ================================================================
    def calcZeller(self, date=1):
        m = self.month - 2
        y = self.year
        d = date

        if m <= 0:
            m = m + 12
            y = y - 1

        p = y // 100
        r = y % 100

        return (d + (26 * m - 2) // 10 + r + r // 4 + p // 4 + 5 * p) % 7

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Returns Weekday Corresponding to Integers 0 - 6
    #   Parameters: N/A
    #   Return/Output: Name of Weekday
    # ================================================================
    def returnDayName(self):
        intWeekday = self.calcZeller(self.date)

        if intWeekday == 0:
            strWeekday = 'Sunday'

        elif intWeekday == 1:
            strWeekday = 'Monday'

        elif intWeekday == 2:
            strWeekday = 'Tuesday'

        elif intWeekday == 3:
            strWeekday = 'Wednesday'

        elif intWeekday == 4:
            strWeekday = 'Thursday'

        elif intWeekday == 5:
            strWeekday = 'Friday'

        elif intWeekday == 6:
            strWeekday = 'Saturday'

        return strWeekday

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Boundary-Checks Month, Date, & Year Entered
    #   Parameters: N/A
    #   Return/Output: True if Data Arguments Valid, False if Not
    # ================================================================
    def calcValid(self):
        if self.month < 1 or self.month > 12:
            self.month = 1

        intMaxDay = self.returnMaxDay()
        if self.date >= 1 and self.date <= intMaxDay \
                and self.month >= 1 and self.month <= 12 \
                and self.year >= 1600 and self.year <= 2200:
            output = True

        else:
            output = False

        return output

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Asks User for Month, Date, & Year
    #   Parameters: N/A
    #   Return/Output: Assigns Data Elements Month, Date, & Year
    # ================================================================
    def getDate(self):
        self.month = getPositiveInteger(1, 12, 'Enter a month ')
        self.date = getPositiveInteger(1, self.returnMaxDay(), 'Enter a date ')
        self.year = getPositiveInteger(1600, 2200, 'Enter a year ')

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Convert and Prepares OBJECT for Print-Use
    #   Parameters: N/A
    #   Return/Output: String Conversion
    # ================================================================
    def __str__(self):
        weekday = self.returnDayName()
        month = self.returnMonthName()
        date = self.date
        year = self.year
        output = '%s, %i %s %i' % (weekday, date, month, year)

        return output

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Prints and Returns a Calender of a Month & Year
    #   Parameters: N/A
    #   Return/Output: String Calender
    # ================================================================
    def displayCalender(self):
        header = "         %9s  %-4s" % (self.returnMonthName(), self.year) + '\n'
        weekSubheader = "Sun  Mon  Tue  Wed  Thu  Fri  Sat \n"
        initialGap = "     " * self.calcZeller()
        calender = initialGap
        date = 1

        initialCount = self.calcZeller() + 1
        maxCount = self.returnMaxDay() + initialCount
        for i in range(initialCount, maxCount):
            calender = calender + "%3s  " % date
            date = date + 1

            if i % 7 == 0:
                calender = calender + "\n"

        return header + weekSubheader + calender

    #   Author: Samuel Bai
    #   Date: 04/13/2020
    #   Purpose: Returns Day of Year Based on Date
    #   Parameters: N/A
    #   Return/Output: Day of Year
    # ================================================================
    def dayOfYear(self):
        month = self.month
        day = self.date
        dayCount = 0

        for i in range(1, month):
            if i in [1, 3, 5, 7, 8, 10, 12]:
                dayCount = dayCount + 31

            elif i in [4, 6, 9, 11]:
                dayCount = dayCount + 30

            elif i == 2:
                if self.returnLeapYear():
                    dayCount = dayCount + 29
                else:
                    dayCount = dayCount + 28

        dayCount = dayCount + day

        return dayCount


userScreen.resizable(0, 0)
objDate = Date(1, 1, 1600)
objOutputDate = StringVar(value=objDate)
objOutputCalender = StringVar(value=objDate.displayCalender())


# ====================================================================
# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Adds 100 to Year Data Element
# Input: N/A
# Output: Year + 100, Date Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def addCentury():
    global objDate
    year = objDate.year
    date = objDate.date

    year += 100
    if year > 2200:
        year = 1600
    objDate.year = year

    if date > objDate.returnMaxDay():
        date = objDate.returnMaxDay()
    objDate.date = date

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Subtracts 100 from Year Data Element
# Input: N/A
# Output: Year - 100, Date Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def subCentury():
    global objDate
    year = objDate.year
    date = objDate.date

    year -= 100
    if year < 1600:
        year = 2200
    objDate.year = year

    if date > objDate.returnMaxDay():
        date = objDate.returnMaxDay()
    objDate.date = date

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Adds 10 to Year Data Element
# Input: N/A
# Output: Year + 10, Date Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def addDecade():
    global objDate
    year = objDate.year
    date = objDate.date

    year += 10
    if year > 2200:
        year = 1600
    objDate.year = year

    if date > objDate.returnMaxDay():
        date = objDate.returnMaxDay()
    objDate.date = date

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Subtracts 10 from Year Data Element
# Input: N/A
# Output: Year - 10, Date Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def subDecade():
    global objDate
    year = objDate.year
    date = objDate.date

    year -= 10
    if year < 1600:
        year = 2200
    objDate.year = year

    if date > objDate.returnMaxDay():
        date = objDate.returnMaxDay()
    objDate.date = date

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Adds 1 to Year Data Element
# Input: N/A
# Output: Year + 1, Date Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def addYear():
    global objDate
    year = objDate.year
    date = objDate.date

    year += 1
    if year > 2200:
        year = 1600
    objDate.year = year

    if date > objDate.returnMaxDay():
        date = objDate.returnMaxDay()
    objDate.date = date

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Subtracts 1 from Year Data Element
# Input: N/A
# Output: Year - 1, Date Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def subYear():
    global objDate
    year = objDate.year
    date = objDate.date

    year -= 1
    if year < 1600:
        year = 2200
    objDate.year = year

    if date > objDate.returnMaxDay():
        date = objDate.returnMaxDay()
    objDate.date = date

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Adds 1 to Month Data Element
# Input: N/A
# Output: Month + 1, Date Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def addMonth():
    global objDate
    month = objDate.month
    date = objDate.date

    month += 1
    if month > 12:
        month = 1
    objDate.month = month

    if date > objDate.returnMaxDay():
        date = objDate.returnMaxDay()
    objDate.date = date

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Subtracts 1 from Month Data Element
# Input: N/A
# Output: Month - 1, Date Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def subMonth():
    global objDate
    month = objDate.month
    date = objDate.date

    month -= 1
    if month < 1:
        month = 12
    objDate.month = month

    if date > objDate.returnMaxDay():
        date = objDate.returnMaxDay()
    objDate.date = date

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Adds 1 to Date Data Element
# Input: N/A
# Output: Date + 1, Date Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def addDay():
    global objDate
    date = objDate.date
    month = objDate.month
    year = objDate.year

    date += 1
    if date > objDate.returnMaxDay():
        month += 1

        if month > 12:
            month = 1
            year += 1
        objDate.month = month

        date = 1
    objDate.date = date

    if year > 2200:
        year = 1600
    objDate.year = year

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# Author: Samuel Bai
# Date: 04/14/2020
# Purpose: Subtracts 1 from Date Data Element
# Input: N/A
# Output: Date - 1, Month & Year Adjusted Accordingly
# Dependencies: objDate
# ====================================================================
def subDay():
    global objDate
    date = objDate.date
    month = objDate.month
    year = objDate.year

    date -= 1
    if date < 1:
        month -= 1

        if month < 1:
            month = 12
            year -= 1
        objDate.month = month

        date = objDate.returnMaxDay()
    objDate.date = date

    if year < 1600:
        year = 2200
    objDate.year = year

    objOutputDate.set(objDate)
    objOutputCalender.set(objDate.displayCalender())


# ====================================================================
widLabelDate = Label(userScreen, textvariable=objOutputDate, width=23)
widAddDay = Button(userScreen, text=">", relief=GROOVE, bg="white", activebackground="white", command=lambda: addDay())
widSubDay = Button(userScreen, text="<", relief=GROOVE, bg="white", activebackground="white", command=lambda: subDay())

widLabelCentury = Label(userScreen, text="Century")
widAddCentury = Button(userScreen, text=">", relief=GROOVE, bg="white", activebackground="white", command=lambda: addCentury())
widSubCentury = Button(userScreen, text="<", relief=GROOVE, bg="white", activebackground="white", command=lambda: subCentury())

widLabelDecade = Label(userScreen, text="Decade")
widAddDecade = Button(userScreen, text=">", relief=GROOVE, bg="white", activebackground="white", command=lambda: addDecade())
widSubDecade = Button(userScreen, text="<", relief=GROOVE, bg="white", activebackground="white", command=lambda: subDecade())

widLabelYear = Label(userScreen, text="Year")
widAddYear = Button(userScreen, text=">", relief=GROOVE, bg="white", activebackground="white", command=lambda: addYear())
widSubYear = Button(userScreen, text="<", relief=GROOVE, bg="white", activebackground="white", command=lambda: subYear())

widLabelMonth = Label(userScreen, text="Month")
widAddMonth = Button(userScreen, text=">", relief=GROOVE, bg="white", activebackground="white", command=lambda: addMonth())
widSubMonth = Button(userScreen, text="<", relief=GROOVE, bg="white", activebackground="white", command=lambda: subMonth())

widLabelCalender = Label(userScreen, textvariable=objOutputCalender, relief=RIDGE, justify=LEFT, anchor=N, font='TkFixedFont', height=8, width=38)

widSpacerLeft = Label(userScreen, textvariable="", width=1)
widSpacerRight = Label(userScreen, textvariable="", width=1)
widSpacerBottom = Label(userScreen, textvariable="")
widSpacerMiddle = Label(userScreen, textvariable="", width=1)

widExit = Button(userScreen, text="Exit", relief=GROOVE, bg="white", activebackground="red", activeforeground="white", width=7, command=lambda: userScreen.destroy())

# ====================================================================
widLabelDate.grid(row=1, column=2)
widAddDay.grid(row=1, column=3)
widSubDay.grid(row=1, column=1)

widLabelCalender.grid(row=2, column=1, rowspan=4, columnspan=3)

widLabelCentury.grid(row=1, column=6)
widAddCentury.grid(row=1, column=7)
widSubCentury.grid(row=1, column=5)

widLabelDecade.grid(row=2, column=6)
widAddDecade.grid(row=2, column=7)
widSubDecade.grid(row=2, column=5)

widLabelYear.grid(row=3, column=6)
widAddYear.grid(row=3, column=7)
widSubYear.grid(row=3, column=5)

widLabelMonth.grid(row=4, column=6)
widAddMonth.grid(row=4, column=7)
widSubMonth.grid(row=4, column=5)

widSpacerLeft.grid(row=1, column=0)
widSpacerRight.grid(row=1, column=8)
widSpacerBottom.grid(row=6, column=1)
widSpacerMiddle.grid(row=1, column=4)

widExit.grid(row=5, column=6)

# ====================================================================
mainloop()
