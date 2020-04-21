#   Pete
#   Version 0.01
#   4/20/2020
#
#   MinMax algorithm
#   Will take the best path during the course of the game to avoid losing/win
#

import Board
import algDef
import algOff
from random import randint

#MinMax Algorithm Main Driver
def __init__(board):
    #Sets two Integers, offensive and defensive, to the best values respectively
    #Column is a last-ditch effort if there are no edges
    offensive = algOff.__init__(board, True)
    defensive = algDef.__init__(board, True)
    column = 0

    #Comparing the two before picking which position to take on the board
    if(offensive > defensive):
        return algOff.__init__(board, False)
    elif(defensive > offensive):
        return algDef.__init__(board, False)
    #If all else fails, will pick at random
    else:
        done = False
        while not done:
            column = randint(0, 6)
            if (board.search(5, column) == 0):
                done = True
        return column
