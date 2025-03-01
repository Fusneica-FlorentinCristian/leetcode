class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        for i in range(len(nums)):
            if nums[i] in d1:
                return d1[nums[i]], i
            d1[target - nums[i]] = i