from bot.agent.naive import RandomBot
from bot import goboard
from bot import gotypes
from bot.utils import print_board, print_move, point_from_coords

def main():
    """Play bot against itself on board of size 9x9"""

    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bot = RandomBot()

    while not game.is_over():
        # clear screen
        print('\n'*4)
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(game.next_player, move)

if __name__ == '__main__':
    main()