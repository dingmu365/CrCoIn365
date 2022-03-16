# Q6 String Compression

# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
import unittest



def string_compression_without_order(data):
    data = sorted(data)
    compressed = []
    char_current = None
    for i in range(len(data)):
        char = data[i]
        if i == 0:
            char_current = data

        else:
            if char != char_current:
                compressed.append(char_current + str(counter))
                counter = 0
                char_current = char
            counter += 1

    return compressed


def string_compression(data):
    compressed = []
    counter = 0
    for i in range(len(data)):
        if i != 0 and data[i] != data[i - 1]:
            compressed.append(data[i - 1] + str(counter))
            counter = 0
        counter += 1
    if counter:
        compressed.append(data[-1] + str(counter))

    return min(data, str("".join(compressed)), key=len)


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", "")
    ]
    testable_functions = [
        string_compression
    ]

    def test_string_compression(self):
        for f in self.testable_functions:

            for test_string, expected in self.test_cases:
                assert f(test_string) == expected, test_string + expected + " " + f(test_string)

#
if __name__ == "__main__":
    unittest.main()
