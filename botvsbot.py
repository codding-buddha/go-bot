from bot.agent.naive import RandomBot
from bot.agent.montecarlo_treesearch import MCTSAgent
from bot import goboard
from bot import gotypes
from bot.utils import print_board, print_move
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    board_size = 4
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: RandomBot(),
        gotypes.Player.white: MCTSAgent(3, 1.5),
    }

    while not game.is_over():
        cls()
        time.sleep(0.3)
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(game.next_player, bot_move)
    print('Winner %s ' % game.winner())

if __name__ == '__main__':
    main()