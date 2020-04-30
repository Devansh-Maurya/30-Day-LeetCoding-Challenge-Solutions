class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        
        count = 0
        maxlen = 0
        
        for i, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1
                
            if count not in d:
                d[count] = i
            
            maxlen = max(maxlen, i - d[count])
        return maxlen
