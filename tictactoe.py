import random

def print_board(board):
    print(' {} | {} | {} '.format(board[0], board[1], board[2]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[3], board[4], board[5]))
    print('---+---+---')
    print(' {} | {} | {} '.format(board[6], board[7], board[8]))

def greeting():
    while True:
        print("Do you want to play?(y/n)")
        answer = input().lower()
        if answer == 'y':
            break
        elif answer == 'n':
            print("Then y u waste my time")
            exit(1)



def play():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
    playerTurn = random.choice([True, False])
    greeting()


if __name__ == '__main__':
    play()