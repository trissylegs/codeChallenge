import sys
from abc import ABC, abstractmethod
import turtle

from direction import Direction


class Graphics(ABC):
    @abstractmethod
    def place(self, x: int, y: int, direction: Direction): pass

    @abstractmethod
    def set_position(self, x: int, y: int): pass

    @abstractmethod
    def set_direction(self, direction: Direction): pass


class NullGraphics(Graphics):
    """
    Null-object pattern. Don't do anything.
    """
    def place(self, x: int, y: int, direction: Direction): pass

    def set_position(self, x: int, y: int): pass

    def set_direction(self, direction: Direction): pass


class TurtleGraphics(Graphics):
    """
    Draw graphics using pythons turtle api.
    """
    def __init__(self, width, height, scale=100):
        self.scale = scale
        turtle.screensize(scale * width, scale * height)
        turtle.penup()

    def place(self, x: int, y: int, direction: Direction):
        turtle.penup()
        turtle.goto(x * self.scale, y * self.scale)
        turtle.setheading(direction.degrees)
        turtle.pendown()

    def set_position(self, x: int, y: int):
        turtle.goto(x * self.scale, y * self.scale)

    def set_direction(self, direction: Direction):
        turtle.setheading(direction.degrees)


def get_graphics(width: int, height: int) -> Graphics:
    if '--turtle' in sys.argv:
        return TurtleGraphics(width, height)
    else:
        return NullGraphics()
