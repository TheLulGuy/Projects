""" 
//TODO: Make a file which has the list of words
//TODO: Make a seperator line
//TODO: Make a random word selector
//TODO: Make a function which contains the interface of the hangman
//TODO: Make a function which replaces items in the blank word
TODO: Make a function which starts the game and controls the tries, wrong letters, etc.
TODO: Make a functioning version of hangman
TODO: Add finishing touches:
    //TODO: Make a function which takes a difficulty input from the user
    TODO: Make a variable called tries which lists out the amount of tries the user has left and the total tries according to difficulty

TODO: Finished the Game!
"""

import random
from time import sleep

def line():
    print('______________________________________')

def difficulty():
    print('Enter difficulty: baby, easy, normal, hard or random')
    possibleAnswers = ['baby', 'easy', 'normal', 'hard']
    while True:
        answer = input('> ').lower()
        if answer not in possibleAnswers:
            print('Enter valid difficulty')
            continue
        elif answer == 'random':
            answer = random.choice(possibleAnswers)
        else:
            break
    return answer


def replacer(blankWord, item, selectedWord):
    bList = blankWord.split()
    index = selectedWord.index(item)
    bList.remove(bList[index*2])
    bList.insert(index*2, item)
    return bList

def interface(attempt, totalTries, blankWord, wrongList):
    line()
    print(f'Attempt no.: {attempt}/{totalTries}')
    print(f'Current: {blankWord}')
    print(f'Wrong: {wrongList}')

def converter(selectedWord):
    pass

def checker(blankWord, selectedWord):
    if blankWord.split() == selectedWord.split():
        return True
    else:
        return False


selectedWord = 'drain' 