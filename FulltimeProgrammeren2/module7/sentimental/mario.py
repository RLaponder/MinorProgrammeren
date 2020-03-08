 #**************************************************************************************
 # mario.py
 #
 # Fulltime Programmeren 2
 # Robin Laponder
 #
 # Creates two half-pyramids of a specified height.
 #**************************************************************************************

from cs50 import get_int

def main():
    # set number to 0
    number = -1

    # prompt user for a positive integer between 1 and 23
    while number < 0 or number > 23:
        number = get_int("Height: ")

    # set rows to 1 and print out the pyramid
    rows = 1
    for i in range (number):
        hashes = number - (number - rows)
        spaces = number - rows
        print(" " * spaces, end = "")
        print("#" * hashes, end = "")
        print("  ", end = "")
        print("#" * hashes)
        rows += 1

if __name__ == "__main__":
    main()