import unittest
import lru_cache


class LruCacheTest(unittest.TestCase):
    """
    Тесты для lru-cache
    """
    def setUp(self):
        self.lru_cache = lru_cache.LRUCache(5)

    def test_get(self):
        self.lru_cache.set('Jesse', 'Pinkman')
        self.lru_cache.set('Walter', 'White')
        self.lru_cache.set('Jesse', 'James')

        with self.subTest(0):
            self.assertEqual(self.lru_cache.get('Jesse'), 'James')

        self.lru_cache.delete('Walter')

        with self.subTest(1):
            self.assertEqual(self.lru_cache.get('Walter'), '')

        self.lru_cache.set('Jonh', 'Snow')
        self.lru_cache.set('Ned', 'Stark')
        self.lru_cache.set('Frodo', 'Baggins')
        self.lru_cache.set('William', 'Butcher')
        self.lru_cache.set('Gustavo', 'Frink')

        with self.subTest(2):
            self.assertEqual(self.lru_cache.get('Jesse'), '')



if __name__ == '__main__':
    unittest.main()
