import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

width = 30
height = 30

turn = 0
winner = 0

margin = 5


def empty_grid():
    # creating a 2-D array
    # that is simply a list of lists
    grid = []
    for row in range(7):
        # add an empty array that will hold
        # each cell in this row
        grid.append([])
        for column in range(7):
            grid[row].append(0)  # append a cell
    return grid


pygame.init()
size = [250, 250]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect-4 Game")


def init():
    global done, display_ins, ins_page, game_over, clock, grid
    done = False
    display_ins = True
    ins_page = 1
    game_over = 0
    grid = empty_grid()
    clock = pygame.time.Clock()


init()

font = pygame.font.SysFont("comicsansms", 25)


def win_row_1(grid):
    for r in range(7):
        for c in range(4):
            if grid[r][c] == 1 and grid[r][c + 1] == 1 and grid[r][c + 2] == 1 and grid[r][c + 3] == 1:
                winner = 1
                return 1
    return 0


def win_row_2(grid):
    for r in range(7):
        for c in range(4):
            if grid[r][c] == 2 and grid[r][c + 1] == 2 and grid[r][c + 2] == 2 and grid[r][c + 3] == 2:
                winner = 2
                return 1
    return 0


def win_col_1(grid):
    for c in range(7):
        for r in range(4):
            if grid[r][c] == 1 and grid[r + 1][c] == 1 and grid[r + 2][c] == 1 and grid[r + 3][c] == 1:
                winner = 1
                return 1
    return 0


def win_col_2(grid):
    for c in range(7):
        for r in range(4):
            if grid[r][c] == 2 and grid[r + 1][c] == 2 and grid[r + 2][c] == 2 and grid[r + 3][c] == 2:
                winner = 2
                return 1
    return 0


def win_forw_diag_1(grid):
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 1 and grid[r + 1][c + 1] == 1 and grid[r + 2][c + 2] == 1 and grid[r + 3][c + 3] == 1:
                winner = 1
                return 1
    return 0


def win_forw_diag_2(grid):
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 2 and grid[r + 1][c + 1] == 2 and grid[r + 2][c + 2] == 2 and grid[r + 3][c + 3] == 2:
                winner = 2
                return 1
    return 0


def win_back_diag_1(grid):
    for r in range(4):
        for c in range(3, 7):
            if grid[r][c] == 1 and grid[r + 1][c - 1] == 1 and grid[r + 2][c - 2] == 1 and grid[r + 3][c - 3] == 1:
                winner = 1
                return 1
    return 0


def win_back_diag_2(grid):
    for r in range(4):
        for c in range(3, 7):
            if grid[r][c] == 2 and grid[r + 1][c - 1] == 2 and grid[r + 2][c - 2] == 2 and grid[r + 3][c - 3] == 2:
                winner = 2
                return 1
    return 0


# INSTRUCTIONS LOOP
while done == False and display_ins:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            ins_page += 1
            if ins_page == 2:
                display_ins = False

    screen.fill(WHITE)

    if ins_page == 1:
        text = font.render("Welcome to Connect-4", True, BLUE)
        screen.blit(text, [125 - text.get_width() // 2, 125 - text.get_width() // 2])
        text = font.render("Click here to begin", True, BLACK)
        screen.blit(text, [125 - text.get_width() // 2, 165 - text.get_width() // 2])

    clock.tick(20)
    pygame.display.flip()

# MAIN GAME LOOP
while not done:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width + margin)
            row = pos[1] / (height + margin)
            # set that location to zero
            if turn % 2 == 0:  # ........player 1........
                if grid[row][column] != 2:
                    grid[row][column] = 1
                    turn += 1

            else:  # ........player 2........
                if grid[row][column] != 1:
                    grid[row][column] = 2
                    turn += 1

            if game_over == 1:
                init()
                game_over = 0

    # drawing the UPDATED grid
    for r in range(7):
        for c in range(7):
            color = WHITE
            if grid[r][c] == 1:
                color = GREEN
            elif grid[r][c] == 2:
                color = RED
            pygame.draw.rect(screen, color,
                             [(margin + width) * c + margin, (margin + height) * r + margin, width, height])

    if win_row_1(grid) or win_col_1(grid) or win_back_diag_1(grid) or win_forw_diag_1(grid):
        # print("1")
        game_over = 1
        screen.fill(WHITE)
        win_text = font.render("Player 1 wins", True, (0, 0, 255))
        screen.blit(win_text, (125 - win_text.get_width() // 2, 125 - win_text.get_height() // 2))
        over_text = font.render("Click here to play again", True, BLACK)
        screen.blit(over_text, (125 - over_text.get_width() // 2, 165 - over_text.get_height() // 2))

    if win_row_2(grid) or win_col_2(grid) or win_back_diag_2(grid) or win_forw_diag_2(grid):
        # print("2")
        game_over = 1
        screen.fill(WHITE)
        win_text = font.render("Player 2 wins", True, (0, 0, 255))
        screen.blit(win_text, (125 - win_text.get_width() // 2, 125 - win_text.get_height() // 2))
        over_text = font.render("Click here to play again", True, BLACK)
        screen.blit(over_text, (125 - over_text.get_width() // 2, 165 - over_text.get_height() // 2))
    clock.tick(60)
    pygame.display.flip()
pygame.quit()