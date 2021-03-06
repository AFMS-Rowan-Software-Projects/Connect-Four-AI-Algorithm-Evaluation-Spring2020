# Rajinder , Pete, Josh, Ian
#   Version 0.05
#   5/01/2020
#
# Offensive/Defensive/Random algorithms
#   Will try to win as fast as possible
#
import copy
from Board import Board
from random import randint

#Global variable dictionary which will hold values calculated for the edges/perimeter of the placed pieces
coordinates = {}


#Offensive Algorithm Driver
#Difficulty set to True when MinMax is active
def __init__(board, bot, difficulty, mode):    #Offensive Bot Main Driver
    tempBoard = copy.deepcopy(board)
    if(bot is not 0):
        if(difficulty is False):
            coordinates.clear()
            fix_board(bot, tempBoard)
            find_edges(tempBoard)
            if(mode is True):
                calculate_edges(tempBoard, True)
            else:
                calculate_edges(tempBoard, False)
            return pick_col(tempBoard)
        else:                           #Only for MinMax
            bestOption = ()
            coordinates.clear()
            fix_board(bot, tempBoard)
            find_edges(tempBoard)
            if(mode is True):
                calculate_edges(tempBoard, True)
            else:
                calculate_edges(tempBoard, False)
            bestOption = (pick_col(tempBoard), pick_best())
            return bestOption
    else:
        return pick_random(board)

    #functions to place

#Changes the board to False for bot and True for bot pieces
def fix_board(bot, board):
    if bot is 1:
        player = True
        placement = False
    elif bot is 2:
        player = False
        placement = True
    for currRow in range(6):
        for currCol in range (7):
            if (board.search(currRow, currCol) == 1 or board.search(currRow, currCol) is player):  # Checks for player piece
                board.set_board(currRow, currCol, player)
            elif (board.search(currRow, currCol) == 2 or board.search(currRow, currCol) is placement):  # Checks for bot piece
                board.set_board(currRow, currCol, placement)
    # board.printBoard()

 # Finds outer edge pieces on the board set to True e.g. bot placed pieces with free slots around them set in
 #dictionary which has initial value of 0 for each key/coordinate tuple
def find_edges(board):
    edges = [] #Array of locations in (row, col, value)

    #Note from 3/31/2020: Do more tests for this part for functionality

    for currRow in range(6):
        for currCol in range(7):
            #Check to see if current position is set to True clockwise i.e. Bot's piece
            if board.search(currRow, currCol) is True:
                #Checks which see if
                if board.inbound(currRow - 1, currCol - 1) and board.search(currRow - 1, currCol - 1) is 0 \
                        and not board.search(currRow - 2, currCol -1) is 0:
                    edges.append((currRow - 1, currCol - 1))
                if board.inbound(currRow, currCol - 1) and board.search(currRow, currCol - 1) is 0 \
                        and not board.search(currRow - 1, currCol -1) is 0:
                    edges.append((currRow, currCol - 1))
                if board.inbound(currRow + 1, currCol - 1) and board.search(currRow + 1, currCol - 1) is 0 \
                        and not board.search(currRow, currCol - 1) is 0:
                    edges.append((currRow + 1, currCol - 1))
                if board.inbound(currRow + 1, currCol) and board.search(currRow + 1, currCol) is 0 \
                        and not board.search(currRow, currCol) is 0:
                    edges.append((currRow + 1, currCol))
                if board.inbound(currRow + 1, currCol + 1) and board.search(currRow + 1, currCol + 1) is 0 \
                        and not board.search(currRow, currCol + 1) is 0:
                    edges.append((currRow + 1, currCol + 1))
                if board.inbound(currRow, currCol + 1) and board.search(currRow, currCol + 1) is 0 \
                        and not board.search(currRow - 1, currCol + 1) is 0:
                    edges.append((currRow, currCol + 1))
                if board.inbound(currRow -1, currCol + 1) and board.search(currRow - 1, currCol + 1) is 0 \
                        and not board.search(currRow - 2, currCol + 1) is 0:
                    edges.append((currRow -1, currCol + 1))
    #Removes duplicates from the array before inserting into a dictionary for all keys to be different
    edges = list(dict.fromkeys(edges))
    #Inserts coordinate tuples into the dictionary, setting all values to 0.
    for value in edges:
        if board.search(value[0], value[1]) is 0:
            coordinates[value] = 0
