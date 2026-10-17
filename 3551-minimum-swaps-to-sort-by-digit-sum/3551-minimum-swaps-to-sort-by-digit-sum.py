class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        arr = sorted((digit_sum(v), v, i) for i, v in enumerate(nums))
        # arr[i][2] = original index of the element that belongs at position i

        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue
            j = i
            cycle_len = 0
            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_len += 1
            swaps += cycle_len - 1
        return swaps