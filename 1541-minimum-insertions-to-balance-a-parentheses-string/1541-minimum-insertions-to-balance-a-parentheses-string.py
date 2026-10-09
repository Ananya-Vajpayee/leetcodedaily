class Solution:
    def minInsertions(self, s: str) -> int:
        ins = 0   # insertions made so far
        need = 0  # ')' still required for the '(' seen so far

        for c in s:
            if c == '(':
                if need % 2 == 1:   # previous '(' has only one ')'
                    ins += 1
                    need -= 1
                need += 2
            else:
                need -= 1
                if need == -1:      # unmatched ')', insert a '('
                    ins += 1
                    need = 1

        return ins + need