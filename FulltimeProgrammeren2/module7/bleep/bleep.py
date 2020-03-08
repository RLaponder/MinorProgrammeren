 #**************************************************************************************
 # bleep.py
 #
 # Fulltime Programmeren 2
 # Robin Laponder
 #
 # Censors messages that contain words that appear on a list of supplied “banned words.”
 #**************************************************************************************

from cs50 import get_string
from sys import argv

def main():
    # check if user typed in one argument
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    # open .txt file and make a lowercase and an uppercase list of the words in it
    banned = open(argv[1])
    banned_lower = list(banned)
    banned_upper = list(map(lambda x:x.upper(), list(banned_lower)))

    # prompt user to enter a message
    message = get_string("What message would you like to censor? ")
    count = message.count(' ')
    spaces = 0

    # check if words are banned words and print censored message
    for word in message.split():
        banword = word + '\n'
        if banword in banned_lower or banword in banned_upper:
            print('*' * (len(banword) - 1), end = '')
        else:
            print(word, end = '')
        if spaces < count:
            print(' ', end = '')
            spaces += 1

    # print a new line at the end of censored message
    print('\n', end = '')

    # succes
    exit(0)

if __name__ == "__main__":
    main()
