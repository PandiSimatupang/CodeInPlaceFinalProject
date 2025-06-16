import random


#game MODE
TEST = "TESTING"
LAUNCH = "LAUNCH"

#Game mode selection
#------------------------------------------> SELECTED MODE
MODE = LAUNCH   # chose TEST or LAUNCH
#-------------------------------------------> SELECTED MODE
DEBUG = (MODE == TEST)  #checking selected mode.. it's "true" if TEST


#quick test
WORDSLIST = ['apple', 'banana', 'cranbarry']




#global variable
TRIES = 5
WORD = random.choice(WORDSLIST)



 
def gameLoop(TRIES):

    while(TRIES>0):
        guess = input("Guess a letter: ")
        #check if user input is "single" alphabet
        if not guess.isalpha():
            print("Please type an alphabet...") 
            continue
        if len(guess) != 1:
            print("Please only type single alphabet....")
            continue
        
        #matching the letter
        if guess in WORD:
            print("match!!")
        else:
            print("wrong guess...")
            TRIES -= 1



def display_text():
    #game title and some header
    print("\n" * 20)
    print("Welcome to Hangman!")
    print("===================")

    if DEBUG:
        print(f"MODE: {MODE}, choosen word is {WORD} ")




def main():
    display_text()
    gameLoop(TRIES)



if __name__ =="__main__":
    main()
