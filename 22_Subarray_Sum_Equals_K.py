class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = {}
        d[0] = 1
        ans = 0
        
        s = 0
        
        for num in nums:
            s += num

            if s - k in d:
                ans += d[s-k]
            
            if s not in d:
                d[s] = 0
            d[s] += 1
             
        return ans
    
