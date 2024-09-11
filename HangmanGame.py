import random
import os
from Pictures import Pictures

#A class representing a game of Hangman
class HangmanGame:

    #Number of wins the player has gotten across all games
    num_wins = 0

    #Total number of games the player has played
    total_games = 0

    #"""Creates a new game of Hangman"""
    def __init__(self):

        #The word of the game
        self.word = HangmanGame.generate_word()

        #A list representing whether or not each character of the word has been guessed
        self.guessed = [False] * len(self.word) 

        #The number of guesses the player has left
        self.guesses_remaining = 6

        #The number of letters the player has correctly guessed
        self.num_right_guesses = 0

        #A list of all the player's incorrect guesses
        self.wrong_guesses = []

        #A list of all the player's correct guesses
        self.right_guesses = []

    #"""Starts the game and asks the user if they want to play again when it's over"""
    @staticmethod
    def main():
        
        answer = "yes"

        #As long as the player keeps saying they want to play again, keep starting a new game
        while answer.lower() == "yes":

            #Clear the screen
            os.system("cls")

            #Play a game of Hangman
            HangmanGame.play_game()

            HangmanGame.total_games += 1

            #Calculates the player's win rate
            print("Win rate:", int(100 * HangmanGame.num_wins / HangmanGame.total_games), "%")
            print("Games played:", HangmanGame.total_games)

            #Asks the player if they want to play again
            answer = input("Would you like to play again? ")

    #"""Returns a random word from a list of words for Hangman"""
    @staticmethod
    def generate_word():
        
        try:
        
            with open("hangmanWords.txt", "r") as word_list:

                words = [word.rstrip("\n") for word in word_list.readlines()]

                #Randomly select a word from the list
                word = words[random.randrange(0, len(words) - 1)]

                return word

        except FileNotFoundError:
            #If the file isn't found, the word will be "error"
            return "error"

    #"""Excutes a single game of Hangman"""
    @staticmethod
    def play_game():

        #Creates a new game
        game = HangmanGame()

        #Prints the word (all underscores at the start) and the picture
        game.print_word()
        Pictures.print_man(game.guesses_remaining, game.wrong_guesses)

        #As long as the player has at least one guess remaining and they have not already guessed the word, continue the game
        while game.guesses_remaining > 0 and game.num_right_guesses < len(game.word): 
            
            letter = input("Guess a letter: ")[0].lower()

            #Clear the screen between guesses so the terminal looks cleaner
            os.system("cls")

            #If the player guesses the same letter twice, inform them of their mistake. Don't penalize them
            if letter in game.right_guesses or letter in game.wrong_guesses:
                print("You already guessed " + letter)
            
            #If they guess correctly, add the guess to the list of correct guesses
            elif game.check_guess(letter):
                game.right_guesses.append(letter)
            
            #If they guess incorrectly, add the guess to the list of correct guesses and decrease the number of guesses they have left
            else:
                game.wrong_guesses.append(letter)
                game.guesses_remaining -= 1
            
            #Print the word and the picture again
            game.print_word()
            Pictures.print_man(game.guesses_remaining, game.wrong_guesses)
              
        #Now that the game has ended, check if the player won or lost and tell them the result
        game.end_game()

    #"""Prints all of the characters of the word that have been guessed, and blank spaces for characters that haven't been guessed"""
    def print_word(self):

        #Go through every character in the word. If it has been guessed, print the character. Otherwise, print an underscore

        i = 0

        while i < len(self.word):

            if self.guessed[i]:
                print(self.word[i], end = " ")
            else:
                print("_", end = " ")
        
            i += 1
        
        #Starts a new line
        print("")
    
    #"""Returns whether or not the user's guess was correct"""
    def check_guess(self, letter):

        #Assume the guess is wrong until proven otherwise
        right_guess = False

        #Check if each character of the word is the same as the guess

        i = 0

        while i < len(self.word):
            if self.word[i] == letter:
                #If the character of the word is the same as the guess, set that position to True in the guessed list
                self.guessed[i] = True
                right_guess = True
                self.num_right_guesses += 1

            i += 1

        return right_guess

    #"""Tells the user whether they won or lost the game"""
    def end_game(self):

        #If they didn't get all the right guesses they needed, the player lost the game
        if self.num_right_guesses < len(self.word):
            print("You lose!")
            print("The word was...")
            print(self.word)
        else:
            print("You win!")
            HangmanGame.num_wins += 1

if __name__ == "__main__":
    HangmanGame.main()