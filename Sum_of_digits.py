import unittest


def sum_of_digits(n):
    total_sum = 0
    for c in str(n):
        try:
            total_sum += int(c)
        except:
            continue
    return total_sum


class TestSum(unittest.TestCase):

    def test_sum_with_positive(self):
        self.assertEqual(sum_of_digits(1325132435356), 43)
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(6), 6)

    def test_sum_with_negative(self):
        self.assertEqual(sum_of_digits(-10), 1)


if __name__ == '__main__':
    unittest.main()
