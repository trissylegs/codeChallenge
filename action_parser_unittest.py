"""
Tests for action_parser.py
"""
import io
import unittest
import action_parser
from direction import Direction
from action import Move, Left, Right, Place, Report


class ParseTests(unittest.TestCase):
    "Tests for action_parser.parse"

    def test_parse_empty(self):
        "It returns zero actions when given an empty string"
        str_input = io.StringIO('')
        res = list(action_parser.parse(str_input))
        self.assertListEqual([], res)

    def test_parse_move(self):
        "It returns a action.Move for 'MOVE'"
        str_input = io.StringIO('MOVE\n')
        res = list(action_parser.parse(str_input))
        self.assertListEqual([Move()], res)

    def test_parse_left(self):
        "It returns a action.Left for 'LEFT'"
        str_input = io.StringIO('LEFT\n')
        res = list(action_parser.parse(str_input))
        self.assertListEqual([Left()], res)

    def test_parse_right(self):
        "It returns a action.Right for 'RIGHT'"
        str_input = io.StringIO('RIGHT\n')
        res = list(action_parser.parse(str_input))
        self.assertListEqual([Right()], res)

    def test_parse_report(self):
        "It returns a action.Report for 'REPORT'"
        str_input = io.StringIO('REPORT\n')
        res = list(action_parser.parse(str_input))
        self.assertListEqual([Report()], res)

    def test_parse_place(self):
        "It returns a action.Place for a place string"
        str_input = io.StringIO('PLACE 1,2,NORTH')
        res = list(action_parser.parse(str_input))
        self.assertListEqual([Place(1, 2, Direction.NORTH)], res)

    def test_parse_place_neq(self):
        """
        Place.__eq__ returns false when the coordinates are different.
        """
        str_input = io.StringIO('PLACE 1,2,NORTH')
        res = list(action_parser.parse(str_input))
        self.assertNotEqual(Place(1, 3, Direction.NORTH), res[0])


if __name__ == '__main__':
    unittest.main()
