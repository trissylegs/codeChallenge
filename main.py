"""
Program simluates a robot moving around a table without falling off.
Main module. Runs the program with stdio.
"""
import sys

from robot import Robot
from action_parser import parse
from table import Table
from graphics import get_graphics

if __name__ == '__main__':
    table = Table(5, 5)
    g = get_graphics(5, 5)
    robot = Robot(table, g, output=sys.stdout)
    for action in parse(sys.stdin):
        action.perform_step(robot)
