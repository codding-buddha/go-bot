from bot.agent.naive import RandomBot
from bot import goboard_slow
from bot import gotypes
from bot.utils import print_board, print_move
import time

def main():
    """Play bot against itself on board of size 9x9"""

    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: RandomBot(),
        gotypes.Player.white: RandomBot()
    }

    while not game.is_over():
        # wait some time before performing next move
        time.sleep(0.3)
        # clear screen
        print('\n'*4)
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(game.next_player, bot_move)

if __name__ == '__main__':
    main()