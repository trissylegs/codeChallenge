import logging
import re
from io import TextIOBase, IOBase
from typing import Generator

from action import Action, Place, Move, Left, Right, Report
from direction import Direction


def parse(text_input: TextIOBase) -> Generator[Action, None, None]:
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
            m = re.search(r'^PLACE (\d),(\d),(NORTH|EAST|SOUTH|WEST)', line)
            x = int(m.group(1))
            y = int(m.group(2))
            direction = Direction[m.group(3)]
            yield Place(x, y, direction)
        else:
            logging.warning(f'Unsupported input: {repr(line)}')
