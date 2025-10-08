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
def draw_shapes(color=white):          #            ( (0,0) (0,1) (0,2) )
    for row in range(rows):            #  (row,col) ( (1,0) (1,1) (1,2) )
        for col in range(cols):        #            ( (2,0) (2,1) (2,2) )
            if board[row][col] == 1:
                               #(surface, color, centre (x,y), radius, width)
                pygame.draw.circle(screen, color, (col * square_size + square_size//2, row*square_size + square_size//2),circle_radius, circle_width)

