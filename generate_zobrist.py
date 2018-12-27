from bot.gotypes import Player, Point
import random

def to_python(state):
    if state is None:
        return 'None'
    if state == Player.black:
        return Player.black
    return Player.white

def hash_generator():
    MAX63 = 0x7fffffffffffffff
    table = {}
    empty_board = 0
    for row in range(1, 20):
        for col in range(1, 20):
            for state in (Player.black, Player.white):
                code = random.randint(0, MAX63)
                table[Point(row=row, col=col), state] = code
    with open('zobrist.py', 'w') as zobrist:
        zobrist.write('from .gotypes import Player, Point\n')
        zobrist.write('\n')
        zobrist.write("__all__ = ['HASH_CODE', 'EMPTY_BOARD']\n")
        zobrist.write('\n')
        zobrist.write('HASH_CODE = {\n')
        for (pt, state), hash_code in table.items():
            zobrist.write(' (%r, %s): %r,\n' % (pt, to_python(state), hash_code))
        zobrist.write('}\n')
        zobrist.write('\n')
        zobrist.write('EMPTY_BOARD = %d' % (empty_board,))
        zobrist.write('\n')

def main():
    hash_generator()
if __name__ == '__main__':
    main()