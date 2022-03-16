#Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be
# limited to just dictionary words

#
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)
import unittest

def palindarome(input):
    input=input.lower()

    input=input.strip(" ")
    str2=input[::-1]
    for i in range(len(input)):
        if input[i]!=str2[i]:
            return False

    return True

def is_palindrome_permutation(input):
    #lowercase alphabet is from 97 to 122
    #uppercase alphabet is from 65 to 90

    check_list=[0]*26
    input=input.lower()
    input = "".join(filter( str.isalpha, input))
    # only keep alphabet in the string
    for char in input:
        check_list[ord(char)-97] +=1
    check_list_booleam=[x for x in check_list if x%2==1]

    if sum(check_list_booleam)>1:
        return False

    return True

class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [
        is_palindrome_permutation,
    ]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()


