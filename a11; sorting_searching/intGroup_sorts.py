# Author: Samuel Bai
# Date: 06/13/2020
# Purpose: Searching & Sorting - Question 1
#          Using Searches & Sorts to Manipulate IntGroup
# =================================================================
import random


# Author: Samuel Bai
# Date: 05/27/2020
# Purpose: Create Integer Groups
# Data Elements:
#   size >= 0; <= 20
#   intList = []
# Methods:
#   __init__: Initializes OBJECT
#   __str__: Prepares OBJECT for Print-Use
#   initAsNum: Initializes intList with all Values Same
#   initAsSequence: Initializes intList with all Values in Ascending Sequence
#   initAsRandom: Initializes intList with all Values Random
#   calcTotal: Calculates Total Sum of Every Value in intList
#   calcMean: Calculates Mean of Values in intList
#   findLargest: Finds Largest Value in intList
#   calcFreq: Finds the Frequency of a Given Value in intList
#   insertAt: Inserts a Given Value at a Given Position in intList
#   removeAt: Removes a Value from a Given Position in intList
#   removeAll: Removes all of a Value from intList
#   findFirst: Finds First Occurrence of Given Value
#   isSorted: Checks if intList is Sorted in Ascending Order
#   merge: Combines 2 Sorted intGroups into 1 in Ascending Order
#   linearSearch: Searches intList for Value using a Linear Search
#   sentinelSearch: Searches intList for Value using a Sentinel Search
#   binarySearch: Searches sorted intList for Value using a Binary Search
#   exchangeSort: Sorts intList using an Exchange Sort
#   selectionSort: Sorts intList using a Selection Sort
#   insertionSort: Sorts intList using an Insertion Sort
# ===================================================================
class IntGroup:
    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Initializes Class; Constructor
    #   Parameters: size
    #   Return/Output: IntGroup Object
    #   Dependencies: random Module
    # ================================================================
    def __init__(self, size=0):
        if str(size).isdigit() and (size >= 0 and size <= 20):
            self.size = size
        else:
            self.size = 0

        initialList = []
        for i in range(self.size):
            randInt = random.randint(0, size)
            initialList.append(randInt)
        self.intList = initialList

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Convert and Prepares OBJECT for Print-Use
    #   Parameters: N/A
    #   Return/Output: String Conversion
    # ================================================================
    def __str__(self):
        output = "%s size: %i" % (self.intList, self.size)

        return output

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Initializes intList with all Values Same
    #   Parameters: size, num
    #   Return/Output: intList with Same Value Throughout
    # ================================================================
    def initAsNum(self, size=0, num=0):
        if str(size).isdigit() and (size >= 0 and size <= 20):
            self.size = size
        else:
            self.size = 0

        if str(num).isdigit() and (num >= 0 and num <= 10000):
            appendNum = num
        else:
            appendNum = 0

        initialList = []
        for i in range(0, self.size):
            initialList.append(appendNum)
        self.intList = initialList

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Initializes intList with all Values in Ascending Sequence
    #   Parameters: size
    #   Return/Output: intList with Ascending Values
    # ================================================================
    def initAsSequence(self, size=0):
        if str(size).isdigit() and (size >= 0 and size <= 20):
            self.size = size
        else:
            self.size = 0

        initialList = []
        initialList.extend(range(1, self.size + 1))
        self.intList = initialList

    #   Author: Samuel Bai
    #   Date: 06/13/2020
    #   Purpose: Initializes intList with all Values Random
    #   Parameters: size
    #   Return/Output: intList with Random Values
    #   Dependencies: random Module
    # ================================================================
    def initAsRandom(self, size=0):
        if str(size).isdigit() and (size >= 0 and size <= 20):
            self.size = size
        else:
            self.size = 0

        initialList = []
        for i in range(self.size):
            randInt = random.randint(0, size)
            initialList.append(randInt)
        self.intList = initialList

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Finds the Sum of All Values in intList
    #   Parameters: N/A
    #   Return/Output: Value Sum
    # ================================================================
    def calcTotal(self):
        total = sum(self.intList)

        return total

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Finds the Mean of All Values in intList
    #   Parameters: N/A
    #   Return/Output: Mean of List
    # ================================================================
    def calcMean(self):
        meanTotal = self.calcTotal()
        meanSize = self.size

        if meanSize != 0:
            mean = meanTotal / meanSize

            if mean == int(mean):
                mean = int(mean)

        else:
            mean = 0

        return mean

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Finds Greatest Values in intList
    #   Parameters: N/A
    #   Return/Output: Greatest Value
    # ================================================================
    def findLargest(self):
        largest = max(self.intList)

        return largest

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Finds the Frequency of a Given Value in intList
    #   Parameters: num
    #   Return/Output: Value Frequency
    # ================================================================
    def calcFreq(self, value=0):
        frequency = self.intList.count(value)

        return frequency

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Inserts a Given Value at a Given Position in intList
    #   Parameters: value, position
    #   Return/Output: Inserted Domino in dominoList
    # ================================================================
    def insertAt(self, value=0, position=1):
        if str(value).isdigit() and value >= 0:
            insertionValue = value
        else:
            insertionValue = 0

        if str(position).isdigit() and (position > 0 and position <= self.size):
            insertionPosition = position - 1
        else:
            insertionPosition = self.size

        self.intList.insert(insertionPosition, insertionValue)
        self.size = len(self.intList)

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Removes a Value from a Given Position in intList
    #   Parameters: position
    #   Return/Output: Removed Value in intList
    # ================================================================
    def removeAt(self, position=1):
        if str(position).isdigit() and (position > 0 and position <= self.size):
            deletionPosition = position - 1

            del self.intList[deletionPosition]

        self.size = len(self.intList)

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Removes all of a Value in intList
    #   Parameters: value
    #   Return/Output: Removed Value/s in intList
    # ================================================================
    def removeAll(self, value=0):
        if str(value).isdigit():
            for i in range(0, self.intList.count(value)):
                self.intList.remove(value)

        self.size = len(self.intList)

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Finds First Occurrence of Given Value
    #   Parameters: value
    #   Return/Output: Position of First Occurrence of a Value
    # ================================================================
    def findFirst(self, value=0):
        if str(value).isdigit() and value in self.intList:
            firstValue = self.intList.index(value) + 1

        else:
            firstValue = -1

        return firstValue

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Checks if intList is Sorted in Ascending Order
    #   Parameters: N/A
    #   Return/Output: Boolean of if intList is Sorted
    # ================================================================
    def isSorted(self):
        sortedProperty = True
        for i in range(self.size - 1):
            if sortedProperty and self.intList[i + 1] >= self.intList[i]:
                sortedProperty = True

            else:
                sortedProperty = False

        return sortedProperty

    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Combines 2 Sorted intGroups into 1 in Ascending Order
    #   Parameters: other
    #   Return/Output: Merged intGroup
    # ================================================================
    def merge(self, other):  # cannot call the class in params
        mergedList = IntGroup()
        mergedFirst = self.intList.copy()
        mergedSecond = other.intList.copy()

        if self.isSorted() and other.isSorted():
            while len(mergedFirst) > 0 or len(mergedSecond) > 0:
                if len(mergedFirst) > 0 and len(mergedSecond) > 0:
                    if mergedFirst[0] <= mergedSecond[0]:
                        addedValue = mergedFirst.pop(0)

                    else:
                        addedValue = mergedSecond.pop(0)

                elif len(mergedFirst) > 0 and len(mergedSecond) <= 0:
                    addedValue = mergedFirst.pop(0)

                elif len(mergedFirst) <= 0 and len(mergedSecond) > 0:
                    addedValue = mergedSecond.pop(0)

                mergedList.intList.append(addedValue)

        mergedList.size = len(mergedList.intList)

        return mergedList

    #   Author: Samuel Bai
    #   Date: 06/13/2020
    #   Purpose: Searches intList for Value using a Linear Search
    #   Parameters: value
    #   Return/Output: Position of Value (-1 if inexistent)
    # ================================================================
    def linearSearch(self, value=0):
        found = False

        for i in range(self.size):
            if not found and self.intList[i] == value:
                found = True
                position = i

        if not found:
            position = -1

        return position

    #   Author: Samuel Bai
    #   Date: 06/13/2020
    #   Purpose: Searches intList for Value using a Sentinel Search
    #   Parameters: value
    #   Return/Output: Position of Value (-1 if inexistent)
    # ================================================================
    def sentinelSearch(self, value=0):
        self.intList.append(value)
        sentinelPosition = self.intList[-1]

        i = 0
        while self.intList[i] != value:
            i = i + 1

        if i == sentinelPosition:
            position = -1
        else:
            position = i

        self.intList.pop()

        return position

    #   Author: Samuel Bai
    #   Date: 06/13/2020
    #   Purpose: Searches sorted intList for Value using a Binary Search
    #   Parameters: value, listMin, listMax, order
    #   Return/Output: Position of Value (-1 if inexistent or -2 if unsorted)
    # ================================================================
    def binarySearch(self, value=0, listMin=0, listMax=0, order="ASCENDING"):
        if self.isSorted():

            if listMax >= listMin:
                listMid = (listMin + listMax) // 2

                if value == self.intList[listMid]:
                    position = listMid

                elif value > self.intList[listMid]:
                    if order == "DESCENDING":
                        position = self.binarySearch(value=value, listMin=listMin, listMax=listMid - 1, order=order)
                    else:
                        position = self.binarySearch(value=value, listMin=listMid + 1, listMax=listMax)

                elif value < self.intList[listMid]:
                    if order == "DESCENDING":
                        position = self.binarySearch(value=value, listMin=listMid + 1, listMax=listMax, order=order)
                    else:
                        position = self.binarySearch(value=value, listMin=listMin, listMax=listMid - 1)

                else:
                    position = -1

        else:
            position = -2  # Return if unsorted

        return position

    #   Author: Samuel Bai
    #   Date: 06/13/2020
    #   Purpose: Sorts intList using an Exchange Sort
    #   Parameters: order
    #   Return/Output: Sorted intList
    # ================================================================
    def exchangeSort(self, order="ASCENDING"):

        for i in range(self.size - 1, 0, -1):
            for j in range(i):
                if order == "DESCENDING":
                    if self.intList[j] < self.intList[j + 1]:
                        self.intList[j], self.intList[j + 1] = self.intList[j + 1], self.intList[j]

                else:
                    if self.intList[j] > self.intList[j + 1]:
                        self.intList[j], self.intList[j + 1] = self.intList[j + 1], self.intList[j]

    #   Author: Samuel Bai
    #   Date: 06/13/2020
    #   Purpose: Sorts intList using a Selection Sort
    #   Parameters: order
    #   Return/Output: Sorted intList
    # ================================================================
    def selectionSort(self, order="ASCENDING"):
        for i in range(self.size):
            keyPosition = i

            for j in range(i + 1, self.size):
                if order == "DESCENDING":
                    if self.intList[keyPosition] > self.intList[j]:
                        keyPosition = j

                else:
                    if self.intList[keyPosition] < self.intList[j]:
                        keyPosition = j

            self.intList[i], self.intList[keyPosition] = self.intList[keyPosition], self.intList[i]

    #   Author: Samuel Bai
    #   Date: 06/13/2020
    #   Purpose: Sorts intList using an Insertion Sort
    #   Parameters: order
    #   Return/Output: Sorted intList
    # ================================================================
    def insertionSort(self, order="ASCENDING"):
        for i in range(1, self.size):
            keyValue = self.intList[i]
            j = i - 1

            if order == "DESCENDING":
                while j >= 0 and keyValue > self.intList[j]:
                    self.intList[j + 1] = self.intList[j]
                    j = j - 1

            else:
                while j >= 0 and keyValue < self.intList[j]:
                    self.intList[j + 1] = self.intList[j]
                    j = j - 1

            self.intList[j + 1] = keyValue


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Asks for a Positive Integer; Boundary + Type Check
# Input: Positive Integer
# Output: Positive Integer that Passes Boundary + Type Check
# ====================================================================
def getPositiveInteger(low=0, high=100, prompt='Enter an integer '):
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


