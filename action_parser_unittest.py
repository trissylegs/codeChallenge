import io
import unittest
import action_parser
from action import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_parse_empty(self):
        s = io.StringIO('')
        res = list(action_parser.parse(s))
        self.assertListEqual([], res)

    def test_parse_move(self):
        s = io.StringIO('MOVE\n')
        res = list(action_parser.parse(s))
        self.assertListEqual([Move()], res)

    def test_parse_left(self):
        s = io.StringIO('LEFT\n')
        res = list(action_parser.parse(s))
        self.assertListEqual([Left()], res)

    def test_parse_right(self):
        s = io.StringIO('RIGHT\n')
        res = list(action_parser.parse(s))
        self.assertListEqual([Right()], res)

    def test_parse_report(self):
        s = io.StringIO('REPORT\n')
        res = list(action_parser.parse(s))
        self.assertListEqual([Report()], res)

    def test_parse_place(self):
        s = io.StringIO('PLACE 1,2,NORTH')
        res = list(action_parser.parse(s))
        self.assertListEqual([Place(1, 2, Direction.NORTH)], res)

    def test_parse_place_neq(self):
        # Checking Place(1,2,N) != Place(1,3,N)
        s = io.StringIO('PLACE 1,2,NORTH')
        res = list(action_parser.parse(s))
        self.assertNotEqual(Place(1, 3, Direction.NORTH), res[0])


if __name__ == '__main__':
    unittest.main()
