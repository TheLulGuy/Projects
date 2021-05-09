import random

def interface(attempt, blankWord, wrongList):
    print('________________________________________________')
    print('Attempts left {}'.format(attempt))
    print('Word: {}'.format(blankWord))
    print('Wrong: {}'.format(wrongList))

def converter(chosenWord):
    blankWord = '- '*len(chosenWord)
    return blankWord

def replacer(blankWord, chosenWord, letter):
    index = chosenWord.index(letter)
    index *= 2
    item = blankWord[index]
    blankWord = blankWord.replace(item, letter)
    return blankWord

def start(chosenWord):
    pass


chosenWord = 'drain' # - - - - - 

