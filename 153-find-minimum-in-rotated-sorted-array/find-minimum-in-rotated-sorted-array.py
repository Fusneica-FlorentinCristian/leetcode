class Solution:
    def findMin(self, nums: List[int]) -> int:
        lenthOfNums = len(nums) - 1
        lo = 0
        hi = lenthOfNums
        
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_number = nums[mid]
            
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            elif nums[mid] < nums[lenthOfNums]:
                hi = mid - 1  
            
            else:
                lo = mid + 1
        
        return nums[0]