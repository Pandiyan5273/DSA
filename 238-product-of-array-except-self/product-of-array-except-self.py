class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        f=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            f[i]=pre
            pre=nums[i]*pre
        suf=1
        for i in range(len(nums)-1,-1,-1):
            f[i]=f[i]*suf
            suf=nums[i]*suf
        return f