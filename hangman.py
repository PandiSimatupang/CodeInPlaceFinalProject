import random


#game MODE
DEBUG = "debug"
LAUNCH = "launch"

#Game mode selection
#-------------------------> SELECTED MODE
MODE = DEBUG


#quick test
wordsList = ['apple', 'banana', 'cranbarry']




#global variable
tries = 5
word = random.choice(wordsList)






 
def gameLoop(tries):

    while(tries>0):
        guess = input("Guess a letter: ")
        #check if user input is "single" alphabet
        if not guess.isalpha():
            print("Please type an alphabet...") 
            continue
        if len(guess) != 1:
            print("Please only type single alphabet....")
            continue
        
        #matching the letter
        if guess in word:
            print("match!!")
        else:
            print("wrong guess...")
            tries -= 1



def display_text():
    #game title and some header
    print("Welcome to Hangman!")
    print("===================")








def main():
    display_text()
    gameLoop(tries)



if __name__ =="__main__":
    main()
