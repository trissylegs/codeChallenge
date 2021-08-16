"""
Contains class for representing a Direction that the robot can travel in.
"""
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

    def turn_cc(self, turns: int):
        """
        Change the direction in a multiple of 90 degrees clockwise
        :param turns: 90 degree turns to perform.
        :return: the resulting direction
        """
        return Direction((4 + self.value - turns) % 4)

    @property
    def degrees(self) -> float:
        """
        Return the direction as a positive degrees value. I.e. EAST is 0 and SOUTH is 270.
        :return: float value of degress rotation from EAST in a counter-clockwise direction.
        """
        if self == Direction.NORTH:
            return 90
        if self == Direction.EAST:
            return 0
        if self == Direction.SOUTH:
            return 270
        if self == Direction.WEST:
            return 180
        raise ValueError("Invalid direction")

    @property
    def left(self):
        """
        Immediately to the left
        :return: 90 degrees left of this direction
        """
        return self.turn_cc(1)

    @property
    def right(self):
        """
        Immediately to the right
        :return: 90 degrees right of this direction
        """
        return self.turn_cc(-1)
