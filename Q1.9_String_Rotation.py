# Q9: Assumeyou have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
import unittest


def string_reverse(data):
    data = list(data)
    data.reverse()
    data = "".join(data)
    return data


def check_string_reverse(data1, data2):
    data1_rotated = string_reverse(data1)
    if data1_rotated == data2:
        return True
    return False


def check_string_rotation(data1, data2):
    if len(data1) == len(data2) != 0:
        return data2 in data1 * 2
    return False


def check_string_rotation_alternative(data1, data2):
    if len(data1) == len(data2) != 0:
        for i in range(len(data1)):
            data = data1[i:] + data1[:i]
            if data == data2:
                return True
    return False


class Test(unittest.TestCase):
    test_cases = [
        ( "erbottlewat","waterbottle", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]
    testable_functions=[
        check_string_rotation,
        check_string_rotation_alternative,
    ]

    def test_string_rotation(self):
        for f in self.testable_functions:
            for [s1, s2, expected] in self.test_cases:
                actual = f(s1, s2)
                assert actual == expected, s1 + " " + s2 + " " + str(actual)


if __name__ == "__main__":
    unittest.main()
