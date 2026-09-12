from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Sort original indices by each interval's end time
        arr = sorted(range(n), key=lambda i: intervals[i][1])
        ends = [intervals[i][1] for i in arr]

        # dp[i][k] = (best score, sorted list of original indices) using first i sorted
        # intervals, choosing at most k
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            idx = arr[i - 1]
            l, r, w = intervals[idx]
            # count of prior sorted intervals whose end < l (strictly non-overlapping)
            j = bisect_left(ends, l, 0, i - 1)

            for k in range(5):
                best = dp[i - 1][k]          # option: skip this interval
                if k > 0:
                    prev_score, prev_idx = dp[j][k - 1]
                    new_score = prev_score + w
                    new_idx = sorted(prev_idx + [idx])
                    if new_score > best[0] or (new_score == best[0] and new_idx < best[1]):
                        best = (new_score, new_idx)   # option: take this interval
                dp[i][k] = best

        return dp[n][4][1]