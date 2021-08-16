"""
Parses actions from a text stream.
"""
import logging
import re
from io import TextIOBase
from typing import Generator

from action import Action, Place, Move, Left, Right, Report
from direction import Direction


def parse(text_input: TextIOBase) -> Generator[Action, None, None]:
    """
    Parse the given input stream lazily yielding the stream of actions specified.
    :param text_input: input file
    :return: Generator of actions parsed from input file.
    """
    for line in text_input:
        line = line.rstrip()
        if line == 'MOVE':
            yield Move()
        elif line == 'LEFT':
            yield Left()
        elif line == 'RIGHT':
            yield Right()
        elif line == 'REPORT':
            yield Report()
        elif line.startswith('PLACE'):
            matches = re.search(r'^PLACE (\d),(\d),(NORTH|EAST|SOUTH|WEST)', line)
            pos_x = int(matches.group(1))
            pos_y = int(matches.group(2))
            direction = Direction[matches.group(3)]
            yield Place(pos_x, pos_y, direction)
        else:
            logging.warning('Unsupported input: %r', line)
