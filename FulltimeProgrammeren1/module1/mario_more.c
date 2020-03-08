/****************************************************************************
 * mario_more.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Creates two half-pyramids of a specified height.
 ***************************************************************************/
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // prototype variables
    int number, hash, space, rows;

    // prompt for a number between 1 and 23
    do
    {
        number = get_int("Enter a number between 1 and 23: ");
    }
    while (number < 0 || number > 23);

    // print out this many rows
    for (rows = 0; rows < number; rows++)
    {
        // print out spaces in the columns
        for (space = (number - 1); space > rows; space--)
        {
            printf(" ");
        }

        // print out hashtags in the columns
        for (hash = (rows + 1); hash > 0; hash--)
        {
            printf("#");
        }

        // print out two spaces in between half pyramids
        printf("  ");

        // print out hashtags in the columns
        for (hash = (rows + 1); hash > 0; hash--)
        {
            printf("#");
        }
        printf("\n");
    }
}
