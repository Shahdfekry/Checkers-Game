import pygame
from Checkers_Game.Constant import SQUARE_SIZE, ROWS, COLS, GREEN, WHITE, BROWN,CROWN
from Checkers_Game.Piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.cream_left = self.brown_left = 12
        self.cream_kings = self.brown_kings = 0
        self.create_board()

    # function to draw squares in A green and cream color scheme
    def draw_squares(self, window):
        # fill the window with green color
        window.fill(GREEN)
        # loop in each row
        for row in range(ROWS):
            # loop in each Col and skip to next one to but the cream color
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def evaluate(self):
        return self.brown_left - self.cream_left + (self.brown_kings * 0.5 - self.cream_kings * 0.5)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    # Function take piece and target position as a parameter.
    # this Function used to move the piece
    def move(self, piece, row, col):
        # Replace the piece in the new location
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        # call function to move the piece from Piece class
        piece.move(row, col)

        # check if the new rows is the last row
        if row == ROWS - 1 or row == 0:
            # if condition true turn piece into king
            piece.turn_into_king()
            if piece.color == BROWN:
                self.brown_kings += 1  # Increase the number of brown kings
            else:
                self.cream_kings += 1  # Increase the number of cream kings

    # Function to get piece by pathing row and col number
    def get_piece(self, row, col):
        return self.board[row][col]

    # Function to create a board and place pieces
    def create_board(self):
        # loop in each rows
        for row in range(ROWS):
            # Puts in each row an empty list
            self.board.append([])
            for col in range(COLS):
                # A condition to put the pieces in their correct places
                if col % 2 == ((row + 1) % 2):
                    # A condition to put the brown pieces in their correct rows(0-1-2)
                    if row < 3:
                        self.board[row].append(Piece(row, col, BROWN))
                    # A condition to put the cream pieces in their correct rows(5-6-7)
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE))
                    else:
                        self.board[row].append(0)  # Leave the rest of the rows blank (3-4)
                else:
                    self.board[row].append(0)

    # Function to draw the piece
    def draw(self, window):
        self.draw_squares(window)
        # loop in each cell
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)

    # A function to delete losing pieces from the board
    def remove(self, pieces):  # pieces are a list of the missing pieces
        for piece in pieces:
            # Replace The deleted piece with ( 0 )
            self.board[piece.row][piece.col] = 0
            # condition for decrease the number of pieces
            if piece != 0:
                if piece.color == BROWN:
                    self.brown_left -= 1
                else:
                    self.cream_left -= 1

    # Function to return the winner
    def winner(self):
        if self.brown_left <= 0:
            return "White is the winner"
        elif self.cream_left <= 0:
            return "Brown is the winner"
        return None

    # Function to get all valid move
    def get_valid_moves(self, piece):
        moves = {}     # Dictionary move
        left = piece.col - 1  # Move left in the same Row
        right = piece.col + 1  # Move right in the same Row
        row = piece.row       # piece Row

        if piece.color == WHITE or piece.king:
            # Add in moves Dictionary
            # get valid left move
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            # get valid right move
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == BROWN or piece.king:
            # Add in moves Dictionary
            # get valid left move
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            # get valid right move
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
