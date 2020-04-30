'''
Rajinder, Pete, Josh, Ian
Version 0.6
4/29/2020
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
def __init__(key, board, turn):
    if key is 1:
        selCol = selectAlgorithm(key, board)
        return selCol
    elif key is not 1:
        if turn < 1:
            return 3
        else:
            selCol = selectAlgorithm(key, board)
            return selCol

#Selects the appropriate algorithm
def selectAlgorithm(key, board):
    if key == 1:
        return random(board)
    elif key == 2:
        return defensive(board)
    elif key == 3:
        return offensive(board)
    elif key == 4:
        return minmax(board)




#Defines each algorithm and associates to the corresponding file
def random(board):
        return Bot.__init__(board, 0, False)
def defensive(board):
        return Bot.__init__(board, 1, False)
def offensive(board):
        return Bot.__init__(board, 2, False)
def minmax(board):
        return MinMax.__init__(board)
