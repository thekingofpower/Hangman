#A class representing the visuals of Hangman
class Pictures:
    
    """Prints a visual depending on how many guesses are left"""
    @staticmethod
    def print_man(guesses_remaining, wrong_guesses):

        #These 2 parts of the diagram are the same regardless of how many guesses the player has left
        print("  ___      ")
        print(" |   |     ")
        
        #This part of the diagram looks different depending on how many guesses the player has left
        match guesses_remaining:
            case 6:
                print("     |     ")
                print("     |     ")
                print("     |     ")   
            
            case 5:
                print(" O   |     ")
                print("     |     ")
                print("     |     ")        

            case 4:
                print(" O   |     ")
                print(" |   |     ")
                print("     |     ")        

            case 3:
                print(" O   |     ")
                print("/|   |     ")
                print("     |     ")        

            case 2:
                print(" O   |     ")
                print("/|\\  |    ")
                print("     |     ")        

            case 1:
                print(" O   |     ")
                print("/|\\  |    ")
                print("/    |     ")        

            case 0:
                print(" O   |     ")
                print("/|\\  |    ")
                print("/ \\  |    ")        

            case _:
                print("Error in generating the diagram.")
        
        
        #This is the base of the diagram plus all of the player's wrong guesses
        print("===========" + Pictures.print_wrong_guesses(wrong_guesses))
    
    """Returns all of the wrong guesses the user has made"""
    @staticmethod
    def print_wrong_guesses(wrong_guesses):

        list = " "

        for i in wrong_guesses:
            list += i + " "

        return list