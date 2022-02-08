import unittest


def nan():
    return ' NaN'


def nan_expand(times):
    result = ''
    flag = False
    for i in range(times + 1):
        if i == 0:
            result += ''
        else:
            result += " Not a"
            flag = True
    if flag:
        result += nan()
    return result.strip()


class TestNanExpand(unittest.TestCase):

    def test_nan_expand(self):
        self.assertEqual(nan_expand(0), "")
        self.assertEqual(nan_expand(1), "Not a NaN")
        self.assertEqual(nan_expand(2), "Not a Not a NaN")
        self.assertEqual(nan_expand(3), "Not a Not a Not a NaN")


if __name__ == '__main__':
    unittest.main()
