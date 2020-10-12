import unittest
import my_list


class MyListTest(unittest.TestCase):
    """
    Тесты для my_list
    """
    def test_add(self):
        list1 = my_list.MyList([5, 1, 3])
        list2 = my_list.MyList([1, 2, 7])

        with self.subTest(0):
            self.assertEqual(list1 + list2, [6, 3, 10])

        list1 = my_list.MyList([5, 1, 3, 4])
        list2 = my_list.MyList([1, 2, 7])

        with self.subTest(1):
            self.assertEqual(list1 + list2, [6, 3, 10, 4])

        list1 = my_list.MyList([5, 1, 3, 4])
        list2 = my_list.MyList([])

        with self.subTest(2):
            self.assertEqual(list1 + list2, [5, 1, 3, 4])

    def test_sub(self):
        list1 = my_list.MyList([5, 1, 3])
        list2 = my_list.MyList([1, 2, 7])

        with self.subTest(0):
            self.assertEqual(list1 - list2, [4, -1, -4])

        list1 = my_list.MyList([5, 1, 3, 4])
        list2 = my_list.MyList([1, 2, 7])

        with self.subTest(1):
            self.assertEqual(list1 - list2, [4, -1, -4, 4])

        list1 = my_list.MyList([])
        list2 = my_list.MyList([5, 1, 3, 4])

        with self.subTest(2):
            self.assertEqual(list1 - list2, [-5, -1, -3, -4])

    def test_equal(self):
        list1 = my_list.MyList([5, 1, 3])
        list2 = my_list.MyList([1, 2, 7])

        with self.subTest(0):
            self.assertEqual(list1 == list2, False)

        list1 = my_list.MyList([5, 1, 3, 1])
        list2 = my_list.MyList([1, 2, 7])

        with self.subTest(1):
            self.assertEqual(list1 == list2, True)

        list1 = my_list.MyList([])
        list2 = my_list.MyList([0, 0, 0])

        with self.subTest(2):
            self.assertEqual(list1 == list2, True)

        list1 = my_list.MyList([5, 1, 3, 1])

        with self.subTest(3):
            self.assertEqual(list1 == 10, False)

        with self.subTest(4):
            self.assertEqual(list1 == (5, 1, 3, 1), False)

    def test_mul(self):
        list1 = my_list.MyList([5, 1, 3])

        with self.subTest(0):
            self.assertEqual(2 * list1, [10, 2, 6])

        list1 = my_list.MyList([5, 1, 3, 4])

        with self.subTest(1):
            self.assertEqual(list1 * 0.5, [2.5, 0.5, 1.5, 2.])


if __name__ == '__main__':
    unittest.main()
