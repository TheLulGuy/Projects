# Sample board
board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,8,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,4,0,0,0,0,0],
    [0,0,0,0,8,0,0,0,0]
]

# Using recursion
def solve(board):
    find = find_empty(board)
    # This means the board is solved
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        # Checks if the number is valid and adds it in the board
        if valid(board, i, (row, column)):
            board[row][column] = i

        # Recursion, repeating the numbering process
        # If solve is False, then the number becomes 0 and backtracking occurs
            if solve(board):
                return True
        
            board[row][column] = 0
    # If recursion doesnt work, it returns False and starts the backtracking
    return False


def valid(board, num, pos):
    # Check row
    # you can write 9 instead of len board as well, i used this so that its compatible with bigger sudoku board
    for i in range(len(board[0])): 
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Checks the elements in the box
    # E.g. let the box_y is 1, thus the first number in the box starts with index 3 or 1 * 3
    # and the last number has index 5, but that is 1 * 3 + 3 - 1. But since for loops dont include the last 
    # number in ranges, the loop will iterate till 5
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')
        
        for j in range(9): #  Iterates through the items of each row
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print('-----------------------------------------------------')
print_board(board)
