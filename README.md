DESCRIPTION: This program allows you to play Hangman in the Python terminal using randomly selected words

INSTRUCTIONS: To play the game, enter a character (case doesn't matter) and the game will tell you whether or not the guess was right. 

You have 6 incorrect guesses before you lose. All previous incorrect guesses will be displayed to you.

To play another game, enter "yes" when prompted.

EXPLANATION: This program utilizes a file filled with 1000 common English words to randomly select a word every game. 

The program keeps track of what characters have already been guessed so the word can be properly printed out based on what the user has guessed.

A separate class exists to handle the visuals. Every time the user guesses incorrectly, a new part of the stick figure is added.
