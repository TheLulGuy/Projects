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
            
            if answer == 69:
                exit(0)
            elif answer > 9 or answer < 1:
                raise ValueError

            return answer
        except ValueError:
            print('Invalid input, try again')
            continue

def checkIfWon():
    # rows
    if board[0] == board[1] == board[2]:
        return True, board[0]
    if board[3] == board[4] == board[5]:
        return True, board[4]
    if board[6] == board[7] == board[8]:
        return True, board[8]
    
    # colums
    if board[0] == board[3] == board[6]:
        return True, board[0]
    if board[1] == board[4] == board[7]:
        return True, board[4]
    if board[2] == board[5] == board[8]:
        return True, board[8]
    
    # diagonals
    if board[0] == board[4] == board[8]:
        return True, board[4]
    if board[2] == board[4] == board[6]:
        return True, board[4]
    
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
        index = index - 1
    
    if board[index] == ' ':
        board[index] = item

def play():
    global board
    global game_still_going_on
    global takenSpots
    winning = ''
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_still_going_on = True
    playerTurn = random.choice([True, False])
    greeting()
    while game_still_going_on:
        game_still_going_on, winning = checkIfWon()
        if playerTurn == True:
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
        if winning == 'X':
            print('YOU WON')
        else:
            print('YOU LOST')

play()
