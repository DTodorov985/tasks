import unittest


def iban_formatter(iban):
    result = ''
    counter = 0
    if len(iban) == 22:
        for c in iban:
            if counter % 4 == 0:
                result += ' '
                result += c
                counter += 1
            else:
                result += c
                counter += 1
        counter = 0
        return result.strip()
    elif len(iban) == 27:
        result = iban
        return result.strip()
    else:
        return F"Please check the iban scriptures"


class TestIbanFormatter(unittest.TestCase):

    def test_with_len_22(self):
        self.assertEqual(iban_formatter("BG80BNBG96611020345678"), "BG80 BNBG 9661 1020 3456 78")
        self.assertEqual(iban_formatter("BG14TTBB94005362446381"), "BG14 TTBB 9400 5362 4463 81")
        self.assertEqual(iban_formatter("BG91UNCR70001864961754"), "BG91 UNCR 7000 1864 9617 54")

    def test_with_len_27(self):
        self.assertEqual(iban_formatter("BG80 BNBG 9661 1020 3456 78"), "BG80 BNBG 9661 1020 3456 78")


if __name__ == '__main__':
    unittest.main()
