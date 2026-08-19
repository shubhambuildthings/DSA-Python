from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        result = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                result[c][r] = matrix[r][c]

        return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().transpose(matrix))