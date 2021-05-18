import random


def print_board():
    print(' {} | {} | {} '.format(board[0], board[1], board[2]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[3], board[4], board[5]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[6], board[7], board[8]))

def chooseDifficulty():
    while True:
        dif = input('Easy or hard?').lower()
        if dif == 'easy':
            return False
        elif dif == 'hard':
            return True
        else:
            print('Invalid input')

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
    
def checkIfDraw():
    if boardFull():
        if not checkIfWon('X') or not checkIfWon('O'):
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
    while True:
        a = random.randint(0, 8)
        if board[a] != ' ':
            continue
        else:
            return a

def replace(index, item, sub=False):
    if sub == True:
        index = index - 1
    
    if board[index] == ' ':
        board[index] = item

def minimax(board, depth, isMaximizing):
    if checkIfWon('O'):
        return 100

    elif checkIfWon('X'):
        return -100

    elif checkIfDraw():
        return 0
    
    if isMaximizing:
        bestScore = -1000

        for i in range(len(board)):
            if(board[i] == ' '):
                board[i] = 'O' 
                score = minimax(board, 0, False)
                board[i] = ' '
                if(score > bestScore):
                    bestScore = score
        
        return bestScore
        
    else:
        bestScore = 800

        for i in range(len(board)):
            if(board[i] == ' '):
                board[i] = 'X' 
                score = minimax(board, 0, True)
                board[i] = ' '
                if(score > bestScore):
                    bestScore = score
        
        return bestScore



def GeniusComputerMove():
    bestScore = -1000
    bestMove = 0

    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = 'O' 
            score = minimax(board, 0, False)
            board[i] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = i
    
    return bestMove

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
    difficulty = chooseDifficulty()
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
            if difficulty:
                replace(GeniusComputerMove(), 'O')
            else:
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
        print('\nFinal board position: ')
        print_board()

play()