# Changes values through calculations based on set rules by the algorithm
def calculate_edges(board, mode):
    # Iterates through all edges in a for-each loop within the dictionary
    for position in coordinates:
        connect = []      # Array which will look counter-clockwise around the edge for number of Bot's pieces
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
                    and board.search(position[0], position[1] - count) is True:
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
        pieces = 0

        #Only will calculate these if the Square Move mode is active
        if(mode is True):
            #Searching for Top-Left Square
            if board.inbound(position[0] + 1, position[1] - 1) and board.search(position[0] + 1, position[1] - 1) is True:
                pieces += 1
            if board.inbound(position[0], position[1] - 1) and board.search(position[0], position[1] - 1) is True:
                pieces += 1
            connect.append(pieces)
            pieces = 0

            #Searching for Bottom-Left Square
            if board.inbound(position[0], position[1] - 1) and board.search(position[0], position[1] - 1) is True:
                pieces += 1
            if board.inbound(position[0] - 1, position[1] - 1) and board.search(position[0] - 1, position[1] - 1) is True:
                pieces += 1
            if board.inbound(position[0] - 1, position[1]) and board.search(position[0] - 1, position[1]) is True:
                pieces += 1
            connect.append(pieces)
            pieces = 0

            #Searching for Bottom-Right Square
            if board.inbound(position[0] - 1, position[1]) and board.search(position[0] - 1, position[1]) is True:
                pieces += 1
            if board.inbound(position[0] - 1, position[1] + 1) and board.search(position[0] - 1, position[1] + 1) is True:
                pieces += 1
            if board.inbound(position[0], position[1] + 1) and board.search(position[0], position[1] + 1) is True:
                pieces += 1
            connect.append(pieces)
            pieces = 0

            #Searching for Top-Right Square
            if board.inbound(position[0], position[1] + 1) and board.search(position[0], position[1] + 1) is True:
                pieces += 1
            if board.inbound(position[0] + 1, position[1] + 1) and board.search(position[0] + 1, position[1] + 1) is True:
                pieces += 1
            connect.append(pieces)

        #Calculations for pieces leading to a Connect4 winning move
        for piece in connect:
            temp = piece
            if piece == 1:
                temp = 1
            elif piece == 2:
                temp = 7
            elif piece == 3:
                temp = 20
            summation += temp
        coordinates[position] = summation

        # Checks if a coordinate is 'floating' and if it is, set its value to a negative to prevent
        # the bot from making that move
        for point in coordinates:
            if board.search(point[0] - 1, point[1]) is 0:
                coordinates[point] = -50

# Returns the column from dictionary associated with the
# position with the highest score made by the bot for User Interface
# @return Integer column to place on board against player
def pick_col(board):
    maximum = 0 # Integer which is set to the maximum value found in the dictionary
    column = 3  # Integer of the y-position of the position which has
                # the greatest score based on bot's piece positions

    if(bool(coordinates) is False): # Picks a column to place if there are no edges
        done = False
        while not done:
            column = randint(0,6)
            if(board.search(5, column) == 0):
                done = True
    else:
        for key in coordinates:
            if maximum is 0:
                maximum = coordinates[key]
                column = key[1]

            if maximum < coordinates[key]:
                maximum = coordinates[key]
                column = key[1]

    # print(column)
    return column

# Returns a value from dictionary associated with the
# position with the highest score made by the bot for User Interface
# @return Integer best to place on board against player for MinMax
def pick_best():
    best = 0
    if(bool(coordinates) is True):
        for key in coordinates:
            if best is 0:
                best = coordinates[key]

            if best < coordinates[key]:
                best = coordinates[key]

    return best

# Selects the col to place into by random
# @return Integer which is random
def pick_random(board):
    column = randint(0,6)
    if board.search(5, column) != 0:
        while True:
            column = randint(0, 6)
            if board.search(5, column) == 0:
                break
    return column
