# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Functions - Question 2
#          Using Functions to play a game of Red Dog
# ==================================================

from random import *
from sys import *

class TwoCard:

    def __init__(self, a=2, b=2):
        self.value1 = a

        self.value2 = b


# Author: Samuel Bai
# Date: 03/04/2020
# Purpose: Asks for a Positive Integer; Boundary + Type Check
# Input: Positive Integer
# Output: Positive Integer that Passes Boundary + Type Check
# ====================================================================
def getPositiveInteger(low=1, high=100, prompt='Enter a positive integer '):
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
# Date: 03/05/2020
# Purpose: Outputs a Random Positive Integer Between 2-14
# Input: None
# Output: Positive Integer Between 2-14
# Dependencies: Random Module
# ====================================================================
def getCard():
    intRandCard = randint(2, 14)

    return intRandCard


# Author: Samuel Bai
# Date: 03/05/2020
# Purpose: Returns 2 Random Positive Integers Between 2-14
# Input: None
# Output: TwoCard Object with 2 Positive Integers Between 2-14
# Dependencies: getCard()
# ====================================================================
def getHand():
    intValue1 = getCard()
    intValue2 = getCard()

    return TwoCard(intValue1, intValue2)


# Author: Samuel Bai
# Date: 03/05/2020
# Purpose: Displays the Colouration, Suit, and Value of a Card
# Input: Integer Between 2-14
# Output: A Corresponding Playing Card with a Random Suit
#         and Corresponding Colouration
# Dependencies: Random Module, Sys Module
# ====================================================================
def printCard(playerCard):
    strSuit = choice(['♠', '♦', '♥', '♣'])

    if playerCard == 11:
        strCard = 'J'
    elif playerCard == 12:
        strCard = 'Q'
    elif playerCard == 13:
        strCard = 'K'
    elif playerCard == 14:
        strCard = 'A'
    else:
        strCard = str(playerCard)

    if strSuit == '♠' or strSuit == '♣':
        print('\033[37;1m' + strCard + strSuit + '\033[0m' + '\n')
    else:
        print('\033[31;1m' + strCard + strSuit + '\033[0m' + '\n')


# Author: Samuel Bai
# Date: 03/05/2020
# Purpose: Displays the Colouration, Suit, and Value of 2 Cards
# Input: 2 Integers Between 2-14
# Output: A Corresponding Playing Card with a Random Suit
#         and Corresponding Colouration for each Integer
# Dependencies: Random Module, TwoCard class, Sys Module
# ====================================================================
def printHand(playerHand):
    strSuit1 = choice(['♠', '♦', '♥', '♣'])
    strSuit2 = choice(['♠', '♦', '♥', '♣'])

    if playerHand.value1 == 11:
        strCard1 = 'J'
    elif playerHand.value1 == 12:
        strCard1 = 'Q'
    elif playerHand.value1 == 13:
        strCard1 = 'K'
    elif playerHand.value1 == 14:
        strCard1 = 'A'
    else:
        strCard1 = str(playerHand.value1)

    if playerHand.value2 == 11:
        strCard2 = 'J'
    elif playerHand.value2 == 12:
        strCard2 = 'Q'
    elif playerHand.value2 == 13:
        strCard2 = 'K'
    elif playerHand.value2 == 14:
        strCard2 = 'A'
    else:
        strCard2 = str(playerHand.value2)

    if strSuit1 == '♠' or strSuit1 == '♣':
        print('\033[2;37;1m' + strCard1 + strSuit1, end='\033[0m ')
    else:
        print('\033[2;31;1m' + strCard1 + strSuit1, end='\033[0m ')

    if strSuit2 == '♠' or strSuit2 == '♣':
        print('\033[2;37;1m' + strCard2 + strSuit2 + '\033[0m' + '\n')
    else:
        print('\033[2;31;1m' + strCard2 + strSuit2 + '\033[0m' + '\n')


# Author: Samuel Bai
# Date: 03/05/2020
# Purpose: Determines the Type of Hand a Player Has
# Input: 2 Integers
# Output: Type of Hand a Player Has
# Dependencies: TwoCard class
# ====================================================================
def getHandType(playerHand):
    if playerHand.value1 == playerHand.value2:
        strHandType = 'pair'

    elif playerHand.value1 == playerHand.value2 + 1 or playerHand.value1 == playerHand.value2 - 1:
        strHandType = 'consecutive'

    else:
        strHandType = 'non-consecutive'

    return strHandType


