import io
import unittest

import action_parser
from robot import Robot
from table import Table


class RobotTest(unittest.TestCase):

    def runtest(self, input, output):
        table = Table(5, 5)
        instream = io.StringIO(input)
        outstream = io.StringIO()
        robot = Robot(table, output=outstream)
        for action in action_parser.parse(instream):
            action.perform_step(robot)
        self.assertMultiLineEqual(outstream.getvalue(), output)

    def test_move(self):
        self.runtest((
            "PLACE 0,0,NORTH\n"
            "MOVE\n"
            "REPORT\n"),
            "0,1,NORTH\n")

    def test_turnleft(self):
        self.runtest((
            "PLACE 0,0,NORTH\n"
            "LEFT\n"
            "REPORT\n"),
            "0,0,WEST\n")

    def test_movemoveturnmove(self):
        self.runtest ((
            "PLACE 1,2,EAST\n"
            "MOVE\n"
            "MOVE\n"
            "LEFT\n"
            "MOVE\n"
            "REPORT\n"
            ),
            "3,3,NORTH\n")

    def test_moveoffboard(self):
        self.runtest((
            "PLACE 0,0,WEST\n"
            "MOVE\n"
            "REPORT\n"
        ), "0,0,WEST\n")

    def test_movefaredge(self):
        self.runtest((
            "PLACE 0,0,NORTH\n"
            "MOVE\n"
            "MOVE\n"
            "MOVE\n"
            "MOVE\n"
            "MOVE\n"
            "MOVE\n"
            "MOVE\n"
            "REPORT"
        ), "0,4,NORTH\n")

if __name__ == '__main__':
    unittest.main()
