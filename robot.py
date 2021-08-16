import sys
from logging import debug

from direction import Direction
from graphics import NullGraphics
from table import Table


class Robot:
    def __init__(self, table: Table, graphics=NullGraphics(), output=sys.stdout):
        self.table = table
        self.x = 0
        self.y = 0
        self.direction = Direction.NORTH
        self.graphics = graphics
        self.output = output

    def place(self, x: int, y: int, direction: Direction):
        if not (0 <= x <= self.table.width):
            debug(f"x must be between 0 and 4 inclusive. x={x}")
            return
        if not (0 <= y <= self.table.height):
            debug(f"y must be between 0 and 4 inclusive. y={y}")
            return
        self.x = x
        self.y = y
        self.direction = direction
        self.graphics.place(x, y, self.direction)

    def move(self):
        dx, dy = self.direction.get_change()
        self.x, self.y = self.table.new_position(self.x, self.y, dx, dy)
        self.graphics.set_position(self.x, self.y)

    def left(self):
        self.direction = self.direction.left
        self.graphics.set_direction(self.direction)

    def right(self):
        self.direction = self.direction.right
        self.graphics.set_direction(self.direction)

    def report(self):
        print(self.x, self.y, self.direction.name, sep=',', file=self.output)
