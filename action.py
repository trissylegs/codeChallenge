from direction import Direction
from robot import Robot
from abc import ABC, abstractmethod


class Action(ABC):
    """
    Base class of objects that represent an action the robot can perform.
    """
    @abstractmethod
    def perform_step(self, robot: Robot): pass
    def __eq__(self, other):
        return type(self) == type(other)


class Place(Action):
    """
    PLACE X,Y,F
    Position and direction robot will be facing at the start.
    """
    def __init__(self, x: int, y: int, direction: Direction):
        self.x = x
        self.y = y
        self.direction = direction

    def perform_step(self, robot: Robot):
        robot.place(self.x, self.y, self.direction)

    def __eq__(self, other):
        return type(self) == type(other) and self.x == other.x and self.y == other.y and self.direction == other.direction


class Move(Action):
    """
    MOVE
    Move the robot forward 1 step.
    """
    def perform_step(self, robot: Robot): robot.move()


class Left(Action):
    """
    LEFT
    Turn robot to the left.
    """
    def perform_step(self, robot: Robot): robot.left()


class Right(Action):
    """
    RIGHT
    Turn robot to the right.
    """
    def perform_step(self, robot: Robot): robot.right()


class Report(Action):
    """
    REPORT
    Print the current state of the robot to stdout.
    """
    def perform_step(self, robot: Robot): robot.report()
