from bot.agent.naive import RandomBot
from bot import goboard_slow
from bot import gotypes
from bot.utils import print_board, print_move, points_from_coords
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bot = RandomBot()

    while not game.is_over():
        cls()
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = points_from_coords(human_move.strip())
            move = goboard_slow.Move(point=point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(game.next_player, move)

if __name__ == '__main__':
    main()