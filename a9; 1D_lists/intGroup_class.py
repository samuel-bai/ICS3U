# Author: Samuel Bai
# Date: 05/24/2020
# Purpose: 1D Lists - Question 1
#          Using Lists to Create Integer Groups
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
# ===================================================================
class IntGroup:
    #   Author: Samuel Bai
    #   Date: 05/27/2020
    #   Purpose: Initializes Class; Constructor
    #   Parameters: size
    #   Return/Output: IntGroup Object
    # ================================================================
    def __init__(self, size=0):
        if str(size).isdigit() and (size >= 0 and size <= 20):
            self.size = size
        else:
            self.size = 0

        initialList = []
        for i in range(0, self.size):
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


# MAIN
# ===================================================================
# Create Objects
firstIntGroup = IntGroup(size=15)
secondIntGroup = IntGroup(size=20)
print("firstIntGroup: %s" % firstIntGroup)
print("secondIntGroup: %s" % secondIntGroup)

# Insert, Find First, Delete
print()
firstIntGroup.insertAt(value=10, position=2)
print("firstIntGroup: %s" % firstIntGroup)
first10 = firstIntGroup.findFirst(value=10)
print("The first 10 is at position: %i" % first10)
firstIntGroup.removeAt(position=2)
print("firstIntGroup: %s" % firstIntGroup)

# Calculate Frequency of 3, Remove All 3s
print()
numOf3 = firstIntGroup.calcFreq(value=3)
print("There are %i 3s" % numOf3)
firstIntGroup.removeAll(value=3)
print("firstIntGroup: %s" % firstIntGroup)

# Check if List is Sorted, Initializes List as Sequence, Checks Again
print()
if secondIntGroup.isSorted():
    print("secondIntGroup is Sorted")
else:
    print("secondIntGroup is not Sorted")
print()

secondIntGroup.initAsSequence(size=20)
print("secondIntGroup: %s" % secondIntGroup)

print()
if secondIntGroup.isSorted():
    print("secondIntGroup is Sorted")
else:
    print("secondIntGroup is not Sorted")

# Largest Value
print()
secondLargest = secondIntGroup.findLargest()
print("The largest value is %i" % secondLargest)

# List Merging, Calculating Total and Mean
print()
firstIntGroup.intList.sort()
mergedIntGroup = firstIntGroup.merge(other=secondIntGroup)
print("mergedIntGroup of the 2 IntGroups: %s" % mergedIntGroup)
mergedTotal = mergedIntGroup.calcTotal()
mergedMean = mergedIntGroup.calcMean()
print("mergedIntGroup has a total of %i and an average of %i" % (mergedTotal, mergedMean))

# Initializes List as Integer
print()
thirdIntGroup = IntGroup()
thirdIntGroup.initAsNum(size=10, num=15)
print("thirdIntGroup: %s" % thirdIntGroup)