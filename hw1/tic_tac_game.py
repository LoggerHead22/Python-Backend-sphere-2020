"""
Программа реализующее консольное приложение - игра крестики - нолики.

Игра происходит с комьпютеорм.
Человеку дается выбор стороны - крестики или нолики.
Игра длится до тех пор, пока все клетки не будут заполнены.

"""


class TicTac:
    """
        Класс реализующий игру.
        size - размер поля
        icon_dict - словарь с символами
        win_line - наборы ячеек для проверки победителя
        computer_moves - клетки для ходов комппьютера
        mess_dict - словарь с сообщениями

    """

    size = 3
    icon_dict = {-1: '*', 1: 'X', 0: 'O'}

    win_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

    computer_moves = [4, 0, 2, 6, 8, 1, 3, 5, 7]

    mess_dict = {'Start': 'Привет! Выбери: X - 1, 0 - 2',
                 'Chose cell': 'Выбери ячейку',
                 'Err: bad format': 'Ошибка: Неверный формат, введи число.',
                 'Err: bad value': 'Ошибка: Недоступное значение.',
                 'Err: cell is busy': 'Ошибка: Ячейка занята',
                 'Win': 'Поздравляю, ты победил!',
                 'Lose': 'Сожалею, но ты проиграл.',
                 'Draw': 'Ничья!'}

    def __init__(self):
        self.board = list(range(1, TicTac.size ** 2 + 1))
        self.busy_cells = []

    def show_board(self):
        """
        Метод показывающтй текущее состояние доски
        """
        print('Board:')
        print('---------')
        for line_n in range(TicTac.size):
            line = list(map(str, self.board[line_n*3:][:3]))
            print(' | '.join(line))
            print('---------')
        print('')

    @classmethod
    def validate_input(cls, in_num):
        """
        Метод проверяющий входные данные на корректность.
        Возвращает: входное число либо -1.
        """
        try:
            num = int(in_num)
        except ValueError:
            return -1
        return num

    def validate_cell(self, in_num):
        """
        Метод проверяющий введенную ячейку на корректность.
        Возвращает: входное номер ячейки либо -1.
        """

        cell = TicTac.validate_input(in_num)
        if cell == -1:
            print(TicTac.mess_dict['Err: bad format'])
        elif cell < 1 or cell > 9:
            print(TicTac.mess_dict['Err: bad value'])
            cell = -1
        elif not TicTac.is_free_cell(self, cell - 1):
            print(TicTac.mess_dict['Err: cell is busy'])
            cell = -1
        else:
            return cell - 1

        return -1

    def is_free_cell(self, num):
        """
        Метод проверяющий  ячейку под номером num на корректность.
        Возвращает: True либо False
        """
        if self.board[num] == 'X' or self.board[num] == 'O':
            res = False
        else:
            res = True
        return res

    def start_game(self):
        """
        Метод начинающий игру.
        Возвращает: 0 после удачного завершения игры.
        """
        print(TicTac.mess_dict['Start'])

        choose_side = -1
        while choose_side == -1:
            choose_side = TicTac.validate_input(input())

            if choose_side == -1:
                print(TicTac.mess_dict['Err: bad format'])
            elif choose_side not in [1, 2]:
                print(TicTac.mess_dict['Err: bad value'])
                choose_side = -1
            else:
                human_side = TicTac.icon_dict[choose_side % 2]
                computer_side = TicTac.icon_dict[(choose_side + 1) % 2]

        choose_side %= 2
        winner = -1

        for step in range(1, TicTac.size ** 2 + 1):
            TicTac.show_board(self)
            TicTac.make_move(self, step, choose_side,
                             human_side, computer_side)
            if step >= 5:
                winner = TicTac.check_winner(self)

            if winner != -1:
                break

        TicTac.show_board(self)

        if TicTac.icon_dict[winner] == human_side:
            print(TicTac.mess_dict['Win'])
        elif TicTac.icon_dict[winner] == computer_side:
            print(TicTac.mess_dict['Lose'])
        else:
            print(TicTac.mess_dict['Draw'])

        return 0

    def make_move(self, step, choose_side, human_side, computer_side):
        """
        Метод делает ход.
        """
        if step % 2 == choose_side:
            print(TicTac.mess_dict['Chose cell'])
            cell = TicTac.validate_cell(self, input())
            while cell == -1:
                cell = TicTac.validate_cell(self, input())
            self.board[cell] = human_side
        else:
            cell = TicTac.computer_move(self, human_side, computer_side)
            self.board[cell] = computer_side

    def way_to_wins(self, side):
        """
        Метод, который пытается найти стратегию для победы на следующий ход.
        Возвращает: номер победной ячейки либо -1

        """
        for cell in range(TicTac.size ** 2):
            if TicTac.is_free_cell(self, cell):
                self.board[cell] = side
                if TicTac.icon_dict[TicTac.check_winner(self)] == side:
                    self.board[cell] = cell + 1
                    return cell
                self.board[cell] = cell + 1
        return -1

    def computer_move(self, human_side='X', computer_side='O'):
        """
        Метод, который производит ход компьютера.
        Возвращает: номер ячейки.

        """
        cell = TicTac.way_to_wins(self, computer_side)
        if cell != -1:
            return cell

        cell = TicTac.way_to_wins(self, human_side)

        if cell != -1:
            return cell

        for move in TicTac.computer_moves:
            if TicTac.is_free_cell(self, move):
                return move

        return -1

    def check_winner(self):
        """
        Метод определяет есть ли победители в данный момент.
        Возвращает: числовой определитель победителя, либо -1.

        """
        res = -1
        for line in self.win_line:
            if [self.board[cell] for cell in line] == ['X']*self.size:
                res = 1
            elif [self.board[cell] for cell in line] == ['O']*self.size:
                res = 0

        return res


if __name__ == '__main__':
    GAME = TicTac()
    GAME.start_game()
