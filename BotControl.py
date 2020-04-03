'''
Rajinder & Pete
Version 0
2/19/2020
Main Function
    Handles all the interactions between Game Function & Algorithms
    Selects the algorithm
'''
import algR
from Board import Board

selCol = -1 # Selected Column by the algorithm ( Default value of -1 for error checking)
algnum = 1 # Chooses algorithm (Make sure to only change when game is won or loss)

#Constructor
def __init__(key, board):
    selCol = selectAlgorithm(key, board)
    return selCol

#Selects the appropriate algorithm
def selectAlgorithm(key, board):
    if key == 1:
        return random(board)
    elif key == 2:
        return "Haha yup"
    elif key == 3:
        return "No chance"
    elif key == 4:
        return "*crying*"




#Defines each algorithm and associates to the corresponding file
def random(board):
        return algR.__init__(board)
def defensive():
        return "file"
def offensive():
        return "file"
def minmax():
        return "file"
