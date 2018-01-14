import random

from gotypes import Player, Point

def to_python(state):
    if state is None:
        return 'None'
    if state == Player.black:
        return Player.black
    return Player.white

MAX63 = 0x7fffffffffffffff

table = {}
empty_board = 0

for row in range(1, 20):
    for col in range(1, 20):
        for state in (None, Player.black, Player.white):
            code = random.randint(0, MAX63)
            table[Point(row, col), state] = code

            if state is None:
                empty_board ^= code

print('from .gotypes import Player, Point')
print('')
print("__all__ = ['HASH_CODE', 'EMPTY_BOARD']")
print('')
print('HASH_CODE = { ')
for (pt, state), hash_code in table.items():
    print('     ({}, {}): {},'.format(pt, to_python(state), hash_code))

print('}')
print('')
print('EMPTY_BOARD = {}'.format(empty_board))
