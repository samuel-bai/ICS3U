# Author: Samuel Bai
# Date: 06/08/2020
# Purpose: String & File Handling - Question 1
#          Using String Methods to Modify Text Files
# =================================================================
import os.path


# Author: Samuel Bai
# Date: 06/08/2020
# Purpose: Create Justified Text Files
# Data Elements:
#   wordsList = []
#   docList = []
#   strInputFile = .txt file
#   strOutputFile = .txt file name
#   strJustification = "l" / "r" / "c" / "f"
#   intWidth >=30; <= 90
# Methods:
#   __init__: Initializes OBJECT
#   readFile: Reads .txt file -- strInputFile
#   writeFile: Writes .txt file -- strOutputFile
#   createDoc: Calls Required Justification Based on strJustification
#   justifyLeft: Creates a String with Text Left Justified
#   justifyRight: Creates a String with Text Right Justified
#   justifyCentre: Creates a String with Text Centre Justified
#   justifyFull: Creates a String with Text Full Justified
#   __str__: Prepares OBJECT for Print-Use
#   getWordFreq: Generates a Word-Frequency Table
# Dependencies:
#   os.path Module
# ===================================================================
class JustifyText:
    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Initializes Class; Constructor
    #   Parameters: inputFile, outputFile, justification, width
    #   Return/Output: JustifyText Object
    # ================================================================
    def __init__(self, inputFile="input.txt", outputFile="output.txt", justification="l", width=60):
        self.wordsList = []
        self.docList = []

        self.strInputFile = inputFile
        self.strOutputFile = outputFile

        if justification in ["l", "r", "c", "f"]:
            self.strJustification = justification
        else:
            self.strJustification = "l"

        if str(width).isdigit():
            if width >= 30 and width <= 90:
                self.intWidth = width
            else:
                self.intWidth = 60
        else:
            self.intWidth = 60

        self.readFile()
        self.createDoc()

    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Reads .txt file -- self.strInputFile
    #   Parameters: N/A
    #   Return/Output: self.wordsList
    # ================================================================
    def readFile(self):
        if os.path.isfile(self.strInputFile):
            file = open(self.strInputFile, "r")

            for line in file:
                lineText = line.strip().split()

                for i in range(len(lineText)):
                    if len(lineText[i]) > 30:
                        lineText[i] = lineText[i][:29]

                self.wordsList = self.wordsList + lineText

            file.close()

        else:
            self.wordsList.append("ERROR: File not Found")

    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Writes .txt file -- strOutputFile
    #   Parameters: N/A
    #   Return/Output: .txt file
    # ================================================================
    def writeFile(self):
        file = open(self.strOutputFile, "w")
        file.write(self.__str__())
        file.close()

    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Calls Required Justification Based on strJustification
    #   Parameters: N/A
    #   Return/Output: Justified String
    # ================================================================
    def createDoc(self):
        if self.strJustification == "l":
            self.justifyLeft()

        elif self.strJustification == "r":
            self.justifyRight()

        elif self.strJustification == "c":
            self.justifyCentre()

        else:
            self.justifyFull()

    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Creates a String with Text Left Justified
    #   Parameters: N/A
    #   Return/Output: Left Justified String
    # ================================================================
    def justifyLeft(self):
        strLine = ""

        for i in range(len(self.wordsList)):
            if strLine == "":
                strLine = strLine + self.wordsList[i]

            else:
                if len(strLine) + len(self.wordsList[i]) + 1 <= self.intWidth:
                    strLine = strLine + " " + self.wordsList[i]
                else:
                    self.docList.append(strLine)
                    strLine = self.wordsList[i]

        self.docList.append(strLine)

    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Creates a String with Text Right Justified
    #   Parameters: N/A
    #   Return/Output: Right Justified String
    # ================================================================
    def justifyRight(self):
        self.justifyLeft()

        for i in range(len(self.docList)):
            rJustSpace = " " * (self.intWidth - len(self.docList[i]))
            self.docList[i] = rJustSpace + self.docList[i]

    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Creates a String with Text Centre Justified
    #   Parameters: N/A
    #   Return/Output: Centre Justified String
    # ================================================================
    def justifyCentre(self):
        self.justifyLeft()

        for i in range(len(self.docList)):
            self.docList[i] = self.docList[i].center(self.intWidth).rstrip()

    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Creates a String with Text Full Justified
    #   Parameters: N/A
    #   Return/Output: Full Justified String
    # ================================================================
    def justifyFull(self):
        self.justifyLeft()

        for i in range(len(self.docList) - 1):
            fJustSpaceCount = self.intWidth - len(self.docList[i])
            lineList = self.docList[i].split()
            for word in range(len(lineList) - 1):
                lineList[word] = lineList[word] + " "

            fullWord = 0
            while fJustSpaceCount != 0:
                lineList[fullWord] = lineList[fullWord] + " "
                fullWord = fullWord + 1

                if fullWord == len(lineList) - 1:
                    fullWord = 0

                fJustSpaceCount = fJustSpaceCount - 1

            fullLine = ""
            for word in lineList:
                fullLine = fullLine + word

            self.docList[i] = fullLine

    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Convert and Prepares OBJECT for Print-Use
    #   Parameters: N/A
    #   Return/Output: String Conversion
    # ================================================================
    def __str__(self):
        output = ""

        for i in range(len(self.docList)):
            output = output + self.docList[i] + "\n"

        return output

    #   Author: Samuel Bai
    #   Date: 06/08/2020
    #   Purpose: Generates a Word-Frequency Table
    #   Parameters: N/A
    #   Return/Output: Word-Frequency Table
    # ================================================================
    def getWordFreq(self):
        uniqueWordSet = set(self.wordsList)
        uniqueWordList = list(uniqueWordSet)
        wordFreqOutput = "\n Word Frequency: \n"

        for word in range(len(uniqueWordList) - 1):
            keyword = "".join(e for e in uniqueWordList[word] if e.isalnum()).lower()
            wordFreq = self.wordsList.count(keyword)
            wordFreqOutput = wordFreqOutput + "     %s - %i \n" % (keyword, wordFreq)

        file = open(self.strOutputFile, "a")
        file.write(wordFreqOutput)
        file.close()

        return wordFreqOutput


# MAIN
# =================================================================
justifyFile = JustifyText(inputFile="input.txt", justification="r", width=90)
justifyFile.writeFile()
wordFreq = justifyFile.getWordFreq()
print(justifyFile)
print(wordFreq)
