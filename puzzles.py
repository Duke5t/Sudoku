import random
import pandas as pd
import copy
import csv

puzzle_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'sudoku.csv'))
file = open(puzzle_file, 'r')
puzzle_raw = list(csv.reader(file, delimiter=','))
file.close()

# puzzle_raw = ['070000043040009610800634900094052000358460020000800530080070091902100005007040802','679518243543729618821634957794352186358461729216897534485276391962183475137945862',
# '301086504046521070500000001400800002080347900009050038004090200008734090007208103','371986524846521379592473861463819752285347916719652438634195287128734695957268143']

puzzle=[]
solution=[]
puzzle_copy = []
puzzle_tosolve = []
#take raw data and standardize it for use in program
def new_puzzle():
    global puzzle
    global puzzle_copy
    global solution
    puzzle = []
    solution = []
    # Generate random puzzle set - index 0 is puzzle - index 1 is solution
    randpuzzle = puzzle_raw[random.randrange(0,len(puzzle_raw))]
    newpuzzle, newsolution = randpuzzle[0], randpuzzle[1]
    #make 9 lines of 9 (9x9 array)
    for x in range(9):
        puzzle.append([a for a in newpuzzle[x*9:(x+1)*9]])
        solution.append([a for a in newsolution[x*9:(x+1)*9]])
    #make puzzlecopy for referencing puzzle prior to changes
    puzzle_copy = copy.deepcopy(puzzle)
    reset_puzzle_copies()

def reset_puzzle_copies():
    global puzzle_copy
    global puzzle_tosolve
    global puzzle
    #reset an altered puzzle back to unchanged original puzzle
    puzzle = puzzle_copy
    #make puzzlecopy for referencing puzzle prior to changes
    puzzle_copy = copy.deepcopy(puzzle)
    #make puzzle copy for reference for solver functions
    puzzle_tosolve = copy.deepcopy(puzzle)

new_puzzle()

def overwrite_puzzle(number, x, y):
    puzzle[x][y] = str(number)


# puzzle[:len(puzzle)/8].to_csv('C:\PythonCode\Sudoku\sudoku1.csv')
