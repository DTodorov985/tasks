import unittest


def is_credit_card_valid(number):
    result = 0
    str_number = str(number)
    str_transformed_number = ''
    counter = 0
    for i in range(len(str_number)):
        if counter == 0:
            str_transformed_number += str_number[i]
            counter += 1
        elif counter == 1:
            num = int(str_number[i]) * 2
            for c in str(num):
                result += int(c)
            str_transformed_number += str(result)
            result = 0
            counter = 0
    for c in str_transformed_number:
        result += int(c)
    if result % 10 == 0:
        return True
    else:
        return False


class TestIsCreditCardValid(unittest.TestCase):

    def test_is_credit_card_valid(self):
        self.assertEqual(is_credit_card_valid(79927398713), True)
        self.assertEqual(is_credit_card_valid(79927398715), False)


if __name__ == '__main__':
    unittest.main()
