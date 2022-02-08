import unittest


def group(items):
    result = []
    length = len(items)
    index = 0
    while index < length:
        item = items[index]
        current_group = [item]
        lookup_index = index + 1
        while lookup_index < length and items[lookup_index] == item:
            current_group.append(items[lookup_index])
            lookup_index += 1
        result.append(current_group)
        index = lookup_index
    return result


KEYPAD = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
}


def numbers_to_message(pressed_sequence):
    letters = []
    grouped_pressed_sequence = group(pressed_sequence)
    upper = False
    for grouped in grouped_pressed_sequence:
        key = grouped[0]
        times_pressed = len(grouped)
        if key == -1:
            continue
        if key == 1:
            upper = True
            continue
        if key == 0:
            letters.append(" " * times_pressed)
            continue
        sequence = KEYPAD[key]
        letter = sequence[(times_pressed - 1) % len(sequence)]
        if upper:
            letter = letter.upper()
            upper = False
        letters.append(letter)
    return "".join(letters)


class TestNumbersToMessage(unittest.TestCase):

    def test_numbers_to_message(self):
        self.assertEqual(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]), "abc")
        self.assertEqual(numbers_to_message([2]), "a")
        self.assertEqual(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]), "Ivo e Panda")
        self.assertEqual(numbers_to_message([2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]), "aabbcc")


if __name__ == '__main__':
    unittest.main()
