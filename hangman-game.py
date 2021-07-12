"""
Set task: Create a Hangman game.
Method:
* self.word_list (list) is imported from a defined document filled with suitable words in word-list.txt (courtesy https://www.hangmanwords.com/words).
* word (String) is a randomly selected word from self.word_list
* solution (list) is the current progress. It starts as ['_','_',...,'_'] and gets progressively filled.
* guesses (list) are letters the user already tried and that were wrong. It starts empty and gets progressively filled.
* Each input gets checked:
** If it is not a letter the user has to try again.
** If it is already in solution or guesses the user user has to try again.
** If it is a new letter, we check whether it is part of the word. If yes it's added to solution, else it's added to guesses and fails (int) gets incremented.
* The game ends once the amount of fails exceeds the max set in self.hangman (list) or once the word has been guessed.
"""
from random import randrange, random
from time import sleep

class Hangman:

    def __init__(self):
        self.word_list = [x.replace("\n","") for x in open("word-list.txt").readlines()]
        self.hangman = [
            "\n\n\n\n\n________",
            "\n|\n|\n|\n|\n|________",
            " ______\n|\n|\n|\n|\n|________",
            " ______\n|/\n|\n|\n|\n|________",
            " ______\n|/     |\n|\n|\n|\n|________",
            " ______\n|/     |\n|      O\n|\n|\n|________",
            " ______\n|/     |\n|      O\n|      |\n|      |\n|________",
            " ______\n|/     |\n|      O\n|     \\|\n|      |\n|________",
            " ______\n|/     |\n|      O\n|     \\|/\n|      |\n|________",
            " ______\n|/     |\n|      O\n|     \\|/\n|      |\n|_____/__",
            " ______\n|/     |\n|      O\n|     \\|/\n|      |\n|_____/_\\"]
        self.name = input("Hello and welcome to our game of Hangman. What is your name?\n")
        
    def game(self):
        fails = 0
        word = self.word_list[randrange(0,len(self.word_list))]
        solution = ["_" for char in word]
        guesses = list()
        sleep(random()*3)
        print(f"{self.name}, your word has {len(word)} letters. Good luck and have fun.")

        while True:
            guess = input(f"{self.hangman[fails]}  {solution}\nPlease make your guess. Already guessed letters: {guesses}\n").lower()
            if guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
                print("Only letters in the alphabet are allowed as input. Please try again.")
                continue
            elif guess.upper() in solution or guess.upper() in guesses:
                print("You already tried this letter.")
                continue
            if guess in word:
                print("That was a hit!")
                for i in range(len(word)):
                    if word[i] == guess:
                        solution[i] = guess.upper()
                if "_" not in solution:
                    print(f"Congrats {self.name}, you won. The word was: {word}")
                    return
            else:
                fails += 1
                guesses.append(guess.upper())
                guesses.sort()
                if fails == len(self.hangman) - 1:
                    print(f"{self.hangman[fails]}  Game Over, {self.name}. The word was: {word}")    
                    return
                print(f"{guess} was not correct, please try again.")


H = Hangman()
H.game()