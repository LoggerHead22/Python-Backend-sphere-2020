"Lru-cache module"
from collections import OrderedDict


class LRUCache:

    'Lru-cache class'

    def __init__(self, capacity: int = 10) -> None:
        'Конструктор'
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> str:
        'Метод возвращающей значения для ключа - key'
        value = self.cache.get(key)
        if value is not None:
            self.cache.move_to_end(key)
        else:
            value = ''
        return value

    def set(self, key: str, value: str) -> None:
        'Метод устанавлювающий значения value для ключа key'
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def delete(self, key: str) -> None:
        'Метод удаляющий клюс key из кэша'
        if self.cache.get(key) is not None:
            del self.cache[key]
