from . import gotypes

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_CHAR = {
    None: '.',
    gotypes.Player.black: 'x',
    gotypes.Player.white: 'o',
}

def print_move(player, move):
    """Prints given move on screen
    
    Arguments:
        player {[gotypes.Player]} -- [Player who performed this move]
        move {[Move]} -- [Move which can be either pass, resign or play]
    """

    if move.is_pass:
        move_str = 'passes'
    elif move.is_resign:
        move_str = 'resigns'
    else:
        move_str = '{}{}'.format(COLS[move.point.col - 1], move.point.row)
    print('{} {}'.format(player, move_str))


def print_board(board):
    """Print given board on screen
    
    Arguments:
        board {[Board]} -- [Board object]
    """

    for row in range(board.num_rows, 0, -1):
        line = []
        for col in range(1, board.num_cols + 1):
            stone = board.get(gotypes.Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print('{} {}'.format(row, ''.join(line)))
    print('  ' + COLS[:board.num_cols])