class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0   # min and max possible number of unmatched '('

        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1   # treat as ')'
                hi += 1   # treat as '('

            if hi < 0:    # too many ')' even with every '*' as '('
                return False
            lo = max(lo, 0)

        return lo == 0