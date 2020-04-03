import gameFunction
from Board import Board


gameFunction
board = []
grid = Board(True, board)
grid.__init__(True, board)
grid.set_board(0, 3, 1)
grid.set_board(1, 2, 1)
grid.set_board(2, 1, 1)
grid.set_board(3, 0, 1)
grid.printBoard()
print(grid.search(0,0))
print(gameFunction.checkWin(grid))