/****************************************************************************
 * viginere.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Encrypts messages using Vigenère’s cipher.
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

    // variables
    string key = argv[1];
    int keylength = strlen(key);

    // check if argument contains of only letters
    for (int i = 0; i < keylength; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Usage: ./viginere k\n");
            return 1;
        }
    }

    // prompt user to enter text
    string plaintext = get_string("plaintext: ");

    // scan for lowercase an uppercase letters and print in ciphertext
    printf("ciphertext: ");
    for (int i = 0, j = 0, n = strlen(plaintext); i < n; i++, j++)
    {
        // convert key to lowercase letters
        int keyletter = tolower(key[j % keylength]) - 'a';

        // scan for lowercase letters and print encrypted characters
        if (islower(plaintext[i]))
        {
            printf("%c", 'a' + (plaintext[i] - 'a' + keyletter) % LENGTH_ALFABET);
        }

        // scan for uppercase letters and print encrypted characters
        else if (isupper(plaintext[i]))
        {
            printf("%c", 'A' + (plaintext[i] - 'A' + keyletter) % LENGTH_ALFABET);
        }

        // if character is not a letter, print it
        else
        {
            printf("%c", plaintext[i]);
            j--;
        }
    }
    printf("\n");
    return 0;
}