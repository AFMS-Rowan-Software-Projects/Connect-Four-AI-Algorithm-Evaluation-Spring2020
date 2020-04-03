import algDef
from Board import Board

board = []
grid = Board(True, board)
grid.__init__(True, board)
print("Row")
#Row
grid.set_board(0, 3, 1)
grid.set_board(0, 2, 2)
grid.set_board(0, 1, 1)
grid.set_board(1, 3, 1)
grid.set_board(1, 3, 2)
grid.set_board(0, 4, 2)
grid.printBoard()

algDef.__init__(grid, 5)