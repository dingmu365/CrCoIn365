# Q8: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0
import unittest
from copy import deepcopy
def zero_matrix(matrix):
    rows = set()
    columns = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i in rows) or (j in columns):
                matrix[i][j] = 0

    return matrix


def zero_matrix_pythonic(matrix):
    matrix = [["X" if x == 0 else x for x in row] for row in matrix]
    indices = []  # indice is to mark the column
    for idx, row in enumerate(matrix):
        if "X" in row:
            # for i,j => index, value
            indices = indices + [i for i, j in enumerate(row) if j == "X"]
            # make the row to zero first
            matrix[idx] = [0] * len(matrix[0])
    # make the columns to zero now
    # row.index(value) => return value referring index
    matrix = [[0 if row.index(i) in indices else i for i in row] for row in matrix]
    return matrix


matrix = zero_matrix_pythonic([
                                [1, 2, 3, 4, 0],
                                [6, 0, 8, 9, 10],
                                [11, 12, 13, 14, 15],
                                [16, 0, 18, 19, 20],
                                [21, 22, 23, 24, 25],])

class Test(unittest.TestCase):

    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    testable_functions = [zero_matrix, zero_matrix_pythonic]

    def test_zero_matrix(self):
        for f in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = deepcopy(test_matrix)
                assert f(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()