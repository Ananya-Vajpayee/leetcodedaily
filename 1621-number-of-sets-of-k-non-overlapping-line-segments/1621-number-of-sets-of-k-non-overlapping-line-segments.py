class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        N = n + k - 1
        r = 2 * k
        
        # compute C(N, r) mod MOD directly (N <= ~2000, so this is fast)
        num = 1
        den = 1
        for i in range(r):
            num = num * (N - i) % MOD
            den = den * (i + 1) % MOD
        return num * pow(den, MOD - 2, MOD) % MOD