/****************************************************************************
 * mario_less.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Creates a right-aligned hash-pyramid of a specified height.
 ***************************************************************************/
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // define variables
    int number;
    int hash;
    int space;
    int rows;

    // ask for a number between 1 and 23
    do
    {
        number = get_int("Enter a number between 1 and 23: ");
    }
    while (number < 0 || number > 23);

    // print out pyramid with given number
    // print out this many rows
    for (rows = 0; rows < number; rows++)
    {
        // print out this many columns
        // print out spaces in the columns
        for (space = (number - 1); space > rows; space--)
        {
            printf(" ");
        }

        // print out hashtags in the columns
        for (hash = (rows + 2); hash > 0; hash--)
        {
            printf("#");
        }
        printf("\n");
    }
}
