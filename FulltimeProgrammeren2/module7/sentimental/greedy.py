 #**************************************************************************************
 # greedy.py
 #
 # Fulltime Programmeren 2
 # Robin Laponder
 #
 # Calculates the minimum number of coins required to give a user change.
 #**************************************************************************************

from cs50 import get_float

def main():
    # prompt user for an amount of money
    amount = get_float("Change owed: ")

    # if user did not enter a positive float, keep prompting for it
    while amount < 0:
        amount = get_float("Please enter a positive number: ")

    # convert amount in dollars to amount in cents and set count to 0
    amount *= 100
    count = 0

    # count the number of quarters
    while amount > 24:
        amount -= 25
        count += 1

    # count the number of dimes
    while amount > 9:
        amount -= 10
        count += 1

    # count the number of nickles
    while amount > 4:
        amount -= 5
        count += 1

    # count the number of pennies
    while amount == 4 or amount == 3 or amount == 2 or amount == 1:
        amount -= 1
        count += 1

    print(count)

if __name__ == "__main__":
    main()