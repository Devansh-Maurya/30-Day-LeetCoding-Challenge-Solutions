class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        nearest = len(nums) - 1
        
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= nearest:
                nearest = i
        
        return nearest == 0
        
        #return jump(nums, 0, {})
        
# Old recursive solution        
def jump(nums, start, dp):
    if start == len(nums) - 1:
        return True
    
    ans = False
    
    for i in range(nums[start], 0, -1):
        idx = start + i
        if idx < len(nums):
            if idx in dp:
                return dp[idx]
            dp[idx] = jump(nums, idx, dp)
            if dp[idx]:
                dp[start] = True
                return True
    dp[start] = ans
    return ans
        
