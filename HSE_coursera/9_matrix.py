from sys import stdin
from typing import List


class Matrix:
    def __init__(self, matrix: List):
        self.matrix = matrix.copy()

    def __str__(self):
        s = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if j == len(self.matrix[i]) - 1:
                    s += f"{self.matrix[i][j]}"
                else:
                    s += f"{self.matrix[i][j]}\t"
            if i != len(self.matrix) - 1:
                s += "\n"
            else:
                pass
        return s

    def size(self):
        a = len(self.matrix)
        b = len(self.matrix[0])
        return a, b


if __name__ == '__main__':
    exec(stdin.read())
