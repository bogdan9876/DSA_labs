import unittest
import math

def find_min_speed(piles, H):
    def can_finish(speed):
        hours_needed = sum(math.ceil(pile / speed) for pile in piles)
        return hours_needed <= H

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2

        if not can_finish(mid):
            left = mid + 1
        else:
            right = mid

    return left


class TestMinEatingSpeed(unittest.TestCase):

    def test_example_1(self):
        piles = [3, 6, 7, 11]
        H = 8
        self.assertEqual(find_min_speed(piles, H), 4)

    def test_example_2(self):
        piles = [30, 11, 23, 4, 20]
        H = 5
        self.assertEqual(find_min_speed(piles, H), 30)

    def test_example_3(self):
        piles = [30, 11, 23, 4, 20]
        H = 6
        self.assertEqual(find_min_speed(piles, H), 23)

if __name__ == '__main__':
    unittest.main()
