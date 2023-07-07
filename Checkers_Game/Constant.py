import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = HEIGHT//ROWS

# RGB codes

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 128, 0)
WHITE = (255, 247, 220)
BROWN = (165, 42, 42)
CROWN = pygame.transform.scale(pygame.image.load('Images/crown.png'), (44, 25))