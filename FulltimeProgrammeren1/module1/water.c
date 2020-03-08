/****************************************************************************
 * water.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Calculates the number of bottles, given the minutes of showering.
 ***************************************************************************/
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int minutes = get_int("Minutes: ");
    printf("Bottles: %i\n", minutes * 12);
}