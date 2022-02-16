# Author: Samuel Bai
# Date: 02/25/2020
# Purpose: For Loop Exercise - Question 1
#          Using For Loops to Calculate Monthly Mortgage Payments
# ===============================================================

restart = 'Y'

while restart == 'Y':

    print()
    mortgageAmount = round(float(input('Please enter your mortgage amount: $')), 2)

    while mortgageAmount < 100000 or mortgageAmount > 10000000:
        print()
        print('ERROR: The amount you entered is too low/high to be a mortgage')
        mortgageAmount = round(float(input('Please enter your mortgage amount: $')), 2)

    print(' ' * 60, 'YEARS OF AGREEMENT')
    print('INTEREST (%) ', end=(' ' * 12))

    for years in range(5, 36, 5):
        if years == 35:
            print('%-15i' % years)
        elif years == 5:
            print('%-14i' % years, end='')
        else:
            print('%-15i' % years, end='')

    for rate in range(1, 25):

        calcuRate = rate * 0.25
        i = (1 + (calcuRate / 200)) ** (1 / 6) - 1
        print('%8.2f' % calcuRate, end=(' ' * 3))

        for years in range(5, 36, 5):

            months = years * 12
            f = 1 / ((1 - (1 + i) ** -months) / i)
            monthlyPayment = '%0.2f' % (f * mortgageAmount)
            printPayment = '$' + str(monthlyPayment)

            if years == 35:
                print('%15s' % printPayment)
            else:
                print('%15s' % printPayment, end='')

        print(end=(' ' * 11))
        for years in range(5, 36, 5):

            months = years * 12
            f = 1 / ((1 - (1 + i) ** -months) / i)
            monthlyPayment = f * mortgageAmount
            totalInterest = '%0.2f' % (monthlyPayment * months - mortgageAmount)
            printTotal = '$' + str(totalInterest)

            if years == 35:
                print('%15s' % printTotal)
            else:
                print('%15s' % printTotal, end='')

        print()

    # Asks the user if they wish to re-execute the program
    restart = input('Calculate another mortgage? (Y/N): ').upper()

    # Checks if the user input is either Y/N
    while restart != 'Y' and restart != 'N':
        print()
        print('ERROR: Please enter Y/N')
        restart = input('Calculate another mortgage? (Y/N): ').upper()