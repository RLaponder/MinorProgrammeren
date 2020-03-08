# **************************************************************************************
# helpers.py
#
# Fulltime Programmeren 2
# Robin Laponder
#
# Program that determines whether two files are similar or not.
# **************************************************************************************


from nltk.tokenize import sent_tokenize


def lines(a, b):
    # Remove newlines and make a set of the common lines to prevent duplicates.
    # Compare the two sets and return a list with common lines.
    return list(set(a.split('\n')).intersection(b.split('\n')))


def sentences(a, b):
    # Make two sets with sentences to prevent duplicates.
    # Compare the two sets and return a list with common sentences.
    return list(set(sent_tokenize(a)).intersection(set(sent_tokenize(b))))


def substrings(a, b, n):
    # Open two empty lists.
    substrings_a = []
    substrings_b = []

    # Fill the lists with substrings of a certain lenght.
    for i in range(len(a) - n + 1):
        substrings_a.append(a[i:i + n])

    for i in range(len(b) - n + 1):
        substrings_b.append(b[i:i + n])

    # Convert the lists to sets to prevent duplicates.
    # Compare the two sets and return a list with common substrings.
    return list(set(substrings_a).intersection(set(substrings_b)))