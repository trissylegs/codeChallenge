from enum import Enum
from typing import Tuple


class Direction(Enum):
    """
    Enum represents the directions the robot can be facing.
    Value increases in clockwise order.
    """
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def get_change(self) -> Tuple[int, int]:
        """
        Get the change and x and y made by moving 1 unit in this direction.
        :return: change in x, change in y
        """
        if self == Direction.NORTH:
            return 0, 1
        if self == Direction.EAST:
            return 1, 0
        if self == Direction.SOUTH:
            return 0, -1
        if self == Direction.WEST:
            return -1, 0
        raise ValueError("Invalid Direction")

    def turn_cw(self, turns: int):
        """
        Change the direction in a multiple of 90 degrees clockwise
        :param turns: 90 degree turns to perform.
        :return: the resulting direction
        """
        return Direction((4 + self.value + turns) % 4)

    @property
    def degrees(self) -> float:
        if self == Direction.NORTH:
            return 90
        if self == Direction.EAST:
            return 0
        if self == Direction.SOUTH:
            return 270
        if self == Direction.WEST:
            return 180

    @property
    def left(self):
        """
        Immediately to the left
        :return: 90 degrees left of this direction
        """
        return self.turn_cw(-1)

    @property
    def right(self):
        """
        Immediately to the right
        :return: 90 degrees right of this direction
        """
        return self.turn_cw(1)
