# Author: Samuel Bai
# Date: 02/13/2020
# Purpose: Nesting, Div & Mod Exercise - Question 1
#          Using Div & Mod Operators to Calculate Change and Coins to Return
# ==========================================================================

restart = 'Y'

while restart == 'Y':

    # Asks the user for the cost of the product and the amount paid
    print('')
    price = float(input('Please enter the cost of the product: '))
    cashGive = float(input('Please enter the amount of cash tendered: '))

    # Calculates the amount of change to be given
    change = round(cashGive - price, 2)

    # Checks if there is an error with the inputs
    while price < 0 or price > 100000 or cashGive < 0 or cashGive > 100000 or change < 0:

        print('')
        print('ERROR:')

        # Checks if any input is negative
        if price < 0 or cashGive < 0:
            print('The amount tendered / cost of the product is negative')

        # Checks if any input is greater than $100 000 (this is a cash transaction)
        if price > 100000 or cashGive > 100000:
            print('Please be reasonable about the amount entered; this is a cash transaction')

        # Checks if the price of the product is greater than the amount paid for it
        if change < 0:
            print('You did not pay enough for the product')

        # Asks the user to input the price and amount paid again
        print('')
        price = float(input('Please enter the cost of the product: '))
        cashGive = float(input('Please enter the amount of cash tendered: '))

        change = round(cashGive - price, 2)

    # Outputs the price, cash paid, and change
    print('')
    print('Cost of Product: %13.2f' % price)
    print('Amount Tendered: %13.2f' % cashGive)
    print('Change Due:      %13.2f' % change)

    # Outputs the optimal distribution of the change in coins
    print('')
    print('Coin Distribution:')

    calcuChange = change * 100

    # Penny Rounding
    if calcuChange % 5 >= 3:
        calcuChange += (5 - calcuChange % 5)

    # Outputs the amount and value of $20 bills to be returned
    if calcuChange // 2000 > 0:
        change20 = int(calcuChange // 2000)
        calcuChange = calcuChange % 2000

        print('%9i - 20.00 = %10.2f' % (change20, change20 * 20))

    # Outputs the amount and value of $10 bills to be returned
    if calcuChange // 1000 > 0:
        change10 = int(calcuChange // 1000)
        calcuChange = calcuChange % 1000

        print('%9i - 10.00 = %10.2f' % (change10, change10 * 10))

    # Outputs the amount and value of $5 bills to be returned
    if calcuChange // 500 > 0:
        change5 = int(calcuChange // 500)
        calcuChange = calcuChange % 500

        print('%9i  - 5.00 = %10.2f' % (change5, change5 * 5))

    # Outputs the amount and value of Toonies to be returned
    if calcuChange // 200 > 0:
        changeT = int(calcuChange // 200)
        calcuChange = calcuChange % 200

        print('%9i  - 2.00 = %10.2f' % (changeT, changeT * 2))

    # Outputs the amount and value of Loonies to be returned
    if calcuChange // 100 > 0:
        changeL = int(calcuChange // 100)
        calcuChange = calcuChange % 100

        print('%9i  - 1.00 = %10.2f' % (changeL, changeL))

    # Outputs the amount and value of Quarters to be returned
    if calcuChange // 25 > 0:
        changeQ = calcuChange // 25
        calcuChange = calcuChange % 25

        print('%9i  - 0.25 = %10.2f' % (changeQ, changeQ * 0.25))

    # Outputs the amount and value of Dimes to be returned
    if calcuChange // 10 > 0:
        changeD = calcuChange // 10
        calcuChange = calcuChange % 10

        print('%9i  - 0.10 = %10.2f' % (changeD, changeD * 0.1))

    # Outputs the amount and value of Nickels to be returned and calculates Penny Rounding
    if calcuChange // 5 > 0:
        changeN = calcuChange // 5
        calcuChange = calcuChange % 5

        print('%9i  - 0.05 = %10.2f' % (changeN, changeN * 0.05))

    # Asks the user if they wish to re-execute the program
    print('')
    restart = input('Calculate another transaction? (Y/N): ').upper()

    # Checks if the user input is either Y/N
    while restart != 'Y' and restart != 'N':

        print('')
        print('ERROR: Please enter Y/N')
        print('')
        restart = input('Calculate another transaction? (Y/N): ').upper()