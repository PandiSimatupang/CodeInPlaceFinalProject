import random

#quick test
wordsList = ['apple', 'banana', 'cranbarry']


#global variable
tries = 5
word = random.choice(wordsList)



def main():
    #game title and some header
    print("Welcome to Hangman!")
    print("===================")

    gameLoop()



def gameLoop():

    while(True):
        guess = input("Guess a letter: ")
        #check if user input is "single" alphabet
        if not guess.isalpha():
            print("Pleaser type an alphabet...") 
            continue


if __name__ =="__main__":
    main()