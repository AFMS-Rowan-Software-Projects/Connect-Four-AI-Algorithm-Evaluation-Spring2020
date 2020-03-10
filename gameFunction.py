# Rajinder , Pete, Nick, Allison
#   Last Updated: 3/9/2020
#   Version 1
# Processes the board and looks for win conditions

from Board import Board

    # Check Win looks at left & right diagonals, columns, and rows for 4 in a row
    # @grid the board that needs to be checked for any win conditions
    # @return returns the winning player if one is found, if none 0 is returned
def checkWin(grid):
    winner = 0
    winner = checkBothDiagonals(grid)
    if(winner > 0):
        print("diag win")
        return winner
    winner = checkCol(grid)
    if(winner > 0):
        print("Col win")
        return winner
    winner = checkRow(grid)
    if(winner > 0):
        print("row win")
        return winner
    return winner


    # Checks both diagonals across the board
    # @board the board at which the diagonals of both right and left need to be checked
    # @return returns the winning player or 0 by default if no winner is found
def checkBothDiagonals(board):

    #2 Tuples  to store the coordinates of the base of the diagonal
    #RIGHT
    positionsRRow = [0, 2, 0, 1, 0, 0]   #positions for Right row coordinates
    positionsRCol = [3, 1, 2, 1, 1, 0]   #positions for Right col coordinates

    #LEFT
    positionsLRow = [0, 2, 0, 1, 0, 0]   #positions for Left row coordinates
    positionsLCol = [3, 6, 4, 6, 6, 5]   #positions for Left col coordinates
    player = 0

    for num in range(2):
        if(num == 0):
            player = checkDiagonal(board, positionsRRow, positionsRCol, False)
            if(player > 0):
                return player
        else:
            player = checkDiagonal(board, positionsLRow, positionsLCol, True)
            if(player > 0):
                return player
    return 0;



    # Check either left or right diagonal
    # @board the board that needs the diagonal checked
    # @positionsRow an array with coordinates for the row that need to be checked needs to be length of 6
    # @positionsCol an array with coordinates for the col that need to be checked needs to be length of 6
    # @left a boolean that determines if the value will be a left or right diagonal (False for right and True for Right)
    # @return returns the winning player, will return 0 by default
def checkDiagonal(board, positionsRow,positionsCol, left):

    position = 0                        #current diagonal coordinates based on tuples

    # Outer Diagonals length of 4th
    while position < 2:
        if(left):
            currDiag = board.get_diagL(positionsRow[position], positionsCol[position])
        else:
            currDiag = board.get_diagR(positionsRow[position], positionsCol[position])

        player = currDiag[3]  # player value for check
        if(player != 0):
            if(currDiag[2] != 0 and player == currDiag[2]):
                if(currDiag[1] != 0 and player == currDiag[1]):
                    if (currDiag[0] != 0 and player == currDiag[0]):
                            return player
        position += 1

    # Second and Fifth Diagonals length of 5th
    while position < 4:
        if (left):
            currDiag = board.get_diagL(positionsRow[position], positionsCol[position])
        else:
            currDiag = board.get_diagR(positionsRow[position], positionsCol[position])

        player = currDiag[3]  # player value for check
        if(player != 0):
            if (currDiag[2] != 0 and player == currDiag[2]):
                if (currDiag[1] != 0 and player == currDiag[1]):
                    if (currDiag[0] != 0 and player == currDiag[0]):
                        return player
                    if(currDiag[4] != 0 and player == currDiag[4]):
                        return player
        position += 1

    # Middle Diagonals length of 6th
    while position < 6:
        if (left):
            currDiag = board.get_diagL(positionsRow[position], positionsCol[position])
        else:
            currDiag = board.get_diagR(positionsRow[position], positionsCol[position])

        player = currDiag[3]  # player value for check
        if(player != 0): #Position 3 checked
            if(currDiag[2] != 0 and player == currDiag[2]): #Position 2 checked
                if (currDiag[1] != 0 and player == currDiag[1]): #Position 1 checked
                    if (currDiag[0] != 0 and player == currDiag[0]): #Position 0 checked
                        return player
                    if (currDiag[4] != 0 and player == currDiag[4]): #Position 4 checked
                        return player
                if (currDiag[4] != 0 and player == currDiag[4]): #Position 4 checked
                    if (currDiag[5] != 0 and player == currDiag[5]): #Position 5 checked
                        return player
        position += 1
    return 0


    # Checks the columns for win conditions
    # @board the board that needs the column checked
    # @Returns a winnning player or will return 0 if no player wins
def checkCol(board):
    col = 0
    while col < 6:
        currCol = board.get_col(col) #Returns the current Col array
        player = currCol[3] #Holds the value of the first win condition spot
        if(player != 0): #Position 3 checked
        # Checks to see if positions to the down or up are 0 and proceeds forward
        # Will also take into account the player and will exit if the player's pieces don't match
            if(currCol[2] != 0 and player == currCol[2]): #Position 2 checked
                #Moves down in the column
                if(currCol[1] != 0 and player == currCol[1]): #Position 1 checked
                    if (currCol[0] != 0 and player == currCol[0]): #Position 0 checked
                        return player
                    if (currCol[4] != 0 and player == currCol[4]): #Position 4 checked
                        return player
                #Moves up in the column
                if(currCol[4] != 0 and player == currCol[4]): #Position 4 checked
                    if (currCol[5] != 0 and player == currCol[5]): #Position 5 checked
                        return player
        col += 1
    return 0;


    # Checks row for the win condition
    # @board the board that needs the row checked
    # @Returns a winnning player or will return 0 if no player wins
def checkRow(board):
    row = 0
    while row < 6:
        currRow = board.get_row(row)   #Returns the current Row array
        playerMiddle = int(currRow[3])  #Holds the value of the piece in the middle
        if(playerMiddle != 0): #position 3 checked

        #Checks to see if positions to the left or right are 0 and proceeds forward
        #Will also take into account the player and will exit if the player's pieces don't match
            #Moves through the right of the array
            if(currRow[4] != 0 and playerMiddle == currRow[4]): #Position 4 checked
                if(currRow[5] != 0 and playerMiddle == currRow[5]): #Position 5 checked
                    if(currRow[6] != 0 and playerMiddle == currRow[6]): #Position 6 checked
                        return playerMiddle
                    if(currRow[2] != 0 and playerMiddle == currRow[2]): #Position 2 checked
                        return playerMiddle
            #Moves through the left of the array
            if(currRow[2] != 0 and playerMiddle == currRow[2]): #Position 2 checked
                if (currRow[1] != 0 and playerMiddle == currRow[1]): #Position 1 checked
                    if (currRow[0] != 0 and playerMiddle == currRow[0]): #Position 0 checked
                        return playerMiddle
                    if (currRow[4] != 0 and playerMiddle == currRow[4]):  # Position 4 checked
                        return playerMiddle
        row += 1
    return 0;

