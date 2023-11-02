import unittest
from src.main import is_contain_cycle


class TestContainsCycle(unittest.TestCase):
    def test_1(self):
        # Перевіряємо при пустому графі
        graph = {}
        self.assertFalse(is_contain_cycle(graph))

    def test_2(self):
        # Перевіряємо граф який містить у собі цикл
        graph = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}
        self.assertTrue(is_contain_cycle(graph))

    def test_3(self):
        # Перевіряємо граф який не містить у собі цикл
        graph = {1: [2, 3], 2: [1], 3: [1, 4], 4: [3]}
        self.assertFalse(is_contain_cycle(graph))


if __name__ == "__main__":
    unittest.main()
