class Solution:
    def search(self, nums: list[int], target: int) -> int:
        res=-1
        for i in range(len(nums)):
            if nums[i]==target:
                res=i
        return res