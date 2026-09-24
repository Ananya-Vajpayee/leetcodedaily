class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        for i, num in enumerate(nums):
            if digit_sum(num) == i:
                return i
        return -1