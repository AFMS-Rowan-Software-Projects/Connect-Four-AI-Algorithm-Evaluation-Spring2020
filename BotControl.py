'''
Rajinder, Pete, Josh, Ian
Version 0.05
4/20/2020
Main Function
    Handles all the interactions between Game Function & Algorithms
    Selects the algorithm
'''
import algR
import algDef
import algOff
import algMinMax
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
        return defensive(board, False)
    elif key == 3:
        return offensive(board, False)
    elif key == 4:
        return minmax(board)




#Defines each algorithm and associates to the corresponding file
def random(board):
        return algR.__init__(board)
def defensive(board):
        return algDef.__init__(board, False)
def offensive(board):
        return algOff.__init__(board, False)
def minmax(board):
        return algMinMax.__init__(board)
