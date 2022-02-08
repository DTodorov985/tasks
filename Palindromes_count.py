import unittest


def check_is_palindrome(n):
    n = str(n)
    first = n
    second = n[::-1]
    if first == second:
        return True
    else:
        return False


def palindromes_count(n):
    palindrome_count = 0
    while 10 <= n <= 99999:
        for number in range(10, n + 1):
            if check_is_palindrome(number):
                palindrome_count += 1
        break
    return palindrome_count


class TestPalindromesCount(unittest.TestCase):

    def test_palindromes_count(self):
        self.assertEqual(palindromes_count(10), 0)
        self.assertEqual(palindromes_count(20), 1)
        self.assertEqual(palindromes_count(101), 10)
        self.assertEqual(palindromes_count(92009), 1009)
        self.assertEqual(palindromes_count(99999), 1089)


if __name__ == '__main__':
    unittest.main()
