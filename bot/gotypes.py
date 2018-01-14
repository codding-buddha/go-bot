import enum
from collections import namedtuple

class Player(enum.Enum):
    """Enum to represent player"""

    black = 1
    white = 2

    @property
    def other(self):
        """Get other player
        
        Returns:
            [Player] -- [Opponent for given player]
        """

        return Player.black if self == Player.white else Player.white


class Point(namedtuple('Point', 'row col')):
    """Represents point on given board"""

    def neighbours(self):
        """Get neighbouring points for given point"""

        return [
        Point(self.row - 1, self.col),
        Point(self.row + 1, self.col),
        Point(self.row, self.col - 1),
        Point(self.row, self.col + 1)
    ]