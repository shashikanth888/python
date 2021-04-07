def rotate_2D(board):
    board[:] = list(map(list, zip(*board[::-1])))
    return board

def check_win(cur_board,i,j):
    if j >= len(cur_board[i]):
        i = i+1
        j = 0
    if i >= len(cur_board):
        return False
    if cur_board[i][j] >= 2048:
        return True
    return check_win(cur_board, i, j+1)
    

def left_recurr(arr, temp, i, j, previous, win):
    if i >= len(arr):
        if previous != None:
            temp[j] = previous
        return win
    if arr[i] != 0: # number different from zero
        if previous == None:
            previous = arr[i]
        else:
            if previous == arr[i]:
                if 2*arr[i] == 2048 and win == False:
                    win = True
                    print("You win!")
                temp[j] = 2 * arr[i]
                j += 1
                previous = None
            else:
                temp[j] = previous
                j += 1
                previous = arr[i]
    i = i+1
    return left_recurr(arr, temp, i, j, previous, win)

def move_left(arr, win):
    temp = [0]*len(arr)
    win = left_recurr(arr, temp, 0, 0, None, win)
    return temp, win

def move_2048(cur_board, d):
    win = check_win(cur_board, 0, 0)
    if d == "left":
        cur_board[0], win = move_left(cur_board[0], win)
        cur_board[1], win = move_left(cur_board[1], win)
        cur_board[2], win = move_left(cur_board[2], win)
        cur_board[3], win = move_left(cur_board[3], win)
    elif d == "down":
        cur_board = rotate_2D(cur_board)
        cur_board[0], win = move_left(cur_board[0], win)
        cur_board[1], win = move_left(cur_board[1], win)
        cur_board[2], win = move_left(cur_board[2], win)
        cur_board[3], win = move_left(cur_board[3], win)
        cur_board = rotate_2D(cur_board)
        cur_board = rotate_2D(cur_board)
        cur_board = rotate_2D(cur_board)
    elif d == "right":
        cur_board = rotate_2D(cur_board)
        cur_board = rotate_2D(cur_board)
        cur_board[0], win = move_left(cur_board[0], win)
        cur_board[1], win = move_left(cur_board[1], win)
        cur_board[2], win = move_left(cur_board[2], win)
        cur_board[3], win = move_left(cur_board[3], win)
        cur_board = rotate_2D(cur_board)
        cur_board = rotate_2D(cur_board)
    elif d == "up":
        cur_board = rotate_2D(cur_board)
        cur_board = rotate_2D(cur_board)
        cur_board = rotate_2D(cur_board)
        cur_board[0], win = move_left(cur_board[0], win)
        cur_board[1], win = move_left(cur_board[1], win)
        cur_board[2], win = move_left(cur_board[2], win)
        cur_board[3], win = move_left(cur_board[3], win)
        cur_board = rotate_2D(cur_board)
    else:
        print("invalid input")
    return sum(map(sum, cur_board))


A = [[16, 16, 4, 2], [4, 4, 0, 4], [0,16,16,16], [1024, 1024, 8, 0]]
print(move_2048(A, "right"))
print(A)