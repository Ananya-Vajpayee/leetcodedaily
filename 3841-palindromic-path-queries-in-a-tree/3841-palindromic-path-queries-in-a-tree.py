from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        chars = [ord(c) - 97 for c in s]
        LOG = max(1, n.bit_length())

        par = [-1] * n
        tin = [0] * n
        P0 = [0] * n
        P0[0] = 1 << chars[0]
        order = []

        stack = [0]
        timer = 0
        while stack:
            v = stack.pop()
            tin[v] = timer
            timer += 1
            order.append(v)
            for w in adj[v]:
                if w != par[v]:
                    par[w] = v
                    P0[w] = P0[v] ^ (1 << chars[w])
                    stack.append(w)

        sz = [1] * n
        for v in reversed(order):
            if par[v] != -1:
                sz[par[v]] += sz[v]
        tout = [tin[v] + sz[v] - 1 for v in range(n)]

        # binary lifting (root's parent = itself)
        base = [p if p != -1 else 0 for p in par]
        up = [base]
        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def is_anc(a, b):
            return tin[a] <= tin[b] <= tout[a]

        def lca(a, b):
            if is_anc(a, b):
                return a
            if is_anc(b, a):
                return b
            for j in range(LOG - 1, -1, -1):
                x = up[j][a]
                if not is_anc(x, b):
                    a = x
            return up[0][a]

        # Fenwick tree: range XOR update, point query
        bit = [0] * (n + 2)

        def add(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def pval(v):
            return P0[v] ^ prefix(tin[v])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                x, c = int(parts[1]), ord(parts[2]) - 97
                if c != chars[x]:
                    d = (1 << chars[x]) ^ (1 << c)
                    add(tin[x], d)
                    add(tout[x] + 1, d)
                    chars[x] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                m = pval(u) ^ pval(v) ^ (1 << chars[l])
                ans.append((m & (m - 1)) == 0)
        return ans