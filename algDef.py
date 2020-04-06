# Rajinder , Pete, Josh, Ian
#   Version 0.02
#   4/5/2020
#
# Defensive algorithm
#   Will try to force draws on the board
#
import copy
from Board import Board

#Global variable dictionary which will hold values calculated for the edges/perimeter of the placed pieces
coordinates = { }


#Defensive Algorithm Driver
def __init__(board):
    tempBoard = copy.deepcopy(board)
    fix_board(tempBoard)
    find_edges(tempBoard)
    calculate_edges(tempBoard)
    return pick_col()

    #functions to place

#Changes the board to False for bot and True for player pieces
def fix_board(board):
    for currRow in range(6):
        for currCol in range (7):
            if (board.search(currRow, currCol) == 1):  # Checks for player piece
                board.set_board(currRow, currCol, True)
            elif (board.search(currRow, currCol) == 2):  # Checks for bot piece
                board.set_board(currRow, currCol, False)

 # Finds outer edge pieces on the board set to True e.g. human placed pieces with free slots around them set in
 #dictionary which has initial value of 0 for each key/coordinate tuple
def find_edges(board):
    edges = [] #Array of locations in (row, col, value)

    #Note from 3/31/2020: Do more tests for this part for functionality

    for currRow in range(6):
        for currCol in range(7):
            #Check to see if current position is set to True clockwise i.e. Player's piece
            if board.search(currRow, currCol) is True:
                #Checks which see if
                if board.inbound(currRow - 1, currCol - 1) and board.search(currRow - 1, currCol - 1) is 0:
                    edges.append((currRow - 1, currCol - 1))
                if board.inbound(currRow, currCol - 1) and board.search(currRow, currCol - 1) is 0:
                    edges.append((currRow, currCol - 1))
                if board.inbound(currRow + 1, currCol - 1) and board.search(currRow + 1, currCol - 1) is 0:
                    edges.append((currRow + 1, currCol - 1))
                if board.inbound(currRow + 1, currCol) and board.search(currRow + 1, currCol) is 0:
                    edges.append((currRow + 1, currCol))
                if board.inbound(currRow + 1, currCol + 1) and board.search(currRow + 1, currCol + 1) is 0:
                    edges.append((currRow + 1, currCol + 1))
                if board.inbound(currRow, currCol + 1) and board.search(currRow, currCol + 1) is 0:
                    edges.append((currRow, currCol + 1))
                if board.inbound(currRow -1, currCol + 1) and board.search(currRow - 1, currCol + 1) is 0:
                    edges.append((currRow -1 , currCol + 1))

    #Removes duplicates from the array before inserting into a dictionary for all keys to be different
    edges = list(dict.fromkeys(edges))

    #Inserts coordinate tuples into the dictionary, setting all values to 0.
    for value in edges:
        coordinates[value] = 0

# Changes values through calculations based on set rules by the algorithm
def calculate_edges(board):
    # Iterates through all edges in a for-each loop within the dictionary
    for position in coordinates:
        connect = []      # Array which will look counter-clockwise around the edge for number of player's pieces
        summation = 0    # Calculation/score of all pieces' values that will be the value of coordinate in dictionary
        pieces = 0  # How many pieces are in the diagonal/row/column which will determine an edge's score

        # Searching for Left Diagonal going Upward
        for count in range(1, 4):
            if board.inbound(position[0] + count, position[1] - count) \
                    and board.search(position[0] + count, position[1] - count) is True:
                pieces = count
            else:
                break
        connect.append(pieces)
        pieces = 0

        # Searching for Row going Left
        for count in range(1, 4):
            if board.inbound(position[0], position[1] - count) \
                    and board.search(position[0] + count, position[1] - count) is True:
                pieces = count
            else:
                break
        connect.append(pieces)
        pieces = 0

        # Searching for Right Diagonal going Downward
        for count in range(1, 4):
            if board.inbound(position[0] - count, position[1] - count) \
                    and board.search(position[0] - count, position[1] - count) is True:
                pieces = count
            else:
                break
        connect.append(pieces)
        pieces = 0

        # Searching for Column going Downward
        for count in range(1, 4):
            if board.inbound(position[0] - count, position[1]) \
                    and board.search(position[0] - count, position[1]) is True:
                pieces = count
            else:
                break
        connect.append(pieces)
        pieces = 0

        # Searching for Left Diagonal going Downward
        for count in range(1, 4):
            if board.inbound(position[0] - count, position[1] + count) \
                    and board.search(position[0] - count, position[1] + count) is True:
                pieces = count
            else:
                break
        connect.append(pieces)
        pieces = 0

        # Searching for Row going Right
        for count in range(1, 4):
            if board.inbound(position[0], position[1] + count) \
                    and board.search(position[0], position[1] + count) is True:
                pieces = count
            else:
                break
        connect.append(pieces)
        pieces = 0

        # Searching for Right Diagonal going Upward
        for count in range(1, 4):
            if board.inbound(position[0] + count, position[1] + count) \
                    and board.search(position[0] + count, position[1] + count) is True:
                pieces = count
            else:
                break
        connect.append(pieces)

        for piece in connect:
            temp = piece
            if piece == 1:
                temp = 1
            elif piece == 2:
                temp = 2
            elif piece == 3:
                temp = 10
            summation += temp

        coordinates[position] = summation

# Returns the column from dictionary associated with the
# position with the highest score made by the bot for User Interface
# @return Integer column to place on board against player
def pick_col():
    maximum = 0 # Integer which is set to the maximum value found in the dictionary
    column = 0  # Integer of the y-position of the position which has
                # the greatest score based on player's piece positions
    for key in coordinates:
        if maximum is 0:
            maximum = coordinates[key]
            column = key[1]

        if maximum < coordinates[key]:
            maximum = coordinates[key]
            column = key[1]

    return column






