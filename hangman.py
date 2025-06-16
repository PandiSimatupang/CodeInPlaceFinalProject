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


def display_text(word, guessedLetter, status, TRIES):
    #clean screen
    print("\n" * 20)

    #game title and some header
    print("Welcome to Hangman!")
    print("===================")
    
    #status
    print("COMM: ", status)

    #hints
    hints= ""
    for letter in word:
        if letter in guessedLetter:
            hints += (letter + " ") 
        else:
            hints += ("_ ")
        
        
    print("Tries :", TRIES)
    print("Guessed Letters: ", guessedLetter)
    print("WORD: ", hints)
    

    if DEBUG:
        print(f"MODE:  {MODE}", f"choosen word is -----> {word} ")
       #print(guessedLetter)



 
def gameLoop(TRIES, word, guessedLetter, status):

    while(TRIES>0):

        display_text(word, guessedLetter, status, TRIES)
        guess = input("Guess a letter: ")

        #check if user input is "single" alphabet
        if not guess.isalpha():
            status = "Please type an alphabet..." 
            continue
        if len(guess) != 1:
            status = "Please only type single alphabet...."
            continue
        if guess in guessedLetter:
            status= "This letter is already tried...."
            continue           

        #if all filter above is passed 
        guessedLetter.append(guess)




        #matching the letter
        if guess in word:
            status = "match!!"
        else:
            status = "wrong guess..."
            TRIES -= 1
        #check win or loose
        if all(test in guessedLetter for test in word):
            gameWin = True
            break
        else:
            gameWin = False
    return gameWin

def gameEnd(gameWin):
    if gameWin:
        print("You are win!!!!")
    else:
        print("Sorry, try again")


def choosenWord():
    return random.choice(WORDSLIST)


def main():
    word = choosenWord()
    guessedLetter=[]
    status = "Let's start it.."
    gameWin = False

    gameWin= gameLoop(TRIES, word, guessedLetter, status)
    gameEnd(gameWin)


if __name__ =="__main__":
    main()
