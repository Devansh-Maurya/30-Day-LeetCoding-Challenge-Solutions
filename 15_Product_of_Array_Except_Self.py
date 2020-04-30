class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]
        prod = 1
        
        for i in range(1, len(nums)):
            prod = prod * nums[i-1]
            ans[i] = prod
        
        prod = 1
        for i in range(len(nums)-2, -1, -1):
            prod = prod * nums[i+1]
            ans[i] = ans[i]*prod
            
        return ans
        
