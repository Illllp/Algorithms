import unittest
from test_checkers import Checkers, Board, Piece

class TestCheckers(unittest.TestCase):
    def test_board_creation(self):
        checkers = Checkers()
        checkers.board.create_board()
        self.assertEqual(len(checkers.board.grid), 8)
        self.assertTrue(all(len(row) == 8 for row in checkers.board.grid))

if __name__ == '__main__':
    unittest.main()
