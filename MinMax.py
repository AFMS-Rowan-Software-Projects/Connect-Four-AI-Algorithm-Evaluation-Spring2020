#   Pete
#   Version 0.03
#   4/30/2020
#
#   MinMax algorithm
#   Will take the best path during the course of the game to avoid losing/win
#

import Board
import Bot

#MinMax Algorithm Main Driver
def __init__(board, mode):
    #Sets two Integers, offensive and defensive, to the best values respectively
    #Column is a last-ditch effort if there are no edges
    defensive = Bot.__init__(board, 1, True, mode)
    offensive = Bot.__init__(board, 2, True, mode)

    #Comparing the two before picking which position to take on the board
    if(offensive[1] > defensive[1]):
        return offensive[0]
    elif(defensive[1] > offensive[1]):
        return defensive[0]
    #If all else fails, will pick at random
    else:
        return Bot.__init__(board, 0, False, False)

