 #**************************************************************************************
 # vigenere.py
 #
 # Fulltime Programmeren 2
 # Robin Laponder
 #
 # Encrypts messages using Vigenère’s cipher.
 #**************************************************************************************

from sys import argv
from cs50 import get_string

def main():
    # check if user typed in one argument
    if len(argv) != 2 or not argv[1].isalpha():
        print("Usage: python vigenere.py k")
        exit(1)

    # convert entered argument to keyword
    keyword = argv[1].lower()

    # prompt user to enter plaintext
    plaintext = get_string("plaintext: ")

    # print ciphertext
    print("ciphertext: ", end = "")
    c = 0
    for i in plaintext:
        key = get_key(keyword, c)

        # Character is uppercase
        if i.isupper():
            upper = (((ord(i) - ord('A')) + key) % 26) + ord('A')
            print(chr(upper), end="")
            c += 1

        # Character is lowercase
        elif i.islower():
            lower = (((ord(i) - ord('a')) + key) % 26) + ord('a')
            print(chr(lower), end="")
            c += 1

        else:
            print("{}".format(i), end="")

    # print a new line at the end
    print()

# get key for every letter
def get_key(keyword, counter):
    letter = counter % len(keyword)
    return ord(keyword[letter]) - 97

if __name__ == "__main__":
    main()