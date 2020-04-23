class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 0
        
        while j < len(nums):
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j < len(nums):
                nums[i] = nums[j]
                i += 1
                j += 1
                
        for k in range(i, len(nums)):
            nums[k] = 0
