import pygame
from Checkers_Game.Constant import BLACK, SQUARE_SIZE, WHITE, BROWN,CROWN
from Checkers_Game.Board import Board


class Game:
    def __init__(self, window):
        self.selected = None  # no selected piece
        self.board = Board()
        self.turn = WHITE  # turn to play
        self.valid_moves = {}  # what is the valid moves
        # create object from Window
        self.window = window

    # Function to draw every update
    def update(self):
        # to draw the board
        self.board.draw(self.window)
        # to draw the valid moves
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # Function to return the winner
    def winner(self):
        winner = self.board.winner()
        return winner
        

    # Function to Select Piece
    def select(self, row, col):
        # If we already selected piece and have this row and col
        if self.selected:
            # then try to move
            result = self._move(row, col)
            # condition if we cant move
            if not result:
                #  selected = none
                self.selected = None
                # then recall this function
                self.select(row, col)

        # get the piece i selected from the board
        piece = self.board.get_piece(row, col)
        # check if the piece not empty square and The piece is not the opponent's piece
        if piece != 0 and piece.color == self.turn:
            # Put piece in selected
            self.selected = piece
            # Get all Valid moves
            self.valid_moves = self.board.get_valid_moves(piece)
            return True  # The piece has been selected successfully

        return False  # Not selected

    # Function to the piece
    def _move(self, row, col):
        # get the piece
        piece = self.board.get_piece(row, col)
        # Condition to check if the piece can be moved
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            # make a move
            self.board.move(self.selected, row, col)
            # get valid moves to delete it
            skipped = self.valid_moves[(row, col)]
            if skipped:
                # remove black circle
                self.board.remove(skipped)
            # Change the turn
            self.change_turn()
        else:
            return False  # cant move

        return True  # move is done

    # Function to draw the valid moves
    def draw_valid_moves(self, moves):
        for move in moves:  # loop in dictionary
            row, col = move
            pygame.draw.circle(self.window, BLACK,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    # Function to change turn
    def change_turn(self):
        # after playing a turn make valid_moves empty
        self.valid_moves = {}
        if self.turn == BROWN:
            self.turn = WHITE
        else:
            self.turn = BROWN

    # Function to Return Board
    def get_board(self):
        return self.board

    # Function to make AI play a move
    def ai_move(self, board):
        self.board = board
        self.change_turn()
