class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total ^= num

        if total != 0:
            return len(nums)

        # total == 0: check if any non-zero element exists
        if any(num != 0 for num in nums):
            return len(nums) - 1

        return 0