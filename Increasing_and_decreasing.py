import unittest
from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3


def increasing_or_decreasing(ns):
    length = len(ns)
    if length <= 1:
        return Monotonicity.NONE
    increasing = True
    decreasing = True
    for index in range(length - 1):
        a = ns[index]
        b = ns[index + 1]
        increasing = increasing and a < b
        decreasing = decreasing and a > b
    if increasing:
        return Monotonicity.INCREASING
    if decreasing:
        return Monotonicity.DECREASING
    return Monotonicity.NONE


class TestIncreasingOrDecreasing(unittest.TestCase):

    def test_increasing_or_decreasing(self):
        self.assertEqual(increasing_or_decreasing([1, 2, 3, 4, 5]), Monotonicity.INCREASING)
        self.assertEqual(increasing_or_decreasing([5, 6, -10]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([1, 1, 1, 1]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([9, 8, 7, 6]), Monotonicity.DECREASING)
        self.assertEqual(increasing_or_decreasing([]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([1]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([1, 100]), Monotonicity.INCREASING)
        self.assertEqual(increasing_or_decreasing([1, 100, 100]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([100, 1]), Monotonicity.DECREASING)
        self.assertEqual(increasing_or_decreasing([100, 1, 1]), Monotonicity.NONE)
        self.assertEqual(increasing_or_decreasing([100, 1, 2]), Monotonicity.NONE)


if __name__ == '__main__':
    unittest.main()
