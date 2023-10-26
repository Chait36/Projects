def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)  #i - row  j - col
    return None


def solve_board(board):
    if isValidSudoku(board):
        temp = find_empty(board)
        if not temp:
            return True
        else:
            row,col = temp

        for i in range(1,10):
            if isValid(board, i, (row,col)):
                board[row][col] = i

                if solve_board(board):
                    return True
                
                board[row][col] = 0
    else:
        print('BOard is Not solvable')


def isValid(board,value,position):
    for i in range(len(board[0])):
        if board[position[0]][i] == value and i != position[1]:
            return False
        
        if board[i][position[1]] == value and i != position[0]:
            return False
        
        row_box = position[1]//3
        col_box = position[0]//3

        for i in range(col_box*3,col_box*3 + 3):
            for j in range(row_box*3,row_box*3 + 3):
                if board[i][j] == value and (i,j) != position:
                    return False
        return True


def print_all(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - -")

        for j in range(len(board[0])):
            if j%3 == 0 and j!=0:
                print('|',end = '')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def isValidSudoku(board):
    for i in range(9):
        # create empty dictionaries to keep track of row, column, and block values
        row = {}
        column = {}
        block = {}
        # calculate the starting index of the current 3x3 block
        row_cube = 3 * (i//3)
        column_cube = 3 * (i%3)
        for j in range(9):
            # check if the value in the current cell of the row is valid
            if board[i][j]!=0 and board[i][j] in row:
                return False
            row[board[i][j]] = 1  # add the value to the row dictionary
            
            # check if the value in the current cell of the column is valid
            if board[j][i]!=0 and board[j][i] in column:
                return False
            column[board[j][i]] = 1  # add the value to the column dictionary
            
            # calculate the row and column index of the current cell within the 3x3 block
            rc = row_cube+j//3
            cc = column_cube + j%3
            
            # check if the value in the current cell of the block is valid
            if board[rc][cc] in block and board[rc][cc]!=0:
                return False
            block[board[rc][cc]] = 1  # add the value to the block dictionary
    return True




'''input_board = []
for j in range(9):
    l = []
    for i in range(9):
        t = int(input())
        l.append(t)
    input_board.append(l)'''

input_board=  [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,7,7]
]



print_all(input_board)
solve_board(input_board)
print('___________________')
print_all(input_board)