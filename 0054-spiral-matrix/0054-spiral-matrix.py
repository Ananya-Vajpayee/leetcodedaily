class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        n = len(matrix)
        m = len(matrix[0])

        top, bottom = 0, n - 1
        left, right = 0, m - 1

        while top <= bottom and left <= right:
            # 1. Traverse left → right along the top row
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # 2. Traverse top → bottom along the right column
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 3. Traverse right → left along the bottom row (if it still exists)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # 4. Traverse bottom → top along the left column (if it still exists)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result