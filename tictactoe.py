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
            if answer > 9 or answer < 1:
                raise ValueError
            
            return answer
        except ValueError:
            print('Invalid input, try again')
            continue

def checkIfWon():
    # rows
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    
    # colums
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    
    # diagonals
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
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

def boardFull():
    for item in board:
        if item == ' ':
            return False
    
    return True
def compTurn():
    return random.randint(0, 9)

def replace(index, item, sub=False):
    if sub == True:
        index -= 1



def play():
    global board
    global game_still_going_on
    global takenSpots
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_still_going_on = True
    playerTurn = random.choice([True, False])
    greeting()
    while game_still_going_on:
        if playerTurn == True:
            replace(takeInputs(), 'X', sub=True)
            playerTurn = False
            continue
        else:
            # playerTurn == False
            replace(compTurn(), 'O')
            playerTurn = True
            continue

