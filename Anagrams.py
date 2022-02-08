import unittest


def anagrams(word1, word2):
    (word1, word2) = (word1.lower(), word2.lower())
    dictionary = {}
    for c in word1:
        if c not in dictionary:
            dictionary[c] = 0
        dictionary[c] += 1
    for c in word2:
        if c not in dictionary:
            return False
        else:
            dictionary[c] -= 1
            if dictionary[c] == 0:
                dictionary.pop(c)
    return True


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        self.assertEqual(anagrams("listen", "silent"), True)
        self.assertEqual(anagrams("LISTEN", "silent"), True)
        self.assertEqual(anagrams("python", "ruby"), False)
        self.assertEqual(anagrams("New York Times", "monkeys write"), True)
        self.assertEqual(anagrams("snake", "sssnakee"), False)


if __name__ == '__main__':
    unittest.main()
