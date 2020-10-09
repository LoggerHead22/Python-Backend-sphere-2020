"""
Тесты для крестики-нолики
"""
import unittest
import tic_tac_game


class TicTacTest(unittest.TestCase):
    """
    Тесты для крестики-нолики
    """
    def setUp(self):
        self.tictac = tic_tac_game.TicTac()

    def test_check_winner(self):

        with self.subTest(1):
            self.tictac.board = [1, 2, 3,
                                 4, 5, 6,
                                 7, 8, 9]

            self.assertEqual(self.tictac.check_winner(), -1)

        with self.subTest(2):
            self.tictac.board = ['X', 2, 'O',
                                 4, 'X', 'O',
                                 'O', 8, 'X']
            self.assertEqual(self.tictac.check_winner(), 1)

        with self.subTest(3):
            self.tictac.board = [1, 'X', 3,
                                 'O', 'O', 'O',
                                 'X', 8, 'X']

            self.assertEqual(self.tictac.check_winner(), 0)

        with self.subTest(4):
            self.tictac.board = ['X', 'O', 'X',
                                 'X', 'X', 'O',
                                 'O', 'X', 'O']

            self.assertEqual(self.tictac.check_winner(), -1)

    def test_way_to_wins(self):

        with self.subTest(0):
            self.tictac.board = [1, 2, 3,
                                 4, 5, 6,
                                 7, 8, 9]

            self.assertEqual(self.tictac.way_to_wins('X'), -1)

        with self.subTest(1):
            self.tictac.board = [1, 2, 'O',
                                 4, 'X', 'O',
                                 'X', 8, 9]
            self.assertEqual(self.tictac.way_to_wins('O'), 8)

        with self.subTest(2):
            self.tictac.board = ['O', 2, 'X',
                                 'X', 'X', 6,
                                 'O', 8, 9]

            self.assertEqual(self.tictac.way_to_wins('X'), 5)

        with self.subTest(3):
            self.tictac.board = [1, 'O', 'X',
                                 'X', 'X', 'O',
                                 'O', 'X', 'O']

            self.assertEqual(self.tictac.way_to_wins('X'), -1)

    def test_validate_input(self):

        self.assertEqual(self.tictac.validate_input('b'), -1)

        self.assertEqual(self.tictac.validate_input('2 '), 2)

        self.assertEqual(self.tictac.validate_input('2.3'), -1)

        self.assertEqual(self.tictac.validate_input('1 2'), -1)

    def test_validate_cell(self):

        with self.subTest(0):
            self.tictac.board = [1, 2, 3,
                                 4, 5, 6,
                                 7, 8, 9]

            self.assertEqual(self.tictac.validate_cell('9'), 8)

        with self.subTest(1):
            self.tictac.board = [1, 2, 'O',
                                 4, 'X', 'O',
                                 'X', 8, 9]
            self.assertEqual(self.tictac.validate_cell('0'), -1)

        with self.subTest(2):
            self.tictac.board = ['O', 2, 'X',
                                 'X', 'X', 6,
                                 'O', 8, 9]

            self.assertEqual(self.tictac.validate_cell('3'), -1)

        with self.subTest(3):
            self.tictac.board = [1, 'O', 'X',
                                 'X', 'X', 'O',
                                 'O', 'X', 'O']

            self.assertEqual(self.tictac.validate_cell('sdg w w'), -1)

    def test_computer_move(self):

        with self.subTest(0):
            self.tictac.board = [1, 2, 3,
                                 4, 5, 6,
                                 7, 8, 9]

            self.assertEqual(self.tictac.computer_move('O', 'X'), 4)

        with self.subTest(1):
            self.tictac.board = [1, 2, 'O',
                                 4, 'X', 'O',
                                 'X', 'X', 9]
            self.assertEqual(self.tictac.computer_move('X', 'O'), 8)

        with self.subTest(2):
            self.tictac.board = ['O', 2, 'X',
                                 'X', 'X', 6,
                                 'O', 8, 9]

            self.assertEqual(self.tictac.computer_move('X', 'O'), 5)

        with self.subTest(3):
            self.tictac.board = [1, 'O', 'X',
                                 'X', 'X', 'O',
                                 'O', 'X', 'O']

            self.assertEqual(self.tictac.computer_move('O', 'X'), 0)

        with self.subTest(4):
            self.tictac.board = ['O', 2, 'X',
                                 4, 'X', 6,
                                 7, 8, 9]

            self.assertEqual(self.tictac.computer_move('X', 'O'), 6)


if __name__ == "__main__":
    unittest.main()
