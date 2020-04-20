# Allison, Nick
# version 2.0
# 4/9/20
# UI for whole game
from tkinter import messagebox

import pygame
from pygame.constants import KEYDOWN

from Board import Board
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
import gameFunction
import BotControl
from random import randint
import time
# Root window for new game
root = Tk()
board = []
grid = Board(True, board)
winner = 0

def reset():
    grid.makeBoard()
    grid.printBoard()




def start_game():
    # make start menu invisible
    root.withdraw()  # bug- can't quit program after this is closed, need to close root
    humanTurn = randint(0, 1)
    botTurn = 1 - humanTurn

    reset()
    # Define colors
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    YELLOW = (255,255,204)
    # set height and width for each cell
    WIDTH = 30
    HEIGHT = 30

    # Sets the margin between each cell
    MARGIN = 5
    # Keeps track of turns
    turn = 0


    grid.__init__(True, board)
    # Initialize pygame
    pygame.init()

    # Set the size of screen
    screen = pygame.display.set_mode([255,230], pygame.RESIZABLE)
    # Set title of screen
    pygame.display.set_caption("Connect Four")
    # Background where pause menu exists, will overlay game when player pauses game

    # Is set to true when the user is done playing
    done = False

    # Needed for game clock to run
    clock = pygame.time.Clock()
    counter = 0

    #ToDo: make it so it doesn't loop constantly ( Maybe an action listener???????????)
    while not done:

        counter = counter + 1
        #print("Starting..... loop: " + str(counter))
        for event in pygame.event.get():  # Check to see user input
            if event.type == pygame.QUIT:  # If user clicked close
                root.deiconify()
                done = True  # Then we are done
            elif event.type == pygame.MOUSEBUTTONDOWN and turn % 2 == humanTurn:
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                #print("Mouse Pos: " + str(pos[0]))
                WIDTH, HEIGHT = pygame.display.get_surface().get_size()
                #print("WIDTH: " + str(WIDTH))

                column = int((((pos[0] / (WIDTH + MARGIN))*100)//13))
                #print("Column Value: " + str(((pos[0] / (WIDTH + MARGIN))*100)//13))
                if column > 6:
                    column = 6

                # Checks turn and sees if location is occupied
                if turn % 2 == humanTurn and grid.search(row, column) == 0:
                    # makes sure the piece is the lowest possible position
                    currentCol = grid.get_col(column)
                    for currRow in range(5, -1, -1):
                        if currentCol[currRow] == 0:
                            row = currRow
                        else:
                            break
                    grid.set_board(row, column, 1)
                    turn = turn + 1
                    # Sets the selected location to player 1
                # Checks turn and sees if location is occupied

            elif turn % 2 == botTurn:
                column = BotControl.__init__(botPick.get(), grid, turn)
                currentCol = grid.get_col(column)
                for currRow in range(5, -1, -1):
                    if currentCol[currRow] == 0:
                        row = currRow
                    else:
                        break
                grid.set_board(row, column, 2)
                # Sets the selected location to player 2
                # Increment the turn
                turn = turn + 1
#*******************************************************************************************************************
            # triggers pause menu with options for player to start new game, restart, or quit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Esc key pressed mid game")

                    OPTIONSWIDTH, OPTIONSHEIGHT = pygame.display.get_surface().get_size()
                    background = pygame.Surface([OPTIONSWIDTH, OPTIONSHEIGHT], pygame.RESIZABLE)
                    print(str(OPTIONSWIDTH))
                    print(str(OPTIONSHEIGHT))

                    rectBtnHeight = OPTIONSHEIGHT//10
                    rectBtnWidth = OPTIONSWIDTH//3


                    rectMargin = rectBtnHeight + 10

                    rectX = OPTIONSWIDTH//3
                    continueY = OPTIONSHEIGHT//10
                    restartY = continueY + rectMargin
                    mainY = restartY + rectMargin
                    quitY = mainY + rectMargin

                    pygame.draw.rect(background, BLUE, (0, 0, OPTIONSWIDTH, OPTIONSHEIGHT))
                    pygame.draw.rect(background, WHITE,
                                     (rectX, continueY, rectBtnWidth, rectBtnHeight))  # The continue rectangle
                    pygame.draw.rect(background, WHITE,
                                     (rectX, restartY, rectBtnWidth, rectBtnHeight))  # the restart rect
                    pygame.draw.rect(background, WHITE,
                                     (rectX, mainY, rectBtnWidth, rectBtnHeight))  # main menu rect
                    pygame.draw.rect(background, WHITE,
                                     (rectX, quitY, rectBtnWidth, rectBtnHeight))  # the quit rect

                    font = pygame.font.Font('freesansbold.ttf', 12)

                    Continue = font.render('Continue', True, BLACK)
                    ContinueRect = Continue.get_rect()
                    ContinueRect.center = (rectX+(rectBtnWidth//2), continueY+(rectBtnHeight//2))
                    background.blit(Continue, ContinueRect)

                    Restart = font.render('Restart', True, BLACK)
                    RestartRect = Restart.get_rect()
                    RestartRect.center = (rectX+(rectBtnWidth//2), restartY+(rectBtnHeight//2))
                    background.blit(Restart, RestartRect)

                    MM = font.render("Main Menu", True, BLACK)
                    MMRect = MM.get_rect()
                    MMRect.center = (rectX+(rectBtnWidth//2), mainY+(rectBtnHeight//2))
                    background.blit(MM, MMRect)

                    Quit = font.render("Quit", True, BLACK)
                    QuitRect = Quit.get_rect()
                    QuitRect.center = (rectX+(rectBtnWidth//2), quitY+(rectBtnHeight//2))

                    background.blit(Quit, QuitRect)
                    screen.blit(background, (0, 0))
                    finished = False
                    pygame.display.flip()
                    while not finished:
                        for i in pygame.event.get():
                            if i.type == pygame.QUIT:  # If user clicked close
                                pygame.quit()
                                root.deiconify()
                                done = True  # Then we are done
                                finished = True

                            if i.type == pygame.QUIT:  # If user clicked close
                                return None

                            if i.type == pygame.MOUSEBUTTONDOWN:
                                optionpos = pygame.mouse.get_pos()
                                posY = optionpos[1]

                                # check if user clicked within width of buttons, ignore anything to right or left of them
                                if rectX <= optionpos[0] <= (rectX+rectBtnWidth):
                                    # checks if user clicks between start and end of buttons vertically
                                    if continueY <= posY <= (quitY + rectBtnHeight):
                                        if continueY <= posY <= (continueY + rectBtnHeight):
                                            # continue game btn pressed
                                            finished = True
                                        elif restartY <= posY <= restartY + rectBtnHeight:
                                            # reset board
                                            reset()
                                            humanTurn = randint(0, 1)
                                            botTurn = 1 - humanTurn
                                            turn = 0
                                            finished = True
                                        elif mainY <= posY <= mainY + rectBtnHeight:
                                            # main menu btn pressed
                                            root.deiconify()  # make main menu visible again
                                            done = True  # exit pygame loop
                                            finished = True  # exit option menu loop
                                        elif quitY <= posY <= quitY + rectBtnHeight:
                                            # quit entire program, kill everything
                                            pygame.quit()
                                            root.destroy()
                                            # jump over rest of code, don't need to run, program closing
                                            return None



                                # finished = True

                    # update display
#**********************************************************************************************************************

                    # FOR TESTING to stop this from inf looping, just pauses everything for 5 sec
                    #time.sleep(3)

                    # create separate tkinter window that features options for player to select
                    # optionFrame = Tk()
                    # optionFrame.geometry('200x200')
                    # create 3 buttons on frame for each option
            elif event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                screen = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)

        # Set the screen background
        screen.fill(BLUE)

        # Draw the grid
        #print("Drawing.....")
        for row in range(6):
            for column in range(7):
                color = WHITE
                # If player one placed in this location set color of piece to black
                if grid.search(row,column) == 1:
                    color = BLACK
                # If player two placed in this location set color of piece to red
                if grid.search(row,column) == 2:
                    color = RED
            # Redraws board circles to match colors that players 1 & 2 select
                #Pulls out the screens Width & Height
                WIDTH, HEIGHT = pygame.display.get_surface().get_size()
                #
                # Max - > Takes the larger integer between 1 and the returned min value
                # Min - > compares the value of the width and height to find the proper size of the circle
                # Math -> // pulls out a strictly integer value & Width(Height)//7 matches the proper size of the circle
                radius = max(min((WIDTH//7)//2 - 5, (HEIGHT//7)//2 - 5), 1)

                #Debug Line
                #print("Current Row: " + str(row) + " @ y Coordinate : " + str(HEIGHT//7 + (HEIGHT//7 * row)) + " Current Height: " + str(HEIGHT))

                # @1st param layer to be placed
                # @2nd param color of the circle, changes based on selection
                # @3rd param x & y coord
                # @4rd param the radius of the circle
                pygame.draw.circle(screen, color, [radius+10 +(WIDTH//7 * column), (HEIGHT - radius - 2) - (HEIGHT//7 + (HEIGHT//7 * row))], radius)

                #Set New Margin
                MARGIN = radius+10//2

        #Drawing grid to figure out margins
        #sad = 0
        #for x in range(6):
        #    sad =sad + (255//6.85)
        #    pygame.draw.rect(screen, RED,(sad, 0, 3 ,230))


        clock.tick(60)  # FPS
        pygame.display.flip()  # Updates screen
        pygame.display.update()
        if turn > 6:
            winner = gameFunction.checkWin(grid)
            if winner != 0:  # check if there is a win
                # convert 1 or 2 to player or bot respectively
                winnerStr = ""
                if (winner == 1):
                    winnerStr = "Player"
                else:
                    winnerStr = "Bot"
                # TODO make winner box appear in front of pygame
                # create tkinter message telling user who won (user or bot)
                messagebox.showinfo("Winner!", winnerStr + " has won! Game completed in " + str(turn) + " turns.")

                # make main menu reappear
                root.deiconify()
                done = True

    # Stops running pygame
    pygame.quit()


#def open_options():
    # create new frame to give player options to
    # 'quit', 'restart', 'new game'
    #optionFrame = Tk()
    #optionFrame.config(width=100, height=100)

    # create grid for button option positions
    #optionFrame.grid()


    # create each button for every option
    # quitBtn = Button(optionFrame, text='Quit', command=quit_game)
    # restartBtn = Button(optionFrame, text='Quit', command=restart_game)
    # new_game_Btn = Button(optionFrame, text='Quit', command=new_game)

    #quitBtn = Button(optionFrame, text='Quit')
    #restartBtn = Button(optionFrame, text='Restart')
    #new_game_Btn = Button(optionFrame, text='New Game')

    # add btns to grid
    #quitBtn.grid(row=0, column=0, sticky=NSEW)
    #restartBtn.grid(row=1, column=0, sticky=NSEW)
    #new_game_Btn.grid(row=2, column=0, sticky=NSEW)


# var that controls selection of bot pick radio buttons
botPick = tk.IntVar()
botPick.set(1)  # default bot is set to 1, or 'random bot'

# set default size of frame
root.geometry('500x500')

# set title of frame
root.title("Connect 4")
# create new game button that starts game
start_game_btn = Button(root, text='New Game', command=start_game)

# create buttons that let user pick which bot they would like to play against
# random bot select btn
rand_select_btn = Radiobutton(root, text='Random Bot', variable=botPick, value=1)  # default option
defensive_select_btn = Radiobutton(root, text='Defensive Bot', variable=botPick, value=2)
aggresive_select_btn = Radiobutton(root, text='Aggressive Bot', variable=botPick, value=3)
minmax_select_btn = Radiobutton(root, text='Min Max Bot', variable=botPick, value=4)

# set position of each btn to top of window
start_game_btn.grid(row=0, column=0)
rand_select_btn.grid(row=1, column=0)
defensive_select_btn.grid(row=2, column=0)
aggresive_select_btn.grid(row=3, column=0)
minmax_select_btn.grid(row=4, column=0)

start_game_btn.place(relx=0.5, rely=0.2, anchor=CENTER)
rand_select_btn.place(relx=0.5, rely=0.3, anchor=CENTER)
defensive_select_btn.place(relx=0.5, rely=0.4, anchor=CENTER)
aggresive_select_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
minmax_select_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

# mainloop
root.mainloop()