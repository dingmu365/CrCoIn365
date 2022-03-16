# Q5 One Away
# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to
# check if they are one edit or zero edits away.

# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# Hints:#23, #97, #130
import unittest
import time


def one_away(s1, s2):
    if s1 == s2:
        return True
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) == 0 | len(s2) == 0:
        return True
    if len(s1) < len(s2):
        str1 = s2
        str2 = s1
    else:
        str1 = s1
        str2 = s2
    check_list = [0] * 128
    for char in str1:
        check_list[ord(char)] += 1
    for char in str2:
        if check_list[ord(char)] != 0:
            check_list[ord(char)] -= 1

    if abs(sum(check_list)) > 1:
        return False
    return True


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),#??? why
    ]

    testable_functions = [one_away]

    def test_one_away(self):

        for f in self.testable_functions:

            for s1, s2, expectation in self.test_cases:
                errorinfo = f.__name__ + "_" + s1 + "_" + s2 + "_" + str(f(s1, s2)) + "_" + str(expectation)

                assert f(s1, s2) == expectation, errorinfo
        #


if __name__ == "__main__":
    unittest.main()
