class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        n = len(nums1)
        d = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
        d.append(0)

        i = 0
        while i < n and k > 0:
            cnt = i + 1
            need = (d[i] - d[i + 1]) * cnt
            if need <= k:
                k -= need
                i += 1
            else:
                drop, rem = divmod(k, cnt)
                level = d[i] - drop
                total = rem * (level - 1) ** 2 + (cnt - rem) * level ** 2
                total += sum(x * x for x in d[cnt:n])
                return total

        # top i elements were all leveled down to d[i]
        return i * d[i] ** 2 + sum(x * x for x in d[i:n])