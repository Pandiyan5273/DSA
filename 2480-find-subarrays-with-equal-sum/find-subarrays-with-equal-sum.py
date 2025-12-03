class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        freq={}
        for i in range(len(nums)-1):
            s=nums[i]+nums[i+1]
            if freq.get(s,0)+1>1:
                return True
            else:

                freq[s]=freq.get(s,0)+1
        return False