"""
Module tests. Tests the whole programs based on input given in string.
"""
import io
import unittest

import action_parser
from robot import Robot
from table import Table


class RobotTest(unittest.TestCase):
    """
    Tests for the robot.
    """

    def runtest(self, input_str: str, expected_output: str) -> None:
        """
        Rust tests given data as arguments.
        :param input_str: The input as a string.
        :param expected_output: The expected output as a string.
        """
        table = Table(5, 5)
        in_stream = io.StringIO(input_str)
        out_stream = io.StringIO()
        robot = Robot(table, output=out_stream)
        for action in action_parser.parse(in_stream):
            action.perform_step(robot)
        self.assertMultiLineEqual(out_stream.getvalue(), expected_output)

    def test_move(self):
        """Test MOVE changes the robots position."""
        self.runtest((
            "PLACE 0,0,NORTH\n"
            "MOVE\n"
            "REPORT\n"),
            "0,1,NORTH\n")

    def test_turnleft(self):
        """Test LEFT changes the robots direction"""
        self.runtest((
            "PLACE 0,0,NORTH\n"
            "LEFT\n"
            "REPORT\n"),
            "0,0,WEST\n")

    def test_movemoveturnmove(self):
        """Test multiple move and turn actions"""
        self.runtest((
            "PLACE 1,2,EAST\n"
            "MOVE\n"
            "MOVE\n"
            "LEFT\n"
            "MOVE\n"
            "REPORT\n"
        ),
            "3,3,NORTH\n")

    def test_move_off_table(self):
        """Test trying to move off table in WEST direction is ignored."""
        self.runtest((
            "PLACE 0,0,WEST\n"
            "MOVE\n"
            "REPORT\n"
        ), "0,0,WEST\n")

    def test_move_off_far_edge(self):
        """Test traveling accross the table and going off the north end is stopped at edge."""
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

    def test_move_nowhere(self):
        """Test reporting position immediately after starting is still the same."""
        self.runtest(("PLACE 0,0,NORTH\n"
                      "REPORT\n"),
                     "0,0,NORTH\n")

    def test_report_twice(self):
        """Test that calling report multiple-times works"""
        self.runtest(("PLACE 0,0,NORTH\n"
                      "REPORT\n"
                      "REPORT\n"),
                     ("0,0,NORTH\n"
                      "0,0,NORTH\n"))

    def test_turn_left_1(self):
        """Test output after 1 turn anti-clockwise."""
        self.runtest(("PLACE 0,0,EAST\n"
                      "LEFT\n"
                      "REPORT\n"),
                     "0,0,NORTH\n")

    def test_turn_left_2(self):
        """Test output after 2 turns anti-clockwise."""
        self.runtest(("PLACE 0,0,EAST\n"
                      "LEFT\n"
                      "LEFT\n"
                      "REPORT\n"),
                     "0,0,WEST\n")

    def test_turn_left_3(self):
        """Test output after 3 turns anti-clockwise."""
        self.runtest(("PLACE 0,0,EAST\n"
                      "LEFT\n"
                      "LEFT\n"
                      "LEFT\n"
                      "REPORT\n"),
                     "0,0,SOUTH\n")

    def test_turn_left_4(self):
        """Test output after 4 turns anti-clockwise."""
        self.runtest(("PLACE 0,0,EAST\n"
                      "LEFT\n"
                      "LEFT\n"
                      "LEFT\n"
                      "LEFT\n"
                      "REPORT\n"),
                     "0,0,EAST\n")

    def test_turn_right_1(self):
        """Test output after 1 turn clockwise."""
        self.runtest(("PLACE 0,0,EAST\n"
                      "RIGHT\n"
                      "REPORT\n"),
                     "0,0,SOUTH\n")

    def test_turn_right_2(self):
        """Test output after 2 turns clockwise."""
        self.runtest(("PLACE 0,0,EAST\n"
                      "RIGHT\n"
                      "RIGHT\n"
                      "REPORT\n"),
                     "0,0,WEST\n")

    def test_turn_right_3(self):
        """Test output after 3 turns clockwise."""
        self.runtest(("PLACE 0,0,EAST\n"
                      "RIGHT\n"
                      "RIGHT\n"
                      "RIGHT\n"
                      "REPORT\n"),
                     "0,0,NORTH\n")

    def test_turn_right_4(self):
        """Test output after 4 turns clockwise."""
        self.runtest(("PLACE 0,0,EAST\n"
                      "RIGHT\n"
                      "RIGHT\n"
                      "RIGHT\n"
                      "RIGHT\n"
                      "REPORT\n"),
                     "0,0,EAST\n")

    def test_move_north(self):
        """Test moving 1 space north."""
        self.runtest(("PLACE 2,2,NORTH\n"
                      "REPORT\n"
                      "MOVE\n"
                      "REPORT\n"),
                     ("2,2,NORTH\n"
                      "2,3,NORTH\n"))

    def test_move_south(self):
        """Test moving 1 space south."""
        self.runtest(("PLACE 2,2,SOUTH\n"
                      "REPORT\n"
                      "MOVE\n"
                      "REPORT\n"),
                     ("2,2,SOUTH\n"
                      "2,1,SOUTH\n"))

    def test_move_east(self):
        """Test moving 1 space north."""
        self.runtest(("PLACE 2,2,EAST\n"
                      "REPORT\n"
                      "MOVE\n"
                      "REPORT\n"),
                     ("2,2,EAST\n"
                      "3,2,EAST\n"))

    def test_move_west(self):
        """Test moving 1 space north."""
        self.runtest(("PLACE 2,2,WEST\n"
                      "REPORT\n"
                      "MOVE\n"
                      "REPORT\n"),
                     ("2,2,WEST\n"
                      "1,2,WEST\n"))


if __name__ == '__main__':
    unittest.main()
