class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        s = [0] * (4 * n)
        q = [0] * (4 * n)
        lz = [0] * (4 * n)

        def apply(o, ln, k):
            q[o] = (q[o] + 2 * k * s[o] + k * k * ln) % MOD
            s[o] = (s[o] + k * ln) % MOD
            lz[o] = (lz[o] + k) % MOD

        def update(o, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(o, r - l + 1, 1)
                return
            m = (l + r) // 2
            if lz[o]:
                apply(2 * o, m - l + 1, lz[o])
                apply(2 * o + 1, r - m, lz[o])
                lz[o] = 0
            if ql <= m:
                update(2 * o, l, m, ql, qr)
            if qr > m:
                update(2 * o + 1, m + 1, r, ql, qr)
            s[o] = (s[2 * o] + s[2 * o + 1]) % MOD
            q[o] = (q[2 * o] + q[2 * o + 1]) % MOD

        last = {}
        ans = 0
        for i, x in enumerate(nums):
            update(1, 0, n - 1, last.get(x, -1) + 1, i)
            last[x] = i
            ans = (ans + q[1]) % MOD
        return ans