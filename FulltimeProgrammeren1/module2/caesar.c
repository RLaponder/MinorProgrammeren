/****************************************************************************
 * caesar.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Encrypts messages using Caesar’s cipher.
 ***************************************************************************/
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
// 26 is the number of chars in the alfabet
#define LENGTH_ALFABET 26

    // check if there is one argument
    if (argc != 2)
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }

    // convert entered argument to integer
    int key = atoi(argv[1]);

    // prompt user to enter text
    string plaintext = get_string("plaintext: ");

    // scan for lowercase an uppercase letters and print in ciphertext
    printf("ciphertext: ");
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        // scan for lowercase letters and print encrypted characters
        if (islower(plaintext[i]))
        {
            printf("%c", (((plaintext[i] - 'a') + key) % LENGTH_ALFABET) + 'a');
        }

        // scan for uppercase letters and print encrypted characters
        else if (isupper(plaintext[i]))
        {
            printf("%c", (((plaintext[i] - 'A') + key) % LENGTH_ALFABET) + 'A');
        }

        // if character is not a letter, print it
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
    return 0;
}