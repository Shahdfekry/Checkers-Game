from Checkers_Game.Constant import SQUARE_SIZE, GREY,CROWN
import pygame


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        # color of stand piece
        self.color = color
        self.king = False
        # piece position
        self.x = 0
        self.y = 0
        # this calling in every init to make piece in the middle of square
        self.calc_position()

    # To make piece in the center of the Square
    def calc_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # To turn piece into a king
    def turn_into_king(self):
        self.king = True

    # Function to draw the piece
    def draw(self, window):
        # To calculate the radius of the Piece
        rad = SQUARE_SIZE // 2 - self.PADDING
        # To Draw the Outline of the Piece
        pygame.draw.circle(window, GREY, (self.x, self.y), rad + self.OUTLINE)
        # To Draw the Piece
        pygame.draw.circle(window, self.color, (self.x, self.y), rad)
        # In order to place the crown on the King Piece
        if self.king:
            window.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    # Function to move the Piece
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()
