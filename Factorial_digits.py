import unittest


def fact(n):
    """returns factorial of n."""
    if n <= 1:
        return 1
    return n * fact(n - 1)


def fact_digits(n):
    total_sum = 0
    for c in str(n):
        try:
            total_sum += fact(int(c))
        except:
            continue
    return total_sum


class TestFactDigits(unittest.TestCase):

    def test_fact_digits(self):
        self.assertEqual(fact_digits(101), 3)
        self.assertEqual(fact_digits(111), 3)
        self.assertEqual(fact_digits(145), 145)
        self.assertEqual(fact_digits(999), 1088640)


if __name__ == '__main__':
    unittest.main()