# MAIN
# ===================================================================
firstList = IntGroup()
firstList.initAsRandom(size=15)
print("firstList; %s" % firstList)

print()
methodOption = input("Type SORT or SEARCH as intended: ").upper()
while methodOption not in ["SORT", "SEARCH"]:
    print()
    print("ERROR: Invalid Input")
    methodOption = input("Type SORT or SEARCH as intended: ").upper()

print()

if methodOption == "SORT":
    sortOption = input("Type EXCHANGE, SELECTION, or INSERTION as intended: ").upper()
    while sortOption not in ["EXCHANGE", "SELECTION", "INSERTION"]:
        print()
        print("ERROR: Invalid Input")
        sortOption = input("Type EXCHANGE, SELECTION, or INSERTION as intended: ").upper()

    sortOrder = input("Type ASCENDING or DESCENDING as intended: ").upper()

    if sortOption == "EXCHANGE":
        firstList.exchangeSort(order=sortOrder)
    elif sortOption == "SELECTION":
        firstList.selectionSort(order=sortOrder)
    else:
        firstList.insertionSort(order=sortOrder)
    print()
    print("Sorted List; %s" % firstList)

else:
    searchOption = input("Type LINEAR, SENTINEL, or BINARY as intended: ").upper()
    while searchOption not in ["LINEAR", "SENTINEL", "BINARY"]:
        print()
        print("ERROR: Invalid Input")
        searchOption = input("Type LINEAR, SENTINEL, or BINARY as intended: ").upper()

    searchValue = getPositiveInteger(high=50)

    if searchOption == "LINEAR":
        valuePosition = firstList.linearSearch(value=searchValue)
    elif searchOption == "SENTINEL":
        valuePosition = firstList.sentinelSearch(value=searchValue)
    else:
        searchOrder = input("Type ASCENDING or DESCENDING as intended: ").upper()
        valuePosition = firstList.binarySearch(value=searchValue, order=searchOrder)
    print()
    print("Value Position at index[%i]" % valuePosition)