# Author: Samuel Bai
# Date: 03/05/2020
# Purpose: Determines Distance Between 2 Integers
# Input: 2 Integers
# Output: Number of Integers Between 2 Integers
# Dependencies: TwoCard class
# ====================================================================
def getSpread(playerHand):
    if playerHand.value1 > playerHand.value2:
        playerHand.value1, playerHand.value2 = playerHand.value2, playerHand.value1

    intSpread = 0
    for i in range(playerHand.value1 + 1, playerHand.value2):
        intSpread += 1

    return intSpread


# Author: Samuel Bai
# Date: 03/05/2020
# Purpose: Determines the Amount of Points a Player Earns Depending
#          on the Distance Between 2 Integers
# Input: 2 Integers
# Output: the Amount of Points a Player
# Dependencies: getSpread()
# ====================================================================
def getPayout(playerHand):
    intSpread = getSpread(playerHand)
    if intSpread == 1:
        intPayout = 5
    elif intSpread == 2:
        intPayout = 4
    elif intSpread == 3:
        intPayout = 2
    else:
        intPayout = 1

    return intPayout


# Author: Samuel Bai
# Date: 03/05/2020
# Purpose: Determines if an Integer is Between 2 Integers
# Input: 3 Integers
# Output: Boolean Value Stating if an Integer is Between 2 Integers
# ====================================================================
def checkBetween(playerHand, playerCard3):
    if playerHand.value1 > playerHand.value2:
        playerHand.value1, playerHand.value2 = playerHand.value2, playerHand.value1

    boolBetween = False
    if playerCard3 < playerHand.value2 and playerCard3 > playerHand.value1:
        boolBetween = True

    return boolBetween


# Main
restart = 'Y'

while restart == 'Y':

    intPurse = 100

    strBet = 'Y'
    while strBet == 'Y':
        print()
        intPlayerBet = getPositiveInteger(1, intPurse, 'Enter a bet amount ')
        intPurse -= intPlayerBet

        intHand = getHand()
        print()
        print('Your Hand:')
        printHand(intHand)

        if getHandType(intHand) == 'pair':

            print()
            print('Pair--Third Card:')
            intCard3 = getCard()
            printCard(intCard3)
            if intCard3 == intHand.value1:
                intPurse += intPlayerBet * 11

            else:
                print()
                print('The round was a tie')
                intPurse += intPlayerBet

        elif getHandType(intHand) == 'consecutive':
            print()
            print('The round was a tie')
            intPurse += intPlayerBet

        else:
            if intPlayerBet < intPurse:
                intBet2High = intPlayerBet
            else:
                intBet2High = intPurse

            if intBet2High != 0:
                print()
                intPlayerBet2 = getPositiveInteger(0, intBet2High, 'Enter another bet amount ')
                intPlayerBet += intPlayerBet2
                intPurse -= intPlayerBet2

            intCard3 = getCard()
            print()
            print('Non-Consecutive--Third Card:')
            printCard(intCard3)

            if checkBetween(intHand, intCard3):
                intPurse += intPlayerBet * getPayout(intHand)

        print()
        print('You now have %i in your purse' % intPurse)

        if intPurse == 0:
            strBet = 'N'

        else:

            # Asks the user if they wish to bet again
            print()
            strBet = input('Bet Again? (Y/N): ').upper()

            # Checks if the user input is either Y/N
            while strBet != 'Y' and strBet != 'N':
                print()
                print('ERROR: Please enter Y/N')
                strBet = input('Bet Again? (Y/N): ').upper()

        if strBet == 'N':
            print()
            print('Thank you for playing')
            print('You ended the game with %i in your purse' % intPurse)

    # Asks the user if they wish to re-execute the program
    print()
    restart = input('Would you like to play a new game? (Y/N): ').upper()

    # Checks if the user input is either Y/N
    while restart != 'Y' and restart != 'N':
        print()
        print('ERROR: Please enter Y/N')
        restart = input('Would you like to play a new game? (Y/N): ').upper()
