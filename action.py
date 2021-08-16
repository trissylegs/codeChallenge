"""
Contains classes that represent actions the robot can perform.
"""

from abc import ABC, abstractmethod

from direction import Direction
from robot import Robot


class Action(ABC):
    """
    Base class of objects that represent an action the robot can perform.
    """
    @abstractmethod
    def perform_step(self, robot: Robot):
        """
        Perform the steps on the robot.
        :param robot: Robot to perform steops
        """

    @abstractmethod
    def __eq__(self, other):
        pass

class Place(Action):
    """
    PLACE X,Y,F
    Position and direction robot will be facing at the start.
    """
    def __init__(self, x: int, y: int, direction: Direction):
        self.position = x, y
        self.direction = direction

    def perform_step(self, robot: Robot):
        robot.place(self.position[0], self.position[1], self.direction)

    def __eq__(self, other):
        return isinstance(other, Place) and \
               self.position == other.position and \
               self.direction == other.direction


class Move(Action):
    """
    MOVE
    Move the robot forward 1 step.
    """
    def perform_step(self, robot: Robot):
        robot.move()

    def __eq__(self, other):
        return isinstance(other, Move)



class Left(Action):
    """
    LEFT
    Turn robot to the left.
    """
    def perform_step(self, robot: Robot):
        robot.left()

    def __eq__(self, other):
        return isinstance(other, Left)


class Right(Action):
    """
    RIGHT
    Turn robot to the right.
    """
    def perform_step(self, robot: Robot):
        robot.right()

    def __eq__(self, other):
        return isinstance(other, Right)


class Report(Action):
    """
    REPORT
    Print the current state of the robot to stdout.
    """
    def perform_step(self, robot: Robot):
        robot.report()

    def __eq__(self, other):
        return isinstance(other, Report)
