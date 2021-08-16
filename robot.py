"""
Simulates the robot.
"""
import sys
from logging import debug

from direction import Direction
from graphics import NullGraphics
from table import Table


class Robot:
    """
    Represents a robot moving around on a table. Won't fall off.
    """
    def __init__(self, table: Table, graphics=NullGraphics(), output=sys.stdout):
        self.table = table
        self.pos_x = 0
        self.pos_y = 0
        self.direction = Direction.NORTH
        self.graphics = graphics
        self.output = output

    def place(self, pos_x: int, pos_y: int, direction: Direction):
        """Place robot on the table at a given position facing a certain direction."""
        if not 0 <= pos_x <= self.table.width:
            debug(f"x must be between 0 and 4 inclusive. x={pos_x}")
            return
        if not 0 <= pos_y <= self.table.height:
            debug(f"y must be between 0 and 4 inclusive. y={pos_y}")
            return
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction
        self.graphics.place(pos_x, pos_y, self.direction)

    def move(self):
        """Move the robot forward 1 unit if there's room."""
        change_x, change_y = self.direction.get_change()
        self.pos_x, self.pos_y = self.table.new_position(self.pos_x, self.pos_y, change_x, change_y)
        self.graphics.set_position(self.pos_x, self.pos_y)

    def left(self):
        """Turn the robot anti-clockwise 90 degrees."""
        self.direction = self.direction.left
        self.graphics.set_direction(self.direction)

    def right(self):
        """Turn the robot clockwise 90 degrees."""
        self.direction = self.direction.right
        self.graphics.set_direction(self.direction)

    def report(self):
        """Print to the output the current position and direction of the robot."""
        print(self.pos_x, self.pos_y, self.direction.name, sep=',', file=self.output)
