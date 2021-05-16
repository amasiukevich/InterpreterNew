from src.utils.position import Position
from src.exceptions.position_exception import PositionException
import unittest

class TestPosition(unittest.TestCase):

    def test_position_creation(self):

        pos = Position(line=3, column=10)
        self.assertEqual(pos.line, 3, "Line doesn't match")
        self.assertEqual(pos.column, 10, "Column doesn't match")

    def test_position_advance_column(self):

        pos = Position(line=1, column=1)
        pos.advance_column()
        self.assertEqual(pos.line, 1, "Line number shouldn't change")
        self.assertEqual(pos.column, 2, "Column number should change")

    def test_position_advance_line(self):

        pos = Position(line=10, column=12)
        pos.advance_line()

        self.assertEqual(pos.line, 11, "Line number should change")
        self.assertEqual(pos.column, 0, "Column number should be 0")


    def testEquality(self):

        pos1 = Position(line=2, column=3)
        pos2 = Position(line=2, column=2)

        pos2.advance_column()

        self.assertEqual(pos1, pos2, f"Positions should be equal\npos1: {repr(pos1)}\npos2: {repr(pos2)}")


    def test_invalid_line(self):

        with self.assertRaises(PositionException) as cm:
            Position(line=-1, column=0)


        the_exception = cm.exception
        self.assertEqual(
            the_exception.message,
            "Line number cannot be less or equal to 0"
        )



    def test_invalid_column(self):

        with self.assertRaises(PositionException) as cm:
            Position(line=1, column=-10)

        the_exception = cm.exception
        self.assertEqual(
            the_exception.message,
            "Column number cannot be less than 0"
        )