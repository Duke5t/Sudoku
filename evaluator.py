
#Sudoku Solver
#Given an array of 9 x 9 : returns whether or not the array is correct
pp = [  ['3', '7', '1', '9', '8', '6', '5', '2', '4'],
        ['2', '0', '6', '5', '0', '1', '3', '7', '9'],
        ['5', '9', '0', '4', '7', '3', '8', '6', '1'],
        ['4', '6', '3', '8', '1', '9', '7', '5', '2'],
        ['0', '8', '5', '3', '4', '7', '9', '1', '6'],
        ['7', '1', '9', '6', '5', '2', '4', '3', '8'],
        ['6', '3', '4', '1', '9', '5', '2', '8', '7'],
        ['1', '2', '8', '7', '3', '4', '6', '9', '5'],
        ['9', '5', '7', '2', '6', '8', '1', '4', '3']]

pp = [  ['0', '7', '0', '0', '0', '0', '0', '4', '3'],
        ['0', '4', '0', '0', '0', '9', '6', '1', '0'],
        ['8', '0', '0', '6', '3', '4', '9', '0', '0'],
        ['0', '9', '4', '0', '5', '2', '0', '0', '0'],
        ['3', '5', '8', '4', '6', '0', '0', '2', '0'],
        ['0', '0', '0', '8', '0', '0', '5', '3', '0'],
        ['0', '8', '0', '0', '7', '0', '0', '9', '1'],
        ['9', '0', '2', '1', '0', '0', '0', '0', '5'],
        ['0', '0', '7', '0', '4', '0', '8', '0', '2']]

pp =[   ['3', '0', '1', '0', '8', '6', '5', '0', '4'],
        ['0', '4', '6', '5', '2', '1', '0', '7', '0'],
        ['5', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['4', '0', '0', '8', '0', '0', '0', '0', '2'],
        ['0', '8', '0', '3', '4', '7', '9', '0', '0'],
        ['0', '0', '9', '0', '5', '0', '0', '3', '8'],
        ['0', '0', '4', '0', '9', '0', '2', '0', '0'],
        ['0', '0', '8', '7', '3', '4', '0', '9', '0'],
        ['0', '0', '7', '2', '0', '8', '1', '0', '3']]

def valid_input(board, num, x, y):
    row = []
    col = []
#check rows for duplicate numbers
    if board[x].count(num) > 1:
        return False
#check cols for dup #s
    if [list(a) for a in (zip(*board))][y].count(num) > 1:
        return False
#check 3x3 for dup #s
    sqx = x - x % 3
    sqy = y - y % 3
    sqboard = []
    for a in board[sqx:sqx+3]:
        sqboard += a[sqy:sqy+3]
    if sqboard.count(num) > 1:
        return False
    return True


def valid_solution(board):
    sol = ['1','2','3','4','5','6','7','8','9']
    for x in board:
        if '0' in x:
            return False
#check rows for duplicate numbers
    for row in board:
        if sorted(row) != sol:
            return False
#check cols for dup #s
    for col in [list(a) for a in (zip(*board))]:
        if sorted(col) != sol:
            return False
#check 3x3 for dup #s
    a, b, c = [], [] ,[]
    for k,x in enumerate(board,start=1):
        a += x[0:3]
        b += x[3:6]
        c += x[6:9]
        if k%3 == 0:
            for z in [a, b, c]:
                if sorted(z) != sol:
                    return False
            a,b,c = [], [] ,[]
    return True


def solve_brute_force(board):
    if valid_solution(board) == True:
        return board
    for x, a in enumerate(board):
        for y, b in enumerate(a):
            if b == '0' or b == None or b ==' ':
                for num in range(1,10):
                    board[x][y] = str(num)
                    if valid_input(board, str(num), x, y) == True:
                        solve_brute_force(board)
                        if valid_solution(board) == True:
                            return board
                        board[x][y] = '0'
                    else:
                        board[x][y] = '0'
                return




# print(valid_solution(p))
# print(solve_brute_force(pp))
# print(valid_input(pp, '8', 0, 2))
# print(valid_solution(pp))
