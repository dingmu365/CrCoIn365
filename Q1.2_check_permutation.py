# 1. Array and String
# Q2_Check permutation

# given two strings, write a method to decide if one is a permutation of the other.
# A Permutation of a string is another string that contains same characters, only the
# order of characters can be different. For example, “abcd” and “dabc” are Permutation of each other.


# A permutation is a mathematical technique that determines the number of possible arrangements
# in a set when the order of the arrangements matters. Common mathematical problems involve
# choosing only several items from a set of items in a certain order. 排序
from collections import Counter
import unittest


def check_permutation_sort(str1, str2):
    if len(str1) != len(str2):
        return False
    str1, str2 = sorted(str1), sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True


def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for char in str1:
        counter[ord(char)] += 1
    for char in str2:
        if counter[ord(char)]==0:
            return False
        else:
            counter[ord(char)]-= 1
    return True


def check_pertutation_pythonic(str1,str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1)==Counter(str2)

class UnitTest(unittest.TestCase):
    test_case=(
        ("dog","dgo",True),
        ("flower","wolfer",True),
        ("aaab","bbba",False)
    )

    test_functions=[
        check_pertutation_pythonic,
        check_permutation_by_count,
        check_permutation_sort,
    ]

    def test_cp(self):
        for function in self.test_functions:
            for s1,s2,expectation in self.test_case:
                errorinfo=function.__name__ +"_"+ s1 +"_"+ s2+"_"+ str(function(s1,s2))+"_"+ str(expectation)

                assert function(s1,s2) == expectation, errorinfo



if __name__=="__main__":
  unittest.main()
 #   check_permutation_by_count("dog","dgo")