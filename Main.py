from tkinter import *
import settings
from PIL import Image, ImageTk
from cell import Cell
import puzzles
from solve import Solver
import copy


colour_palette = ['#E5FCC2', '#594F4F', '#547980', '#45ADA8']
gradient_arr=[['#eea229',
'#e2a325',
'#d6a422',
'#caa420',
'#bea421',
'#b2a323',
'#a6a326',
'#9ba22a',
'#90a12e',
'#859f33',
'#7a9e37',
'#709c3c',
'#659a41',
'#5b9846',
'#51954b',
'#46934f',
'#3c9054',
'#318d58',
'#258a5c',
'#178760',
'#028463',
'#008166',
'#007e69',
'#007b6b',
'#00776c',
'#00746e',
'#00706e',
'#006d6f',
'#00696e',
'#00656e',
'#00626c',
'#005e6b',
'#0b5a69',
'#155666',
'#1c5363',
'#224f60',
'#264c5c',
'#2a4858'],
['#245808',
'#285b09',
'#2c5f0b',
'#2f620d',
'#33650e',
'#376910',
'#3b6c11',
'#3f6f13',
'#437314',
'#477616',
'#4b7a17',
'#4f7d19',
'#53801a',
'#57841c',
'#5b871d',
'#5f8b1e',
'#638e20',
'#679221',
'#6c9523',
'#709924',
'#749c26',
'#79a027',
'#7da329',
'#82a72a',
'#86aa2c',
'#8bae2d',
'#8fb12f',
'#94b530',
'#98b832',
'#9dbc33',
'#a2bf35',
'#a7c336',
'#abc638',
'#b0ca3a',
'#b5cd3b',
'#bad13d',
'#bfd43e',
'#c4d840'],
['#d05785',
'#cf5889',
'#ce598d',
'#cc5b92',
'#ca5c96',
'#c85e9a',
'#c6609e',
'#c461a2',
'#c263a5',
'#bf65a9',
'#bd67ad',
'#ba69b0',
'#b76bb3',
'#b36db7',
'#b06fba',
'#ad71bd',
'#a973c0',
'#a575c2',
'#a176c5',
'#9d78c7',
'#997aca',
'#957ccc',
'#907ece',
'#8c80cf',
'#8782d1',
'#8284d3',
'#7d85d4',
'#7887d5',
'#7389d6',
'#6e8ad7',
'#698cd8',
'#638ed8',
'#5e8fd8',
'#5891d9',
'#5292d9',
'#4c93d9',
'#4695d8',
'#4096d8'],
['#ebf315',
'#eced06',
'#ece700',
'#ede100',
'#eddb00',
'#edd600',
'#edd000',
'#edca00',
'#ecc400',
'#ecbe00',
'#ebb800',
'#eab300',
'#eaad00',
'#e9a700',
'#e7a100',
'#e69b00',
'#e59600',
'#e39000',
'#e28a00',
'#e08400',
'#de7f00',
'#dc7900',
'#da7300',
'#d76d00',
'#d56800',
'#d36200',
'#d05c00',
'#cd5600',
'#ca5000',
'#c74a00',
'#c44400',
'#c13e00',
'#be3702',
'#ba3105',
'#b72a07',
'#b3220a',
'#b0190c',
'#ac0e0e'],
['#ffffff',
'#f7f7f7',
'#f0f0f0',
'#e8e8e8',
'#e0e0e0',
'#d9d9d9',
'#d1d1d1',
'#cacaca',
'#c3c3c3',
'#bbbbbb',
'#b4b4b4',
'#adadad',
'#a6a6a6',
'#9f9f9f',
'#989898',
'#919191',
'#8a8a8a',
'#838383',
'#7c7c7c',
'#757575',
'#6f6f6f',
'#686868',
'#626262',
'#5b5b5b',
'#555555',
'#4e4e4e',
'#484848',
'#424242',
'#3c3c3c',
'#363636',
'#303030',
'#2b2b2b',
'#252525',
'#202020',
'#1a1a1a',
'#151515',
'#0e0e0e',
'#050505'],
['#21e3ea',
'#13e4e8',
'#00e5e5',
'#00e6e3',
'#00e7e0',
'#00e8dc',
'#00e8d9',
'#00e9d5',
'#00ead2',
'#00eace',
'#00ebca',
'#00ecc5',
'#00ecc1',
'#0cedbc',
'#1cedb7',
'#28eeb2',
'#32eead',
'#3beea8',
'#44eea2',
'#4cef9d',
'#54ef97',
'#5bef91',
'#63ef8b',
'#6aef85',
'#71ef7f',
'#78ef79',
'#7fee73',
'#85ee6c',
'#8cee66',
'#93ed5f',
'#9aed59',
'#a0ec52',
'#a7ec4b',
'#aeeb43',
'#b5ea3c',
'#bbe933',
'#c2e82a',
'#c9e720'],
['#2a012a',
'#2b042d',
'#2d0630',
'#2e0833',
'#300b37',
'#310e3a',
'#33103d',
'#341340',
'#351544',
'#371847',
'#381b4b',
'#391d4e',
'#3a2051',
'#3b2255',
'#3c2558',
'#3d275c',
'#3d2a5f',
'#3e2d63',
'#3f2f66',
'#3f326a',
'#40356d',
'#403771',
'#403a74',
'#413d78',
'#413f7b',
'#41427f',
'#414583',
'#414886',
'#404a8a',
'#404d8d',
'#405091',
'#3f5394',
'#3e5698',
'#3e599b',
'#3d5b9f',
'#3c5ea2',
'#3b61a6',
'#3964a9',
'#3867ad',
'#366ab0'],
['#fff370',
'#f3ed6e',
'#e8e86c',
'#dde26a',
'#d2dc69',
'#c7d667',
'#bdd066',
'#b3ca64',
'#a9c463',
'#9fbe61',
'#96b860',
'#8db25e',
'#85ac5d',
'#7ca55b',
'#749f5a',
'#6c9958',
'#659356',
'#5d8c54',
'#568652',
'#508050',
'#497a4e',
'#43734c',
'#3d6d49',
'#386747',
'#336144',
'#2e5b41',
'#2a543e',
'#264e3b',
'#224837',
'#1e4234',
'#1b3d30',
'#19372d',
'#163129',
'#142b25',
'#122621',
'#10201c',
'#0d1b18',
'#091613',
'#040f0d',
'#000605'],
['#32dcd2',
'#11dad5',
'#00d8d9',
'#00d7dc',
'#00d5e0',
'#00d3e4',
'#00d1e8',
'#00ceeb',
'#00ccef',
'#00caf3',
'#00c7f6',
'#00c5fa',
'#00c2fd',
'#00bfff',
'#00bdff',
'#00baff',
'#00b7ff',
'#00b4ff',
'#00b0ff',
'#00adff',
'#00a9ff',
'#00a6ff',
'#00a2ff',
'#009eff',
'#009aff',
'#1095ff',
'#3791ff',
'#4d8cff',
'#5e87ff',
'#6d82ff',
'#7a7cfd',
'#8676f8',
'#9170f3',
'#9b6aee',
'#a563e7',
'#ae5ce1',
'#b654d9',
'#bd4cd2',
'#c443ca',
'#ca39c1']]


