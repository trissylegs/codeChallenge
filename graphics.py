"""
Contains classes for drawing the robot moving around.
"""
import sys
from abc import ABC, abstractmethod
from turtle import Turtle
from typing import Tuple

from direction import Direction


class Graphics(ABC):
    """
    Abstract base of graphics implementations.
    """
    @abstractmethod
    def place(self, pos_x: int, pos_y: int, direction: Direction):
        """Renders the robot at a position without moving it across the table."""

    @abstractmethod
    def set_position(self, pos_x: int, pos_y: int):
        """Move the robot to a particular position."""

    @abstractmethod
    def set_direction(self, direction: Direction):
        """Turn the robot to face a given direction."""


class NullGraphics(Graphics):
    """
    Null object pattern. Doesn't do anything.
    """
    def place(self, pos_x: int, pos_y: int, direction: Direction):
        pass

    def set_position(self, pos_x: int, pos_y: int):
        pass

    def set_direction(self, direction: Direction):
        pass


class TurtleGraphics(Graphics):
    """
    Draw graphics using pythons turtle api.
    """
    def __init__(self, width, height, scale=100):
        """
        Start turtle graphics with a given width and height scaled up.
        :param width:
        :param height:
        :param scale:
        """

        self.scale = scale
        self.width = width
        self.height = height
        self.turtle = Turtle()
        self.turtle.getscreen().screensize(scale * width, scale * height)
        self.turtle.penup()

    def get_screen_position(self, x_position: int, y_position: int) -> Tuple[int, int]:
        """
        Convert robot position to screen position
        :param x_position: robot x position
        :param y_position: robot y position
        :return: tuple of x and y position of robot on screen.
        """
        return (x_position - self.width / 2) * self.scale, \
               (y_position - self.height / 2) * self.scale

    def place(self, pos_x: int, pos_y: int, direction: Direction):
        self.turtle.penup()
        screen_x, screen_y = self.get_screen_position(pos_x, pos_y)
        self.turtle.goto(screen_x, screen_y)
        self.turtle.setheading(direction.degrees)
        self.turtle.pendown()

    def set_position(self, pos_x: int, pos_y: int):
        screen_x, screen_y = self.get_screen_position(pos_x, pos_y)
        self.turtle.goto(screen_x, screen_y)

    def set_direction(self, direction: Direction):
        self.turtle.setheading(direction.degrees)


def get_graphics(width: int, height: int) -> Graphics:
    """Get the configured graphics implementation."""
    if '--turtle' in sys.argv:
        return TurtleGraphics(width, height)
    return NullGraphics()
