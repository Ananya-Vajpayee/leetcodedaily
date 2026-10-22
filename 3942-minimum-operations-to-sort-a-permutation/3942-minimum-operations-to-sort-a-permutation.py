class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        INF = float('inf')
        best = INF

        # ascending cyclic shift: nums[i] == (nums[0] + i) % n
        k = nums[0]
        if all(nums[i] == (k + i) % n for i in range(n)):
            best = min(best, (n - k) % n, k + 2 if k else 0)

        # descending cyclic shift: nums[i] == (nums[0] - i) % n
        c = nums[0]
        if all(nums[i] == (c - i) % n for i in range(n)):
            k = (c + 1) % n
            best = min(best, 1 + (n - k) % n, k + 1)

        return -1 if best == INF else best