# **************************************************************************************
# hangman.py
#
# Fulltime Programmeren 2
# Robin Laponder
#
# A program that allows someone to play Evil Hangman against the computer.
# **************************************************************************************
from cs50 import get_int
from cs50 import get_string


class Lexicon:
    def __init__(self):
        # Open dictionary file and make a set of all the words in it.
        self.words = set()
        self.dictionary = open("dictionary.txt", "r")
        for line in self.dictionary:
            self.words.add(line.rstrip("\n"))

    def get_words(self, length):
        # Return a list of all words from the dictionary of the given length.
        self.length = length
        self.list = []
        for word in self.words:
            if len(word) == length:
                self.list.append(word.rstrip("\n"))
        if not self.list:
            return False
        return self.list


class Hangman:
    def __init__(self, length, num_guesses):
        # Define exceptions.
        if length < 1:
            raise Exception("Hangman word needs to have positive length. >=(")
        if num_guesses < 1:
            raise Exception("You need at least one guess to play Hangman. >=(")

        # Initialization of Hangman class.
        self.length = length
        self.num_guesses = num_guesses

        # Declaration of variables.
        self.check_won = "not "
        self.guessed = ''
        self.letter = ''
        self.longest_key = ''
        self.pattern_before = []
        for elem in range(length):
            self.pattern_before.append('_')
        self.pattern_after = []
        for elem in range(length):
            self.pattern_after.append('_')
        self.pattern_after = ''.join(self.pattern_after)
        self.words = Lexicon().get_words(self.length)

    def guess(self, letter):
        # Define exceptions.
        if len(letter) > 1:
            raise Exception("You can only guess one letter at a time! >=(")
        if (letter.isalpha()) == False:
            raise Exception("You can only guess letters! >=(")
        if letter in self.guessed:
            raise Exception("You already guessed this letter! >=(")

        # Make a string of letters that are guessed.
        self.letter = letter
        self.guessed += self.letter

        # Make word families by making unique keys and adding wordlists.
        self.dictionary = {}
        for word in self.words:
            key = list(word)
            for char in range(len(key)):
                if key[char] == letter:
                    key[char] = letter
                else:
                    key[char] = '0'
            key = ''.join(key)
            if key in self.dictionary:
                self.dictionary[key].append(word)
            else:
                self.dictionary[key] = []
                self.dictionary[key].append(word)

        # Find the key with the longest wordlist and make a new list with it.
        self.longest_key = max(self.dictionary, key=lambda k: len(self.dictionary[k]))
        self.words = self.dictionary[self.longest_key]

        # Create a pattern of underscores and correctly guessed letters.
        pattern_letter = list(self.longest_key)
        for char in range(len(pattern_letter)):
            if pattern_letter[char] == '0':
                if self.pattern_before[char] == '_':
                    self.pattern_before[char] = '_'
                if self.pattern_before[char] != '_':
                    self.pattern_before[char] = self.pattern_before[char]
            elif pattern_letter[char] == self.letter:
                self.pattern_before[char] = self.letter
            else:
                self.pattern_before[char] = pattern_letter[char]
        self.pattern_after = ''.join(self.pattern_before)

        # Check if the guessed letter is in the secret word.
        joinedwords = ''.join(self.words)
        if self.letter in joinedwords:
            print("It's in the word :(")
            return True
        else:
            print("That's not in the word >=)")
            self.num_guesses -= 1
            return False

    def pattern(self):
        # Return the pattern.
        return self.pattern_after

    def guessed_string(self):
        # Return the string of guessed letters.
        return self.guessed

    def consistent_word(self):
        # Produce a word that matches the current pattern.
        self.secretword = self.words[0]
        return self.secretword

    def finished(self):
        # Return True if the game is won or lost, otherwise False.
        if self.won():
            return True
        if self.lost():
            return True
        return False

    def won(self):
        # Return True if the player has won, otherwise False.
        self.check_won = self.pattern_after
        for char in range(len(self.check_won)):
            if self.check_won[char] == '_':
                self.check_won = "not "
                return False
        self.check_won = ""
        return True

    def lost(self):
        # Return True if the player has lost, otherwise False.
        if self.num_guesses == 0:
            check_lost = list(self.pattern_after)
            for char in range(len(check_lost)):
                if check_lost[char] == '_':
                    return True
        return False

    def __str__(self):
        if statistics == 'y':
            return "letters guessed are '{}', {} words remaining, {} guesses remaining, game {}won".format(self.guessed, len(self.words),
                                                                                                           self.num_guesses, self.check_won)
        else:
            return "{} guesses remaining".format(self.num_guesses)


if __name__ == "__main__":
    # Start the game
    startgame = 1
    while startgame > 0:
        # Greet the user.
        print("WELCOME TO EVIL HANGMAN >=)")

        # Ask the user to enter the length of the word, a number of guesses and if he/she wants statistics.
        length = get_int("Enter an amount of letters you want in the word: ")
        num_guesses = get_int("Enter the number of guesses you would like: ")
        statistics = get_string("Would you like detailed statistics of this game? Type 'y' of 'n': ")

        # Create a new game with the entered parameters.
        lex = Lexicon()
        game = Hangman(length, num_guesses)

        # Check if there are words with the entered length, if not reprompt.
        while lex.get_words(length) == False:
            length = get_int("Enter an amount of letters you want in the word: ")
            game = Hangman(length, num_guesses)

        # Keep playing the game while it is not finished.
        while game.finished() == False:
            letter = input("Guess a letter: ")
            game.guess(letter)
            print(game.pattern())
            print(game)
            game.finished()
            if game.won():
                print("YOU WON! (ﾉ*ﾟｰﾟ)ﾉ")

        # Check if the game is lost and reveal the secret word.
        if game.lost():
            print("YOU LOST! (~˘▾˘)~")
            print("The secret word is ", end='')
            print(game.consistent_word())

        # Ask the user if he/she wants to start a new game.
        newgame = input("Would you like to play again? Enter 'y' or 'n': ")
        if newgame == 'y':
            startgame += 1
        else:
            startgame = 0