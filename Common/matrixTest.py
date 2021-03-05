import unittest

from Common.matrix import MatrixSolution


class MatrixTest(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.s = MatrixSolution()

    def test_addTwoArray(self):
        A = [1, 2, 0, 0]
        K = 34
        r = self.s.addToArrayForm(A, K)
        self.assertEqual(r, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
