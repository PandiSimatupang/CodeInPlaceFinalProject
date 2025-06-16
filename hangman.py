import random


#game MODE
TEST = "TESTING"
LAUNCH = "LAUNCH"

#Game mode selection
#------------------------------------------> SELECTED MODE
MODE = TEST   # chose TEST or LAUNCH
#-------------------------------------------> SELECTED MODE
DEBUG = (MODE == TEST)  #checking selected mode.. it's "true" if TEST


#quick test
WORDSLIST = ['apple', 'banana', 'cranbarry']



#global variable
TRIES = 5




def display_text(word, guessedLetter):
    #clean screen
    print("\n" * 20)
    #game title and some header
    print("Welcome to Hangman!")
    print("===================")

    #hits
    print("WORD: ", "_ "*len(word))

    if DEBUG:
        print(f"MODE: {MODE}, choosen word is {word} ")
        print(guessedLetter)



 
def gameLoop(TRIES, word, guessedLetter):
    
    while(TRIES>0):
        display_text(word, guessedLetter)
        guess = input("Guess a letter: ")
        #check if user input is "single" alphabet
        if not guess.isalpha():
            print("Please type an alphabet...") 
            continue
        if len(guess) != 1:
            print("Please only type single alphabet....")
            continue
        if guess in guessedLetter:
            print("This letter is already tried....")
            continue           
        #if all filter above is passed 
        guessedLetter.append(guess)

        #matching the letter
        if guess in word:
            print("match!!")
        else:
            print("wrong guess...")
            TRIES -= 1




def choosenWord():
    return random.choice(WORDSLIST)


def main():
    word = choosenWord()
    guessedLetter=[]

    display_text(word, guessedLetter)
    gameLoop(TRIES, word, guessedLetter)



if __name__ =="__main__":
    main()
