/****************************************************************************
 * initials.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Prints a person's initials, given a person’s name.
 ***************************************************************************/
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // prompt user for name
    string name = get_string("Name: ");

    // print the first letter of the first name as an uppercase letter
    printf("%c", toupper(name[0]));

    // search for spaces in input and print the next character in uppercase
    for (int i = 0; i < strlen(name); i++)
    {
        if (name[i] == ' ')
        {
            printf("%c", toupper(name[i + 1]));
        }
    }
    printf("\n");
    return 0;
}