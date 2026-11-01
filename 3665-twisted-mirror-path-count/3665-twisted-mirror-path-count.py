class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        R = [[0] * (n + 1) for _ in range(m + 1)]
        D = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    tot = 1 if (i == 0 and j == 0) else (R[i][j] + D[i][j]) % MOD
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + tot) % MOD
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + tot) % MOD
                else:
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + R[i][j]) % MOD
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + D[i][j]) % MOD

        return (R[m - 1][n - 1] + D[m - 1][n - 1]) % MOD