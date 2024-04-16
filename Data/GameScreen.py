import pygame
import sys
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (0, 0, 255)
CROSS_COLOR = (255, 0, 0)
icon = pygame.image.load("Data/icon.png")

# Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(icon)

board = [['' for i in range(3)] for i in range(3)]