import sys
import pygame
import numpy as np

pygame.init() # game won't work without this at beginning

# colours
white = (255, 255, 255)
grey = (180,180, 180)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# size of board
width = 300
height = 300
line_width = 5
rows = 3
cols = 3
square_size = width // cols   #100

# player icons
circle_radius = square_size // 3
circle_width = 15 # width of the line of the circle
cross_width = 15

# make the board
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe with AI')
screen.fill('black')

# make an array of zeros  zero would mean empty, so they all start empty
board = np.zeros((rows, cols))

# function to make grid
def draw_grid(color=white):
    for i in range(1, rows):
        #horizontal lines(surface, ", start point of line(x,y), end point of line(x,y),
        pygame.draw.line(screen, color, (0, square_size*i), (width, square_size*i), line_width)
        pygame.draw.line(screen, color, (square_size*i, height), (square_size*i, 0), line_width)

# drawing the shapes in the correct squares
# when the coordinates is 1, its circle, and 2 is cross (0 is empty obvs) 
def draw_shapes(color=white):          #            ( (0,0) (0,1) (0,2) )  these coordinates will either be
    for row in range(rows):            #  (row,col) ( (1,0) (1,1) (1,2) )  a 0 (empty), 1 (circle), or 
        for col in range(cols):        #            ( (2,0) (2,1) (2,2) )  2 (cross)
            # drawing circle
            # these are the coordinates
            if board[row][col] == 1:
                               #(surface, color, centre (x,y), radius, width)
                pygame.draw.circle(screen, color, (col * square_size + square_size//2, row*square_size + square_size//2),circle_radius, circle_width)
            # drawing cross
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, (col * square_size + square_size//4, row * square_size + square_size//4), (col * square_size + 3*square_size//4), row * square_size + 3*square_size//4)
                pygame.draw.line(screen, color, (col * square_size + square_size//4, row * square_size + 3*square_size//4), (col * square_size + 3*square_size//4, row * square_size + square_size//4))


# rules/functions for the game

# function to add the shape to the grid depending on which player chooses it
def mark_square(row, col, player):
    board[row][col] = player   # if the player selects those coordinates then the square should be marked with their shape

# i think this makes a square available
def available_square(row,col):
    return board[row][col] == 0

# function so you can check if the board is empty
def is_board_full(check_board=board):
    for row in range(rows):
        for col in range(cols):
            if check_board[row][col] == 0:
                return False
    return True

#check if someone has one by diagonal, horizontal or verticle 3 in a row
def check_win(player, check_board=board):
    #check for verticle 3 in row
    for col in range(cols):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True

    #check for horizontal 3 in row
    for row in range(rows):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True

    #check for verticle
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True
    if check_board[2][0] == player and check_board[1][1] == player and check_board[0][2] == player:
        return True

    #(else:)
    return False
