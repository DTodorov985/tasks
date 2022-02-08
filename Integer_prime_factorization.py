import unittest


def is_prime(n):
    if n < 2:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


def next_prime(n):
    n += 1

    while not is_prime(n):
        n += 1

    return n


def prime_factorization(n):
    result = []

    p = 2

    while n != 1:
        a = 0

        while n % p == 0:
            a += 1
            n = n // p

        if a > 0:
            result.append((p, a))

        p = next_prime(p)

    return result


class TestPrimeFactorization(unittest.TestCase):

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(2), [(2, 1)])
        self.assertEqual(prime_factorization(4), [(2, 2)])
        self.assertEqual(prime_factorization(10), [(2, 1), (5, 1)])
        self.assertEqual(prime_factorization(14), [(2, 1), (7, 1)])
        self.assertEqual(prime_factorization(356), [(2, 2), (89, 1)])
        self.assertEqual(prime_factorization(89), [(89, 1)])
        self.assertEqual(prime_factorization(1000), [(2, 3), (5, 3)])


if __name__ == '__main__':
    unittest.main()
