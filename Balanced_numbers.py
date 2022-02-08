import unittest


def check_first_second_half(first_half, second_half):
    first_half_number = 0
    second_half_number = 0
    for c in first_half:
        first_half_number += int(c)
    for c in second_half:
        second_half_number += int(c)
    if first_half_number == second_half_number:
        return True
    else:
        return False


def is_number_balanced(number):
    number = str(number)
    half = len(number) // 2
    if len(number) == 1:
        return True
    elif len(number) % 2 == 0:
        first_half = number[:half]
        second_half = number[half:]
        return check_first_second_half(first_half, second_half)
    else:
        first_half = number[:half]
        second_half = number[half + 1:]
        return check_first_second_half(first_half, second_half)


class TestIsNumberBalanced(unittest.TestCase):

    def test_is_number_balanced(self):
        self.assertEqual(is_number_balanced(9), True)
        self.assertEqual(is_number_balanced(4518), True)
        self.assertEqual(is_number_balanced(28471), False)
        self.assertEqual(is_number_balanced(1238033), True)


if __name__ == '__main__':
    unittest.main()
