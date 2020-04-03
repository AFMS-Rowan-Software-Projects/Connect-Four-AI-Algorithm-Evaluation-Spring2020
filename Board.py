# Rajinder , Pete, Josh
#   Version 1
#   Last Updated: 3/9/2020
#
# Makes a board for instancing, origin of board is 1,1
#


class Board(object):

    gameBoard = []  # Store the main board array

    # @new true for a new board and false to store an old board
    # @board previous board to be instantiated
    # starts a new board or previous board based on inputs
    def __init__(self, new, board):
        if (not new):
            self.gameBoard = board
        else:
            self.gameBoard = self.makeBoard()

    # Initializes the board and resets the board
    #   Structure:
    #                   col1 col2 col3 col4 col5 col6 col7
    #               row6
    #               row5
    #               row4
    #               row3
    #               row2
    #               row1

    def makeBoard(self):
        row6 = [0, 0, 0, 0, 0, 0, 0]
        row5 = [0, 0, 0, 0, 0, 0, 0]
        row4 = [0, 0, 0, 0, 0, 0, 0]
        row3 = [0, 0, 0, 0, 0, 0, 0]
        row2 = [0, 0, 0, 0, 0, 0, 0]
        row1 = [0, 0, 0, 0, 0, 0, 0]

        fullBoard = [row1, row2, row3, row4, row5, row6]
        return fullBoard

    # Searches the Board
    # @return returns the value at specified location or -1 if row or col values are out of bounds
    def search(self, row, col):
        if (self.inboundCol(col) and self.inboundRow(row) and True):
            return self.gameBoard[row][col]
        else:
            return -1
    # sets specifics value to the board
    # @return returns the value at specified location or -1 if row or col values are out of bounds
    def set_board(self, row, col, value):
        if (self.inboundCol(col) and self.inboundRow(row) and True):
            self.gameBoard[row][col] = value
            return True
        else:
            return False
    # @return the board
    def get_board(self):
        return self.gameBoard

    # @return a whole row or -1 if input is invalid
    def get_row(self, row):
        if (self.inboundRow(row) and True):
            return self.gameBoard[row]
        else:
            return -1
    # @return a specific column or -1 if input is invalid
    def get_col(self, col):
        if(self.inboundCol(col) and True):
            tempLoop = [0,0,0,0,0,0]
            for currRow in range(6):
                value = self.gameBoard[currRow][col]
                #print(value)
                tempLoop[currRow] = value

            return tempLoop
        else:
            return -1

    # @return returns true or false depending on if col and row are within bounds
    # Checks to see if both col and row are within bound for a 7x6 board (origin 0,0)
    def inbound(self, row, col):
        if self.inboundCol(col) == True and self.inboundRow(row) == True:
            return True
        return False

    # @return returns true or false depending on if col is within bounds
    # Checks to see if col is within bound for a 7x6 board (origin 0,0)
    def inboundCol(self, col):
        if(col < 7):
            return True
        return False

    # @return returns true or false depending on if row is within bounds
    # Checks to see if row is within bound for a 7x6 board (origin 0,0)
    def inboundRow(self, row):
        if(row < 6):
            return True
        return False

# Diag functions will always move up the board and won't account for previous rows

    # Row and Col will be the starting point of the diag going in the right direction
    # @return will return the array of variables or a -1 if it failed
    def get_diagR(self, row, col):
        if(self.inboundCol(col) and self.inboundRow(row)):
            tempLoop = [0,0,0,0,0,0]
            for add in range(6):
                nrow = row + add
                ncol = col + add  # Accounting for moving in the right direction
                if(ncol > 6 or nrow > 5):
                    break
                tempLoop[add] = self.gameBoard[nrow][ncol]
            return tempLoop
        else:
            return -1


    # Row and Col will be the starting point of the diag going in the left direction
    # @return will return the array of variables or a -1 if it failed
    def get_diagL(self, row, col):
        if(self.inboundCol(col) and self.inboundRow(row)):
            tempLoop = [0,0,0,0,0,0]
            for add in range(6):
                nrow = row + add
                ncol = col - add  # Accounting for moving in the left direction
                if ncol < -1 or nrow > 5:
                    break
                tempLoop[add] = self.gameBoard[nrow][ncol]
            return tempLoop
        else:
            return -1

    def printBoard(self):
        for row in range(6, -1, -1):
            print(self.get_row(row))