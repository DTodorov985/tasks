import unittest


def is_prime(n):
    if n < 2:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


def goldbach(n):
    result = []
    if n % 2 == 1 or n <= 2:
        return None
    else:
        primes = [x for x in range(2, n)if is_prime(x)]
        used = set()
        for p1 in primes:
            for p2 in primes:
                if p1 + p2 == n:
                    pair = (p1, p2)
                    reversed_pair = (p2, p1)
                    if pair not in used and reversed_pair not in used:
                        used.add(pair)
                        result.append(pair)
    return result


class TestGoldbach(unittest.TestCase):

    def test_goldbach(self):
        self.assertEqual(goldbach(4), [(2, 2)])
        self.assertEqual(goldbach(6), [(3, 3)])
        self.assertEqual(goldbach(8), [(3, 5)])
        self.assertEqual(goldbach(10), [(3, 7), (5, 5)])
        self.assertEqual(goldbach(100), [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])
        self.assertEqual(goldbach(5), None)


if __name__ == '__main__':
    unittest.main()
