import evaluator
import time
from cell import Cell
import puzzles

class Solver():

    def display(root,num,x,y):
        Cell.board_tiles[y][x].cell_obj.config(text=str(num), font='Helvetica 9 bold', fg = 'blue')
        root.update()
        time.sleep(.001)

    def solve_brute_force(root, board):
          if evaluator.valid_solution(board) == True:
              return board
          for x, a in enumerate(board):
              for y, b in enumerate(a):
                  if b == '0' or b == None or b ==' ':
                      for num in range(1,10):
                          board[x][y] = str(num)
                          #board_tiles ref for print num on screen
                          Solver.display(root,num,x,y)
                          if evaluator.valid_input(board, str(num), x, y) == True:
                              Solver.display(root,num,x,y)
                              Solver.solve_brute_force(root, board)
                              if evaluator.valid_solution(board) == True:
                                  return board
                              Solver.display(root,' ',x,y)
                              board[x][y] = '0'
                          else:
                              Solver.display(root,' ',x,y)
                              board[x][y] = '0'
                      return


    def solve_instant(board):
        for x, a in enumerate(board):
            for y, b in enumerate(a):
                if b == '0' or b == None or b ==' ':
                    Cell.board_tiles[y][x].cell_obj.config(
                    bg='#f1f1f1',
                    text=puzzles.solution[x][y],
                    font='Helvetica 9 bold', fg='green')
                    #line only for testing
                    puzzles.overwrite_puzzle(puzzles.solution[x][y], x, y)
                    #Testing only

    def logic_solve(board):
        pass
