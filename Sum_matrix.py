import unittest


def sum_matrix(matrix):
    return sum([sum(x) for x in matrix])


class TestSumMatrix(unittest.TestCase):

    def test_sum_matrix(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        self.assertEqual(sum_matrix(m), 45)

        m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.assertEqual(sum_matrix(m), 0)

        m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

        self.assertEqual(sum_matrix(m), 55)


if __name__ == '__main__':
    unittest.main()
