class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mc=mg=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                mc+=nums[i]
            else:
                mc=nums[i]
            mg=max(mg,mc)
        return mg            