def new_game(loc):
    loc.destroy()
    puzzles.new_puzzle()
    Cell.board_tiles = [[None for y in range(9)] for x in range(9)]
    main()

def refresh_game(loc):
    loc.destroy()
    puzzles.reset_puzzle_copies()
    main()

def main():
    root = Tk()
    root.configure(bg=colour_palette[2])
    root.geometry(f'{settings.FRAME_WIDTH}x{settings.FRAME_HEIGHT}')
    root.title("Sudoku")
    root.resizable(True, True)
    root.bind('<1>', lambda event: Cell.left_click_action)

    # img_path = 'C:/Users/Spencer/.atom/Code/Sudoku/images/image.ico'
    # img = Image.open(img_path)
    # img = img.resize((18, 18), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img)

    game_frame = Frame(root, bg = colour_palette[2],
                    bd = 2,
                    width = settings.width_pct(100),
                    height = settings.height_pct(10))
    game_frame.grid(row=0, column=0, padx=(20,0))

    new_game_btn = Button(game_frame, text = 'New \n Game ',
                    command = lambda: new_game(root), pady=5)
    new_game_btn.grid(row=0, column=0, ipadx=1, pady=(3,8), padx=(5,5))

    clear_game_btn = Button(game_frame, text = 'Clear \n Inputs ',
                    command = lambda: refresh_game(root), pady=5)
    clear_game_btn.grid(row=0, column=5, ipadx=1, pady=(3,8), padx=(5,5))

    brute_solve_btn = Button(game_frame, text = 'Solve \n Brute Force ',
                    command = lambda: Solver.solve_brute_force(root, puzzles.puzzle_tosolve), pady=5)
    brute_solve_btn.grid(row=0, column=10, ipadx=1, pady=(3,8), padx=(5,5))

    logic_solve_btn = Button(game_frame, text = 'Solve \n Logically ',
                    font='Helvetica 9 bold', bg='#d6d6d6', relief = SUNKEN,
                    command = lambda: Solver.logic_solve(root), pady=5)
    logic_solve_btn.grid(row=0, column=15, ipadx=1, pady=(3,8), padx=(5,5))

    instant_solve_btn = Button(game_frame, text = 'Solve \n Instantly ',
                    command = lambda: Solver.solve_instant(copy.deepcopy(puzzles.puzzle_tosolve)), pady=5)
    instant_solve_btn.grid(row=0, column=20, ipadx=1, pady=(3,8), padx=(5,5))

    submit_btn = Button(game_frame, text = 'Submit \n Board ',
                    command = lambda: Cell.submit(root, puzzles.puzzle, gradient_arr), pady=5)
    submit_btn.grid(row=0, column=25, ipadx=1, pady=(3,8), padx=(5,5))

    # hint_radio_btn = Radiobutton(root, text = 'Hints', indicator=0,
    #                 command = lambda: Cell.submit(root, puzzles.puzzle, gradient_arr), pady=5)
    # hint_radio_btn.grid(row=1, column=0, ipadx=1, pady=(8,8), padx=(0,5))

    middle_frame = Frame(root, bg = colour_palette[1], bd = 2,
                    width = settings.width_pct(80),
                    height = settings.height_pct(80))
    middle_frame.place(x = settings.width_pct(10), y = settings.height_pct(12))

    bottom_frame = Frame(root, bg = colour_palette[2], bd = 2,
                    width = settings.width_pct(100),
                    height = settings.height_pct(10))
    bottom_frame.place(x = settings.width_pct(3), y = settings.height_pct(90))

    # Generate Puzzle
    # Cell generation and placement
    for y in range(settings.COLS):
        for x in range(settings.ROWS):
            if puzzles.puzzle[y][x] != '0':
                c = Cell(y,x,locked=True)
            else:
                c = Cell(y,x)
            c.create_cell(middle_frame,puzzles.puzzle[y][x])
            #Create border between 3x3 cells
            if x % 3 == 0:
                c.cell_obj.grid(column = x, row = y, padx=(5,0))
            if x == 8:
                c.cell_obj.grid(column = x, row = y, padx=(0,5))
            if y % 3 == 0:
                c.cell_obj.grid(column = x, row = y, pady=(5,0))
            if y == 8:
                c.cell_obj.grid(column = x, row = y, pady=(0,5))
            else:
                c.cell_obj.grid(column = x, row = y)
    for x in range(1,10):
        c = Cell((int(x)+11),int(y)+11, name=str(x), is_board=False)
        c.create_cell(bottom_frame,x,btn_relief=RAISED)
        c.cell_obj.grid(column=x,row=y,padx=6)
    root.mainloop()

if __name__ == '__main__':
    main()
