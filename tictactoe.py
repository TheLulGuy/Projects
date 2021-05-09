import random

def winning(choices, value):
    if choices[0] and choices[1] and choices[2] == value:
        return True

    elif choices[3] and choices[4] and choices[5] == value:
        return True
    
    elif choices[6] and choices[7] and choices[8] == value:
        return True
    
    elif choices[0] and choices[4] and choices[8] == value:
        return True
    
    elif choices[2] and choices[4] and choices[8] == value:
        return True
    
    else:
        return False

def printBoard(choices):
    board = """ 
 {} | {} | {} 
---+---+---
 {} | {} | {} 
---+---+---
 {} | {} | {} """.format(choices[0] ,choices[1] ,choices[2] ,choices[3] ,choices[4] ,choices[5] ,choices[6] ,choices[7] ,choices[8])
    print(board)

def start():
    choices = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    computerChoice = ''
    playerChoice = None
    playerTurn = True
    gameEnded = False

    while True:
        if playerTurn:
            printBoard(choices)
            playerChoice = int(input('It is your turn! Enter a shell value: '))
            choices[playerChoice] = 'X'
            if winning(choices, 'X') == False:
                playerTurn = False
            
            else:
                print('You Won! ')
                printBoard(choices)
                gameEnded = True
                break
        
        elif playerTurn == False:
            printBoard(choices)
            emptySpaces = [i for i, shell in enumerate(choices)]
            computerChoice = random.choice(emptySpaces)
            choices[computerChoice] = 'O'
            if winning(choices, 'O') == False:
                playerTurn = True
            
            else:
                print('You lose!')
                gameEnded = True
                break
        elif gameEnded == True:
            break

if __name__ == "__main__":
    start()

while True:
    answer = input('Want to play again?(Y/N)').upper()
    if answer == 'Y':
        gameEnded = False
        start()
    elif answer == 'N':
        break
    else:
        print('Enter a valid input')

