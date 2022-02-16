# Author: Samuel Bai
# Date: 05/12/2020
# Purpose: OOP 3 - Question 1
#          Using Overloaded Operators to Compare Dates
# =================================================================


# Author: Samuel Bai
# Date: 04/12/2020
# Purpose: Create Date Objects
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
#   getPositiveInteger: Asks User for Positive Integer
#   __gt__: Returns if One Date is > Other Date
#   __lt__: Returns if One Date is < Other Date
#   __ge__: Returns if One Date is >= Other Date
#   __le__: Returns if One Date is <= Other Date
#   __eq__: Returns if 2 Dates are Equal
#   __ne__: Returns if 2 Dates are Not Equal
#   __sub__: Returns Number of Days Between 2 Dates
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
            return True

        else:
            return False

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
            return True

        else:
            return False

    #   Author: Samuel Bai
    #   Date: 04/12/2020
    #   Purpose: Asks User for Month, Date, & Year
    #   Parameters: N/A
    #   Return/Output: Assigns Data Elements Month, Date, & Year
    # ================================================================
    def getDate(self):
        self.month = self.getPositiveInteger(1, 12, 'Enter a month ')
        self.date = self.getPositiveInteger(1, self.returnMaxDay(), 'Enter a date ')
        self.year = self.getPositiveInteger(1600, 2200, 'Enter a year ')

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
    #   Date: 05/12/2020
    #   Purpose: Overloads '>' for Date Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Date > Other Date
    # ================================================================
    def __gt__(self, other):
        if self.year > other.year:
            greaterThan = True
        elif self.year == other.year:
            if self.dayOfYear() > other.dayOfYear():
                greaterThan = True
            else:
                greaterThan = False
        else:
            greaterThan = False

        return greaterThan

    #   Author: Samuel Bai
    #   Date: 05/12/2020
    #   Purpose: Overloads '<' for Date Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Date < Other Date
    # ================================================================
    def __lt__(self, other):
        if self.year < other.year:
            lessThan = True
        elif self.year == other.year:
            if self.dayOfYear() < other.dayOfYear():
                lessThan = True
            else:
                lessThan = False
        else:
            lessThan = False

        return lessThan

    #   Author: Samuel Bai
    #   Date: 05/12/2020
    #   Purpose: Overloads '>=' for Date Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Date >= Other Date
    # ================================================================
    def __ge__(self, other):
        if self.year > other.year:
            greaterEqual = True
        elif self.year == other.year:
            if self.dayOfYear() >= other.dayOfYear():
                greaterEqual = True
            else:
                greaterEqual = False
        else:
            greaterEqual = False

        return greaterEqual

    #   Author: Samuel Bai
    #   Date: 05/12/2020
    #   Purpose: Overloads '<=' for Date Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Date <= Other Date
    # ================================================================
    def __le__(self, other):
        if self.year < other.year:
            lessEqual = True
        elif self.year == other.year:
            if self.dayOfYear() <= other.dayOfYear():
                lessEqual = True
            else:
                lessEqual = False
        else:
            lessEqual = False

        return lessEqual

    #   Author: Samuel Bai
    #   Date: 05/12/2020
    #   Purpose: Overloads '==' for Date Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Date == Other Date
    # ================================================================
    def __eq__(self, other):
        if self.year == other.year and \
                self.dayOfYear() == other.dayOfYear():
            equal = True
        else:
            equal = False

        return equal

    #   Author: Samuel Bai
    #   Date: 05/12/2020
    #   Purpose: Overloads '!=' for Date Class
    #   Parameters: N/A
    #   Return/Output: Boolean Value of One Date != Other Date
    # ================================================================
    def __ne__(self, other):
        if self.year != other.year or \
                self.dayOfYear() != other.dayOfYear():
            notEqual = True
        else:
            notEqual = False

        return notEqual

    #   Author: Samuel Bai
    #   Date: 05/12/2020
    #   Purpose: Overloads '-' for Date Class
    #   Parameters: N/A
    #   Return/Output: Number of Days Between 2 Dates
    # ================================================================
    def __sub__(self, other):
        daysBetween = 0

        if self.year > other.year or self.year < other.year:
            if self.year > other.year:
                daysBetween += other.dayOfYear()
                if self.returnLeapYear():
                    daysBetween += 366 - self.dayOfYear()
                else:
                    daysBetween += 365 - self.dayOfYear()

            else:
                daysBetween += self.dayOfYear()
                if other.returnLeapYear():
                    daysBetween += 366 - other.dayOfYear()
                else:
                    daysBetween += 365 - other.dayOfYear()

            for year in range(other.year, self.year):
                tempDate = Date(intYear=year)
                if tempDate.returnLeapYear():
                    daysBetween += 366
                else:
                    daysBetween += 365

        else:
            if other.dayOfYear() > self.dayOfYear():
                daysBetween += other.dayOfYear() - self.dayOfYear()
            else:
                daysBetween += self.dayOfYear() - other.dayOfYear()

        return daysBetween


# MAIN
# ====================================================================
firstDate = Date(intDay=20, intMonth=2, intYear=2019)
secondDate = Date(intDay=15, intMonth=1, intYear=1660)
thirdDate = Date(intDay=20, intMonth=2, intYear=2019)

print("firstDate = %s" % firstDate)
print("secondDate = %s" % secondDate)
print("thirdDate = %s" % thirdDate)

# Arithmetic Operator
difference = firstDate - secondDate

print()
print("firstDate - secondDate = %s days" % difference)

# Relational Operators
print()
if firstDate < secondDate:
    print("firstDate < secondDate")
elif firstDate > secondDate:
    print("firstDate > secondDate")

if firstDate != thirdDate:
    print("firstDate /= thirdDate")
elif firstDate == thirdDate:
    print("firstDate = thirdDate")

if secondDate >= thirdDate:
    print("secondDate >= thirdDate")
elif secondDate <= thirdDate:
    print("secondDate <= thirdDate")