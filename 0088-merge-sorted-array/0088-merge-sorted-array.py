class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]   # drop nums2 into the placeholder slots
        nums1.sort()            # sort the whole thing