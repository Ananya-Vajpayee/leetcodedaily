class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        k, r = divmod(sum, 9)
        res = "9" * k
        if k < num:
            res += str(r)
            res += "0" * (num - k - 1)
        return res