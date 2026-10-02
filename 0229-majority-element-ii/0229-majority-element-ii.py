class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1=nums[0]
        candidate2=nums[0]
        count1=0
        count2=0
        verified1=0
        verified2=0
        for value in nums:
            if value==candidate1:
                count1+=1
            elif value==candidate2:
                count2+=1
            elif count1 == 0:
                candidate1 = value
                count1 = 1
            elif count2 == 0:
                candidate2 = value
                count2 = 1
            else:
                count1-=1
                count2-=1
        for value in nums:
            # An occurrence of the first candidate increases its verified count.
            if value == candidate1:
                verified1 += 1
            # An occurrence of the second candidate increases its verified count.
            elif value == candidate2:
                verified2 += 1
 
        threshold = len(nums) // 3
        answer: list[int] = []
 
        # Include the first candidate only when its real frequency qualifies.
        if verified1 > threshold:
            answer.append(candidate1)
 
        # Include a distinct second candidate only when it also qualifies.
        if candidate2 != candidate1 and verified2 > threshold:
            answer.append(candidate2)
 
        return answer