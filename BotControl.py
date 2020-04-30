'''
Rajinder, Pete, Josh, Ian
Version 0.8
4/30/2020
Main Function
    Handles all the interactions between Game Function & Algorithms
    Selects the algorithm
'''
import Bot
import MinMax
from Board import Board

selCol = -1 # Selected Column by the algorithm ( Default value of -1 for error checking)
algnum = 1 # Chooses algorithm (Make sure to only change when game is won or loss)

#Constructor
def __init__(key, board, turn, mode):
    if key is 1:
        selCol = selectAlgorithm(key, board, False)
        return selCol
    elif key is not 1:
        if turn < 1:
            return 3
        else:
            selCol = selectAlgorithm(key, board, mode)
            return selCol

#Selects the appropriate algorithm
def selectAlgorithm(key, board, mode):
    if key == 1:
        return random(board)
    elif key == 2:
        return defensive(board, mode)
    elif key == 3:
        return offensive(board, mode)
    elif key == 4:
        return minmax(board, mode)




#Defines each algorithm and associates to the corresponding file
def random(board):
        return Bot.__init__(board, 0, False, False)
def defensive(board, mode):
        return Bot.__init__(board, 1, False, mode)
def offensive(board, mode):
        return Bot.__init__(board, 2, False, mode)
def minmax(board, mode):
        return MinMax.__init__(board, mode)

