"""Module of type that represents the table robot is sitting on."""
from typing import Tuple


class Table:
    """Table of given size in units."""
    def __init__(self, width: int, height: int):
        if width <= 0:
            raise ValueError(f"width must be greater than 0. (width = {width})")
        if height <= 0:
            raise ValueError(f"height must be greater than 0. (height = {height})")
        self.width = width
        self.height = height

    def new_position(self, pos_x: int, pos_y: int, change_x: int, change_y: int):
        """Calculate new position such the robot remains on the table."""
        new_x = pos_x + change_x
        new_y = pos_y + change_y
        if not 0 <= new_x < self.width:
            new_x = pos_x
        if not 0 <= new_y < self.height:
            new_y = pos_y
        return new_x, new_y

    @property
    def size(self) -> Tuple[int, int]:
        """Size of the table"""
        return self.width, self.height
