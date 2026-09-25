class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        self.i = 0
        s = expression

        def parseExpr():
            # handles union: term , term , term ...
            groups = [parseTerm()]
            while self.i < len(s) and s[self.i] == ',':
                self.i += 1
                groups.append(parseTerm())
            result = set()
            for g in groups:
                result |= g
            return result

        def parseTerm():
            # handles concatenation: factor factor factor ...
            result = {""}
            while self.i < len(s) and s[self.i] not in ',}':
                factor = parseFactor()
                result = {a + b for a in result for b in factor}
            return result

        def parseFactor():
            if s[self.i] == '{':
                self.i += 1  # skip '{'
                result = parseExpr()
                self.i += 1  # skip '}'
                return result
            else:
                # a run of lowercase letters
                start = self.i
                while self.i < len(s) and s[self.i].islower():
                    self.i += 1
                return {s[start:self.i]}

        return sorted(parseExpr())