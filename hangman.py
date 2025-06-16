import random
import os
import json

#game MODE
TEST = "TESTING"
LAUNCH = "LAUNCH"

#Game mode selection
#------------------------------------------> SELECTED MODE
MODE = LAUNCH   # chose TEST or LAUNCH
#-------------------------------------------> SELECTED MODE
DEBUG = MODE == TEST  #checking selected mode.. it's "true" if TEST

#quick test
WORDSLIST = ['apple', 'banana', 'cranbarry']
#global variable
TRIES = 5


HANGMAN_PICS = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''
]


def clearScreen():
    if os.name == 'posix':
        os.system('clear')
    else:
        #assuming windows
        os.system('cls')


def display_text(word, guessedLetter, status, TRIES, category):
    #clean screen
    #print("\n" * 20)
    clearScreen()

    #game title and some header
    print("Welcome to Hangman!")
    print("===================")

    print(HANGMAN_PICS[5-TRIES])
    #status
    print("COMM: ", status)

    
    #hints
    hints= ""
    for letter in word:
        if letter in guessedLetter:
            hints += (letter + " ") 
        else:
            hints += ("_ ")
        
        
    print("Attempt(s) Remaining:", TRIES)
    print("Guessed Letters: ", guessedLetter)
    print(f"category: {category}")
    print("WORD: ", hints)
    
    if DEBUG:
        print(f"MODE:  {MODE}", f"choosen word is -----> {word} ")
       #print(guessedLetter)
    



 
def gameLoop(TRIES, word, guessedLetter, status, category):

    while(TRIES>0):

        display_text(word, guessedLetter, status, TRIES, category)
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

####GAME image
def print_bunny():
    print(r"""
     (\__/)
     (•ㅅ•)
     / 　 づ
    """)

def print_sad_face():
    print(r"""
    (｡•́︿•̀｡)
    """)


def gameEnd(gameWin, word):
    clearScreen()
    if gameWin:
        print_bunny()
        print("COMM:  You are win!!!!")
    else:
        print(HANGMAN_PICS[6])
        print_sad_face()
        print("Sorry, try again")
    print(f"Hidden word: {word}")
    print("\n"*5)


def choosenWord():
    #read a list base on category from a file
    with open("gameDictionary.json", "r") as file:
        data = json.load(file)
    categoryList = list(data.keys())

    num = 0
    for c in categoryList:
        print(f"{num+1}. {categoryList[num]}")
        num += 1
    categoryNum=int(input("Please select number of the category: "))
    category = categoryList[categoryNum-1]
    WORDSLIST = data.get(category,[])
    return category, random.choice(WORDSLIST) 

def main():
    category, word = choosenWord()
    guessedLetter=[]
    status = "Let's start it.."
    gameWin = False

    gameWin= gameLoop(TRIES, word, guessedLetter, status, category)
    gameEnd(gameWin, word)


if __name__ =="__main__":
    main()


