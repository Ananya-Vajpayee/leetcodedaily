class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            l1 = nums1[i-1] if i else float('-inf')
            r1 = nums1[i] if i < m else float('inf')
            l2 = nums2[j-1] if j else float('-inf')
            r2 = nums2[j] if j < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2) if (m+n) % 2 else (max(l1,l2) + min(r1,r2)) / 2
            elif l1 > r2:
                hi = i - 1
            else:
                lo = i + 1