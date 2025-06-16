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




def display_text(WORD, guessedLetter):
    #clean screen
    print("\n" * 20)
    #game title and some header
    print("Welcome to Hangman!")
    print("===================")

    #hits
    for letter in WORD:
        if (guess in WORD):
            " ".join(letter)
        else:
            " ".join("_")

    if DEBUG:
        print(f"MODE: {MODE}, choosen word is {WORD} ")



 
def gameLoop(TRIES, word, guessedLetter):
    guessedLetter =[]
    
    while(TRIES>0):
        display_text(word, guess)
        guess = input("Guess a letter: ")
        #check if user input is "single" alphabet
        if not guess.isalpha():
            print("Please type an alphabet...") 
            continue
        if len(guess) != 1:
            print("Please only type single alphabet....")
            continue
        #if all filter above is passed 
        guessedLetter.append(guess)

        #matching the letter
        if guess in WORD:
            print("match!!")
        else:
            print("wrong guess...")
            TRIES -= 1




def choosenWord():
    return random.choice(WORDSLIST)


def main():
    word = choosenWord()
    
    

    display_text(word, guess)
    gameLoop(TRIES, word)



if __name__ =="__main__":
    main()
