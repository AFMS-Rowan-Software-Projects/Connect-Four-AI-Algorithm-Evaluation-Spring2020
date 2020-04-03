'''
Rajinder & Pete
2/19/2020
version 0

'''

from random import randint
from Board import Board

#initializing any function needed to determine the col to place
def __init__(board):
    return pickCol(board)

#Selects the col to place into
def pickCol(board):
    col = randint(0,6)
    if board.search(5, col) != 0:
        while True:
            col = randint(0, 6)
            print("i'm stuck yo, help")
            if board.search(5, col) == 0:
                print("i'm free yo thanks")
                break
    return col