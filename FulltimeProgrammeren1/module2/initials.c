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
    int i;

    // prompt user for name
    string name = get_string("Name: ");

    // search for the first letter of the first name and print it
    for (i = 0; i < strlen(name); i++)
    {
        if (isalpha(name[i]))
        {
            printf("%c", toupper(name[i]));
            break;
        }
    }

    // search for spaces and print the letter after the last space
    for (; i < strlen(name); i++)
    {
        if (isspace(name[i]))
        {
            if (isalpha(name[i+1]))
            {
                printf("%c", toupper(name[i+1]));
            }
        }
    }
    printf("\n");
    return 0;
}