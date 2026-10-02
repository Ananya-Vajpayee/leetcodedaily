class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        nums = nums[:]  # avoid mutating the caller's list

        def sort_and_count(lo: int, hi: int) -> int:
            if hi - lo <= 1:
                return 0

            mid = (lo + hi) // 2
            pairs = sort_and_count(lo, mid) + sort_and_count(mid, hi)

            # Both halves are sorted. As the left value grows, the number of
            # right values it beats only grows, so `right` never moves backward.
            right = mid
            for left in range(lo, mid):
                while right < hi and nums[left] > 2 * nums[right]:
                    right += 1
                pairs += right - mid

            # Merge the two sorted halves.
            nums[lo:hi] = sorted(nums[lo:hi])
            return pairs

        return sort_and_count(0, len(nums))
        