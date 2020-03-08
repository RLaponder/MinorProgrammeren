/****************************************************************************
 * credit.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Checks the validity and company of a credit card.
 ***************************************************************************/
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // prototype variables
    int digits, ndigits, sumofdigits = 0;
    long fdigits, cardnumber, temp_cardnumber;

    // prompt user for cc number
    do
    {
        cardnumber = get_long("Please enter your credit card number: ");
    }
    while (cardnumber < 0);

    // store cardnumber for later use
    fdigits = cardnumber;
    temp_cardnumber = cardnumber;

    // scan the first two digits of cc number
    do
    {
        fdigits /= 10;
    }
    while (fdigits > 99);

    // scan the number of digits in cc number
    for (ndigits = 0; cardnumber > 0; ndigits++)
    {
        cardnumber /= 10;
    }

    // scan if cc number is valid by applying Luhn algorithm
    for (int i = 1; i <= ndigits; i++)
    {
        int digit = temp_cardnumber % 10LL;
        if (i % 2 == 0)
        {
            digit *= 2;
            if (digit > 9)
            {
                digit -= 9;
            }
        }
        sumofdigits += digit;
        temp_cardnumber /= 10LL;
    }
    // print if cc number is invalid
    if (sumofdigits % 10 != 0)
    {
        printf("INVALID\n");
    }

    // scan and print the company of cc
    else if (ndigits == 15 && (fdigits == 34 || fdigits == 37))
    {
        printf("AMEX\n");
    }
    else if (ndigits == 16 && ((50 < fdigits) && (fdigits < 56)))
    {
        printf("MASTERCARD\n");
    }
    else if ((ndigits == 13 || ndigits == 16) && ((39 < fdigits) && (fdigits < 50)))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}