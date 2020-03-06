# Allison, Nick
# version 1.0
# 3/5/20
# UI for whole game

import pygame
from Board import Board
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os

# Root window for new game
root = Tk()


def start_game():

    # make start menu invisible
    root.withdraw()  # bug- can't quit program after this is closed, need to close root

    # Root window for game screen
    gameFrame = Tk()
    gameFrame.config(height=280)
    # gameFrame.grid(row=0, column=0, sticky=(N, W, E, S))

    # embed pygame into tkinter frame, to allow use of drop down menu for game
    embed = tk.Frame(gameFrame, width=270, height=250)
    embed.pack()
    # gameFrame.grid()
    os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
    # create option btn
    # launches new tkinter window with options
    # gives player options 'new game, restart, quit'
    option_menu_btn = Button(gameFrame, text='Options', command=open_options)

    option_menu_btn.pack()
    gameFrame.update()
    board = []
    grid = Board(True, board)
    # Define colors
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    # set height and width for each cell
    WIDTH = 30
    HEIGHT = 30

    # Sets the margin between each cell
    MARGIN = 5
    # Keeps track of turns
    turn = 0;

    grid.__init__(True, board)
    # Initialize pygame
    pygame.init()

    # Set the size of screen
    screen = pygame.display.set_mode([255, 230])
    # Set title of screen
    pygame.display.set_caption("Connect Four")

    # Is set to true when the user is done playing
    done = False

    # Needed for game clock to run
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():  # Check to see user input
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Then we are done
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                if column > 6:
                    column = 6
                row = pos[1] // (HEIGHT + MARGIN)
                if row > 5:
                    row = 5
                # Checks turn and sees if location is occupied
                if turn % 2 == 0 and grid.get_board()[row][column] == 0:
                    if grid.get_board()[0][column] == 0:
                        row = 0
                    if grid.get_board()[1][column] == 0:
                        row = 1
                    if grid.get_board()[2][column] == 0:
                        row = 2
                    if grid.get_board()[3][column] == 0:
                        row = 3
                    if grid.get_board()[4][column] == 0:
                        row = 4
                    if grid.get_board()[5][column] == 0:
                        row = 5
                    print(row)
                    print(column)
                    grid.set_board(row, column, 1)
                    # Sets the selected location to player 1
                # Checks turn and sees if location is occupied
                elif turn % 2 == 1 and grid.get_board()[row][column] == 0:
                    if grid.get_board()[0][column] == 0:
                        row = 0
                    if grid.get_board()[1][column] == 0:
                        row = 1
                    if grid.get_board()[2][column] == 0:
                        row = 2
                    if grid.get_board()[3][column] == 0:
                        row = 3
                    if grid.get_board()[4][column] == 0:
                        row = 4
                    if grid.get_board()[5][column] == 0:
                        row = 5
                    print(row)
                    print(column)
                    grid.set_board(row, column, 2)
                    # Sets the selected location to player 2
                # Increment the turn
                turn = turn + 1

        # Set the screen background
        screen.fill(BLUE)

        # Draw the grid
        for row in range(6):
            for column in range(7):
                color = WHITE
                # If player one placed in this location set color of piece to black
                if grid.get_board()[row][column] == 1:
                    color = BLACK
                # If player one placed in this location set color of piece to black
                if grid.get_board()[row][column] == 2:
                    color = RED
                # Redraws board circles to match colors that players 1 & 2 select
                pygame.draw.circle(screen, color,
                                   [((MARGIN + WIDTH) * column + MARGIN) + 20, ((MARGIN + HEIGHT) * row + MARGIN)
                                    + 20], 15)
        clock.tick(60)  # FPS
        pygame.display.flip()  # Updates screen

    # Stops running pygame
    pygame.quit()

def open_options():
    # create new frame to give player options to
    # 'quit', 'restart', 'new game'
    optionFrame = Tk()
    optionFrame.config(width=100, height=100)

    # create grid for button option positions
    optionFrame.grid()

    # create each button for every option
    # quitBtn = Button(optionFrame, text='Quit', command=quit_game)
    # restartBtn = Button(optionFrame, text='Quit', command=restart_game)
    # new_game_Btn = Button(optionFrame, text='Quit', command=new_game)

    quitBtn = Button(optionFrame, text='Quit')
    restartBtn = Button(optionFrame, text='Restart')
    new_game_Btn = Button(optionFrame, text='New Game')

    # add btns to grid
    quitBtn.grid(row=0, column=0, sticky=NSEW)
    restartBtn.grid(row=1, column=0, sticky=NSEW)
    new_game_Btn.grid(row=2, column=0, sticky=NSEW)
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
