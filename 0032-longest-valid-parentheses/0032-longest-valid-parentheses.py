class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0

        # Left to right: catches cases where ')' is in excess.
        open_, close = 0, 0
        for ch in s:
            if ch == '(':
                open_ += 1
            else:
                close += 1
            if open_ == close:
                best = max(best, 2 * close)
            elif close > open_:
                open_ = close = 0

        # Right to left: catches cases where '(' is in excess.
        open_, close = 0, 0
        for ch in reversed(s):
            if ch == '(':
                open_ += 1
            else:
                close += 1
            if open_ == close:
                best = max(best, 2 * open_)
            elif open_ > close:
                open_ = close = 0

        return best