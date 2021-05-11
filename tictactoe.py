import random

def print_board():
    print(' {} | {} | {} '.format(board[0], board[1], board[2]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[3], board[4], board[5]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[6], board[7], board[8]))

def takeInputs():
    while True:
        answer = ''
        try:
            answer = int(input('Chose a index to put your piece(1-9): '))
            
            if answer not in takenSpots:
                if answer == 69420:
                    exit(0)
                if answer > 9 or answer < 1:
                    raise ValueError
            
                takenSpots.append(answer)
                return answer
            else:
                raise ValueError
        except ValueError:
            print('Invalid input, try again')
            continue

def boardFull():
    for item in board:
        if item == ' ':
            return False
    
    return True

def checkIfWon(value):
    # rows
    if board[0] == value and board[1] == value and board[2] == value:
        return True
    if board[3] == value and board[4] == value and board[5] == value:
        return True
    if board[6] == value and board[7] == value and board[8] == value:
        return True
    
    # colums
    if board[0] == value and board[3] == value and board[6] == value:
        return True
    if board[1] == value and board[4] == value and board[7] == value:
        return True
    if board[2] == value and board[5] == value and board[8] == value:
        return True
    
    # diagonals
    if board[0] == value and board[4] == value and board[8] == value:
        return True
    if board[2] == value and board[4] == value and board[6] == value:
        return True
    
    return False
    

def greeting():
    while True:
        print("Do you want to play?(y/n)")
        answer = input().lower()
        if answer == 'y':
            break
        elif answer == 'n':
            print("Then y u waste my time")
            exit(1)


def compTurn():
    return random.randint(0, 9)

def replace(index, item, sub=False):
    if sub == True:
        index = index - 1
    
    if board[index] == ' ':
        board[index] = item

def play():
    global board
    global game_still_going_on
    global takenSpots
    takenSpots = []
    won = ''
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_still_going_on = True
    playerTurn = True
    greeting()
    while game_still_going_on:
        if checkIfWon('X'):
            won = 'X'
            game_still_going_on = False
        elif checkIfWon('O'):
            won = 'O'
            game_still_going_on = False
        elif playerTurn == True:
            print_board()
            replace(takeInputs(), 'X', sub=True)
            playerTurn = False
            continue
        else:
            # playerTurn == False
            replace(compTurn(), 'O')
            playerTurn = True
            continue
    
    if not game_still_going_on:
        if checkIfWon('X'):
            print('YOU WON')
        elif checkIfWon('O'):
            print('YOU LOST')
        else:
            print('DRAW')

play()
