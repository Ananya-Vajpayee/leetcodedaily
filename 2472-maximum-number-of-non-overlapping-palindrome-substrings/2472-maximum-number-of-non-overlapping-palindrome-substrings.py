class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]  # option: skip s[i-1]
            for length in (k, k + 1):
                j = i - length
                if j >= 0 and is_pal(j, i - 1):
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]     