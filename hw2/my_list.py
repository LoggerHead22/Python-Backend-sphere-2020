""" Модуль с классов MyList - список с перегруженными оперциями"""

import numbers


class MyList(list):

    'Класс отнаследованный от списка с перегруженными операциями'

    def __eq__(self, other):
        'Перегрузка оператора "==" на равенство сумм'
        if isinstance(other, list):
            res = sum(self) == sum(other)
        else:
            res = False
        return res

    def add_sub_func(self, other, function):
        'Вспомогательный метод для применения function к общей части массивов'
        add_sub_list = list(map(function, zip(self, other)))
        if len(self) > len(other):
            add_sub_list += self[len(other):]
        else:
            add_sub_list += other[len(self):]

        return add_sub_list

    def __add__(self, other):
        'Перегрузка оператора "+" на поэлементное суммирование'
        if isinstance(other, list):
            add_list = MyList.add_sub_func(self, other, lambda x: x[0] + x[1])
        else:
            mess = f"unsupported operand type for +: list and {type(other)}"
            raise TypeError(mess)
        return MyList(add_list)

    def __sub__(self, other):
        'Перегрузка оператора "-" на поэлементное вычитание'
        if isinstance(other, list):
            sub_list = self.__add__(MyList(other)*-1)
        else:
            mess = f"unsupported operand type for -: list and {type(other)}"
            raise TypeError(mess)
        return MyList(sub_list)

    def __mul__(self, other):
        'Перегрузка оператора "*" на поэлементное умножение'
        if issubclass(type(other), numbers.Number) or\
                issubclass(type(other), numbers.Real):
            mult_list = MyList([other*item for item in self])
        else:
            mess = f"unsupported operand type for *: list and {type(other)}"
            raise TypeError(mess)
        return mult_list

    def __radd__(self, other):
        'Перегрузка оператора + слева'
        return self.__add__(other)

    def __rmul__(self, other):
        'Перегрузка оператора * слева'
        return self.__mul__(other)

    def __rsub__(self, other):
        'Перегрузка оператора - слева'
        return (self * -1).__add__(other)
