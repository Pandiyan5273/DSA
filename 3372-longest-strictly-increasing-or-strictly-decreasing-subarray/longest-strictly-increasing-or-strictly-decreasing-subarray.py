class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxl=0
        for i in range(len(nums)):
            curr=1
            for j in range(i+1,len(nums)):
                if nums[j]>nums[j-1]:
                    curr+=1
                else:
                    break
            maxl=max(maxl,curr)        
        for i in range(len(nums)):
            curr=1
            for j in range(i+1,len(nums)):
                if nums[j]<nums[j-1]:
                    curr+=1
                else:
                    break
            maxl=max(maxl,curr)        
        return maxl                        