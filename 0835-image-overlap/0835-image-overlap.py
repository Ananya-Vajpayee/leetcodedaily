class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        if not ones1 or not ones2:
            return 0

        from collections import defaultdict
        count = defaultdict(int)

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shift = (x2 - x1, y2 - y1)
                count[shift] += 1

        return max(count.values())