class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        intervals = []
        for c in first:
            start, end = first[c], last[c]
            i = start
            while i <= end:
                ch = s[i]
                # expand window if this char's occurrences go outside
                if first[ch] < start:
                    start = first[ch]
                    i = start
                    continue
                if last[ch] > end:
                    end = last[ch]
                i += 1
            intervals.append((start, end))

        # Greedy: sort by end, pick non-overlapping
        intervals.sort(key=lambda x: x[1])
        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end

        return result