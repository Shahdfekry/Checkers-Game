import time

import pygame
from copy import deepcopy
from Checkers_Game.Constant import WIDTH, HEIGHT, SQUARE_SIZE, BROWN, WHITE, CROWN
from Checkers_Game.Game import Game
from Minimax_Algorithm.Minimax import minimax
from Checkers_Game.Alpha_beta.Algorithm import alphaBeta
from Checkers_Game.Board import Board
from Checkers_Game.GUI import CheckersGameGUI

FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Game')


def get_row_col_from_mouse(pos):
    x, y = pos
    global row, col
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def algorithm_difficulty():
    global givendepth
    global alg
    givendepth , alg = CheckersGameGUI.start_game(CheckersGameGUI())
    return givendepth, alg


def main():
    algorithm_difficulty()
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)
        alphaa = float('-inf')
        beta = float('inf')

        if game.turn == BROWN:

            if alg == "alphabeta":
                value, new_board = alphaBeta(game.get_board(), givendepth, alphaa, beta, True, game, BROWN, WHITE)
                if new_board is None:
                    print("Dead End")
                    break
                game.ai_move(new_board)
            elif alg == "minimax":

                value, new_board = minimax(game.get_board(), givendepth, WHITE, game, BROWN, WHITE)
                if new_board is None:
                    print("Dead End")
                    break
                game.ai_move(new_board)

        elif game.turn == WHITE:
            if alg == "alphabeta":
                value, new_board = minimax(game.get_board(), givendepth, BROWN, game, WHITE, BROWN)
                if new_board is None:
                    print("Dead End")
                    break
                game.ai_move(new_board)
            elif alg == "minimax":
                value, new_board = alphaBeta(game.get_board(), givendepth, alphaa, beta, True, game, WHITE, BROWN)
                if new_board is None:
                    print("Dead End")
                    break
                game.ai_move(new_board)

        # time.sleep(1)

        if game.winner() is not None:
            print(game.winner())
            run = False

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         pos = pygame.mouse.get_pos()
        #         row, col = get_row_col_from_mouse(pos)
        #         game.select(row, col)

        game.update()

    pygame.quit()


main()
