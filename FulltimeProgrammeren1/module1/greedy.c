/****************************************************************************
 * greedy.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Calculates the minimum number of coins required to give a user change.
 ***************************************************************************/
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // create the variables for the amount of money and the number of coins
    int count = 0;
    float amount = get_float("Change owed: ");

    // prompt user for a positive number
    while (amount < 0)
    {
        if (amount < 0)
        {
            amount = get_float("Please enter a positive number ");
        }
        else
        {
            break;
        }
    }

    // convert dollars into cents
    amount = amount * 100;

    // count the number of quarters
    while (amount > 0)
    {
        if (amount > 24)
        {
            amount = amount - 25;
            count++;
        }
        else
        {
            break;
        }
    }

    // count the number of dimes
    while (amount > 0)
    {
        if (amount > 9)
        {
            amount = amount - 10;
            count++;
        }
        else
        {
            break;
        }
    }

    // count the number of nickles
    while (amount > 0)
    {
        if (amount > 4)
        {
            amount = amount - 5;
            count++;
        }
        else
        {
            break;
        }
    }

    // count the number of pennies
    while (amount > 0)
    {
        if (amount == 4 || amount == 3 || amount == 2 || amount == 1 || amount == 0)
        {
            amount = amount - 1;
            count++;
        }
        else
        {
            break;
        }
    }

    // show the number of coins used
    printf("%i\n", count);
}
