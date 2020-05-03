class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l = 0
        r = len(nums)-1
        
        while l < r:
            mid = l + (r - l)//2
            
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
                
        
        start = 0
        end = len(nums) - 1
        
        if target <= nums[-1]:
            start = l
        else:
            end = l-1
            
        while start <= end:
            mid = start + (end - start)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return -1
                
