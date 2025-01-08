from tkinter import *
import puzzles
import evaluator
import time
import random

class Cell:
    board_tiles=[[None for y in range(9)] for x in range(9)]
    active_tile = None
    def __init__(self, x, y, name=None, locked=False, is_board=True):
        self.cell_obj = None
        self.x = x
        self.y = y
        self.name= name
        self.locked=locked
        self.is_board = is_board
        if self.is_board==True:
            Cell.board_tiles[y][x] = self


    def create_cell(self, frame, number, btn_relief=SUNKEN):
        if number == '0':
            number = ' '
        b = Button(frame, text=str(number), width=4,
                height=2, border = 1,
                bg='#f1f1f1' , relief=btn_relief)
        b.bind('<Button-1>', self.left_click_action)
        b.bind('<Button-3>', self.right_click_action)
        self.cell_obj = b
        if self.locked == True:
            self.cell_obj.config(font='Helvetica 9 bold', bg='#d6d6d6')


    def left_click_action(self, event):
        # Highlights and activates cell
        if self.is_board == True and self.locked == False and Cell.active_tile == None:
            Cell.active_tile = self
            self.cell_obj.config(bg='khaki')
        # Handles any old highlights and incorrect inputs / Highlights and activates new cell
        elif self.is_board == True and self.locked == False and Cell.active_tile != None:
            if evaluator.valid_input(puzzles.puzzle, Cell.active_tile.cell_obj['text'], Cell.active_tile.x, Cell.active_tile.y) == False:
                Cell.active_tile.cell_obj.config(bg='#e35d73')
            else:
                Cell.active_tile.cell_obj.config(bg='#f1f1f1')
            Cell.active_tile = self
            self.cell_obj.config(bg='khaki')
        # Writes number into active cell / commits number to memory
        elif self.is_board == False and self.locked == False and Cell.active_tile != None:
            #Add self.name (number) to the puzzle array
            puzzles.overwrite_puzzle(self.name, Cell.active_tile.x, Cell.active_tile.y)
            #Add self.name (number) to the tile
            Cell.active_tile.cell_obj.config(bg='#f1f1f1', text=self.name)
            #Add evaluator to evaluate and highlight red if false.
            if evaluator.valid_input(puzzles.puzzle, self.name, Cell.active_tile.x, Cell.active_tile.y) == False:
                Cell.active_tile.cell_obj.config(bg='#e35d73')
            Cell.active_tile = None
        else:
            pass


    def right_click_action(self, event):
        if self.is_board == True and self.locked == False:
            #Remove highlight and tile number
            self.cell_obj.config(text=' ', bg='#f1f1f1')
            #Remove self.name(number) from puzzle array
            puzzles.overwrite_puzzle('0', self.x, self.y)
            Cell.active_tile=None

    @staticmethod
    def end_game(root, board, gradient, count=0):
        # Zip to use rows rather than columns
        for k, a in enumerate(list(a) for a in zip(*Cell.board_tiles)):
            # Alternate sides of gradient row fill animation
            for b in a[::[1,-1][count%2]]:
                # gradient flow animation
                i = [1,-1][int((k+count)/len(gradient))%2]
                b.cell_obj.config(bg=gradient[::i][(k+count)%len(gradient)])
                root.update()
        count +=1
        # Don't break max recursion depth (980)
        if count < 980:
            Cell.end_game(root, board, gradient, count=count)

    # Evaluates the board for completion sequence
    @staticmethod
    def submit(root, board, gradient_arr):
        # 'Background' is array to store current cell backgrounds for ref
        background = [[None for y in range(9)] for x in range(9)]
        # Create endgame effect
        if evaluator.valid_solution(board):
            # Lock all board tiles, game is done
            for y in Cell.board_tiles:
                for x in y:
                    x.locked = True
                    x.cell_obj.config(fg='white')
            # Pick a random end game gradient
            gradient = gradient_arr[random.randint(0,len(gradient_arr)-1)]
            Cell.end_game(root, board, gradient)
        #flash bg to red for 2.5sec then return to former bg
        else:
            for y, a in enumerate(Cell.board_tiles):
                for x, b in enumerate(a):
                    if b.locked == False:
                        background[y][x] = b.cell_obj['bg']
                        b.cell_obj.config(bg='#e35d73')
            root.update()
            time.sleep(2.5)
            for y, a in enumerate(Cell.board_tiles):
                for x, b in enumerate(a):
                    if b.locked == False:
                        b.cell_obj.config(bg=background[y][x])
