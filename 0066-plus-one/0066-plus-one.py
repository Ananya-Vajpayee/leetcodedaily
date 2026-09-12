class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n-1,-1,-1):
         if digits[i]<9:
            digits[i]+=1
            return digits
         digits[i]=0
        #every digit is 9[9,9,9].This only executes if the for loop finishes without hitting return digits inside it — meaning every single digit was 9 (e.g. [9,9,9] → all turned to [0,0,0] during the loop). In that case, the number needs an extra digit at the front: 999 + 1 = 1000, so we prepend 1 to the now-all-zero array.
        return[1]+digits