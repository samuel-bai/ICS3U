# Author: Samuel Bai
# Date: 02/25/2020
# Purpose: For Loop Exercise - Question 2
#          Using For Loops to Output Star Patterns
# ================================================

restart = 'Y'

while restart == 'Y':

    # Shape Property
    print('''
    A = Square
    B = Triangle
    C = Diamond (size must be odd)
    D = Cross
    ''')

    patternType = input('Please select what pattern you would like to display: ').upper()

    while patternType != 'A' and patternType != 'B' and patternType != 'C' and patternType != 'D':
        print()
        print('ERROR: Invalid letter inputted')
        patternType = input('Please select what pattern you would like to display: ').upper()

    # Hollow Property
    print()
    inHollow = input('Please indicate if you would like your pattern to be hollow (Y/N): ').upper()

    while inHollow != 'Y' and inHollow != 'N':
        print()
        print('ERROR: Please enter Y/N')
        inHollow = input('Please indicate if you would like your pattern to be hollow (Y/N): ').upper()

    patternHollow = False
    if inHollow == 'Y':
        patternHollow = True

    # Size Property
    print()
    patternSize = int(input('Please choose the size of your pattern (1-20): '))

    while patternSize <= 0 or patternSize > 20:
        print()
        print('ERROR: Number entered invalid')
        patternSize = int(input('Please choose the size of your pattern (1-20): '))

    # Square Shape
    if patternType == 'A':

        print()
        print('This is your square pattern:')
        print()

        # Hollow Square
        if patternHollow:
            for i in range(patternSize):

                if i == 0 or i == patternSize - 1:
                    stars = '*  ' * patternSize
                    print(stars)

                else:
                    spacingInner = '   ' * (patternSize - 2)
                    print('*  ' + spacingInner + '*  ')

        # Filled Square
        else:
            for i in range(patternSize):
                stars = '*  ' * patternSize
                print(stars)

    # Triangle Shape
    if patternType == 'B':

        print()
        print('This is your triangle pattern:')
        print()

        # Hollow Triangle
        if patternHollow:
            for i in range(patternSize):

                if i == 0 or i == patternSize - 1:
                    stars = '*  ' * (i + 1)
                    print(stars)

                else:
                    spacingInner = '   ' * (i - 1)
                    print('*  ' + spacingInner + '*  ')

        # Filled Triangle
        else:
            for i in range(patternSize):
                stars = '*  ' * (i + 1)
                print(stars)

    # Diamond Shape
    if patternType == 'C':

        # Edits user input for an odd size
        while patternSize <= 0 or patternSize > 20 or patternSize % 2 == 0:
            print()
            print('ERROR: The diamond size is even/invalid')
            patternSize = int(input('Please choose an odd size for your pattern (1-19): '))

        print()
        print('This is your diamond pattern:')
        print()

        # Hollow Diamond
        if patternHollow:
            for i in range(patternSize):

                if i == 0 or i == patternSize - 1:
                    spacingOuter = '   ' * (abs(patternSize // 2 - i))
                    stars = '*  ' * (patternSize - 2 * abs(patternSize // 2 - i))
                    print(spacingOuter + stars)

                else:
                    spacingOuter = '   ' * (abs(patternSize // 2 - i))
                    spacingInner = '   ' * ((patternSize - 2 * abs(patternSize // 2 - i)) - 2)
                    print(spacingOuter + '*  ' + spacingInner + '*  ')

        # Filled Diamond
        else:
            for i in range(patternSize):
                spacingOuter = '   ' * abs(patternSize // 2 - i)
                stars = '*  ' * (patternSize - 2 * abs(patternSize // 2 - i))
                print(spacingOuter + stars)

    # Cross Shape
    if patternType == 'D':

        print()
        print('This is your cross pattern:')
        print()

        # Hollow Cross
        if patternHollow:
            for i in range(patternSize * 2 + 1):

                if i == 0 or i == patternSize * 2:
                    # Left side gap
                    spacingLeft = patternSize - abs(patternSize - i)
                    spacingLeftPrint = '   ' * spacingLeft

                    # Left side of cross
                    stars1 = patternSize
                    stars1Print = '  *' * stars1

                    # Middle gap
                    spacingMid = abs((patternSize * 2) - (2 * i)) - patternSize
                    if spacingMid < 0:
                        spacingMid = 0
                    spacingMidPrint = '   ' * spacingMid

                    # Right side of cross
                    stars2 = patternSize
                    if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 + 1) and spacingMid == 0:
                        stars2 = ((patternSize * 2) - (spacingLeft + stars1)) * 2
                    stars2Print = '  *' * stars2

                    print(spacingLeftPrint + stars1Print + spacingMidPrint + stars2Print)

                else:
                    # Left side gap
                    spacingLeft = patternSize - abs(patternSize - i)
                    spacingLeftPrint = '   ' * spacingLeft

                    # Left side of cross
                    stars1 = patternSize
                    stars1Print = '  *' + '   ' * (stars1 - 2) + '  *'

                    # Middle gap
                    spacingMid = abs((patternSize * 2) - (2 * i)) - patternSize
                    if spacingMid < 0:
                        spacingMid = 0
                    spacingMidPrint = '   ' * spacingMid

                    # Right side of cross
                    stars2 = patternSize
                    if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 + 1) and spacingMid == 0:
                        stars2 = ((patternSize * 2) - (spacingLeft + stars1)) * 2

                    # Right-mid of cross
                    stars2Print = '  *' + '   ' * (stars2 - 2) + '  *'
                    if patternSize % 2 == 0:
                        if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 - 1) and spacingMid == 0:
                            stars2Print = '   ' * (stars2 - 1) + '  *'
                    else:
                        if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 + 1) and spacingMid == 0:
                            stars2Print = '   ' * (stars2 - 1) + '  *'

                    # Left-mid of cross
                    if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 - 1) and spacingMid == 0:
                        if i == patternSize:
                            stars1Print = '  *' + '   ' * (stars1 - 2)
                        else:
                            stars1Print = '  *' + '   ' * (stars1 - 1)

                    print(spacingLeftPrint + stars1Print + spacingMidPrint + stars2Print)

        # Filled Cross
        else:
            for i in range(patternSize * 2 + 1):
                # Left side gap
                spacingLeft = patternSize - abs(patternSize - i)
                spacingLeftPrint = '   ' * spacingLeft

                # Left side of cross
                stars1 = patternSize
                stars1Print = '  *' * stars1

                # Middle gap
                spacingMid = abs((patternSize * 2) - (2 * i)) - patternSize
                if spacingMid < 0:
                    spacingMid = 0
                spacingMidPrint = '   ' * spacingMid

                # Right side of cross
                stars2 = patternSize
                if spacingLeft + stars1 >= patternSize * 2 - (patternSize // 2 + 1) and spacingMid == 0:
                    stars2 = ((patternSize * 2) - (spacingLeft + stars1)) * 2
                stars2Print = '  *' * stars2

                print(spacingLeftPrint + stars1Print + spacingMidPrint + stars2Print)

    # Asks the user if they wish to re-execute the program
    print()
    restart = input('Display another pattern? (Y/N): ').upper()

    # Checks if the user input is either Y/N
    while restart != 'Y' and restart != 'N':
        print()
        print('ERROR: Please enter Y/N')
        restart = input('Display another pattern? (Y/N): ').upper()